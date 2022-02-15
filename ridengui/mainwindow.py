# Built-in modules
import logging
import sys

# Third-party modules
if "PySide2" in sys.modules:
    from PySide2.QtCore import QSettings
    from PySide2.QtGui import QFontDatabase
    from PySide2.QtWidgets import QApplication, QMainWindow
elif "PySide6" in sys.modules:
    from PySide6.QtCore import QSettings
    from PySide6.QtGui import QFontDatabase
    from PySide6.QtWidgets import QApplication, QMainWindow
else:
    raise ModuleNotFoundError("PySide2 or PySide6 is required to run this program.")
from riden import Riden

# Local modules
from ridengui.about import AboutDialog
from ridengui.settings import SettingsWizard
from ridengui.ui.mainwindow import Ui_MainWindow
from ridengui.worker import Worker


class MainWindow(QMainWindow):
    def __init__(self, port: str = None, baudrate: int = None, address: int = None):
        super().__init__()

        logging.debug("Initializing MainWindow from mainwindow.ui")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        logging.debug("Initializing QSettings")
        self.settings = QSettings("ShayBox", "RidenGUI")

        if self.settings.value("first-run", 1) == 1:
            logging.debug("First run detected, showing settings wizard")
            SettingsWizard(self.settings, self).exec()

        logging.debug("Configuring fixed font for labels")
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font.setBold(True)
        font.setPointSize(36)
        self.ui.voltageInput.setFont(font)
        self.ui.voltageOutput.setFont(font)
        self.ui.currentOutput.setFont(font)
        self.ui.powerOutput.setFont(font)

        logging.debug("Resizing widgets and window to minimum size")
        self.adjustSize()
        self.resize(self.minimumSize())

        logging.debug("Initializing Riden library")
        self.r = Riden(
            port=port or self.settings.value("serial/port", "/dev/ttyUSB0"),
            baudrate=baudrate or int(self.settings.value("serial/baudrate", 115200)),
            address=address or int(self.settings.value("serial/address", 1)),
        )

        logging.debug("Loading custom stylesheets from settings")
        self.output_on = self.settings.value("style/output-on")
        self.output_off = self.settings.value("style/output-off")
        self.output_fault = self.settings.value("style/output-fault")

        # Precition output formats
        # Display formats on real devices
        # Model     V      I       P-on<99W P-on>99W
        # RD6006P   00.000 0.0000  00.000   000.00
        # RD6006    00.00  0.000   00.00    000.0
        # RD6012    00.00  00.00   00.00    000.0
        # RD6018    00.00  00.00   00.00    000.0

        logging.debug("Defining default format string settings for device type")
        self.default_voltage_input_format = "%05.2f"
        self.default_voltage_output_format = "%05.2f"
        self.default_current_output_format = "%05.2f"
        self.default_power_output_format = "%6.2f"
        self.default_voltage_max = 61.0
        self.default_current_max = 0.0

        if self.r.type == "RD6012":
            self.default_voltage_output_format = "%05.3f"
            self.default_current_output_format = "%05.4f"
            self.default_power_output_format = "%6.3f"
            self.default_current_max = 6.1
        elif self.r.type == "RD6006":
            self.default_current_output_format = "%04.3f"
            self.default_current_max = 6.1
        elif self.r.type == "RD6012":
            self.default_current_max = 12.1
        elif self.r.type == "RD6018":
            self.default_current_max = 18.1
        elif self.r.type == "RD6024":
            self.default_current_max = 24.1

        logging.debug("Loading custom format strings from settings")
        self.voltage_input_format = self.settings.value("format/voltage-input", self.default_voltage_input_format)
        self.voltage_output_format = self.settings.value("format/voltage-output", self.default_voltage_output_format)
        self.current_output_format = self.settings.value("format/current-output", self.default_current_output_format)
        self.power_output_format = self.settings.value("format/power-output", self.default_power_output_format)

        logging.debug("Defining temporary variables for live feedback")
        self.prev_v_set = self.r.v_set
        self.prev_i_set = self.r.i_set

        logging.debug("Connecting signals and slots")
        self.connect_signals()

        logging.debug("Setting permenant statusbar message")
        self.ui.statusbar.showMessage(
            "Connected to %s using %s at %s baud | FW: %s | SN: %s"
            % (
                self.r.type,
                self.r.serial.port,
                self.r.serial.baudrate,
                self.r.fw,
                self.r.sn,
            )
        )

        logging.debug("Starting worker thread")
        self.worker = Worker(self.r, self.settings, self)
        self.worker.update.connect(self.worker_signal)
        self.worker.start()

    def closeEvent(self, _):
        logging.debug("Saving settings to disk")
        self.settings.sync()

        logging.debug("Stopping worker thread")
        if hasattr(self, "worker"):
            self.worker.running = False
            if not self.worker.wait(1000):
                self.worker.terminate()
                self.worker.wait()

    def connect_signals(self):
        logging.debug("Connecting actionbar signals")
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionSettings.triggered.connect(lambda: SettingsWizard(self.settings, self).show())
        self.ui.actionAboutRiden.triggered.connect(lambda: AboutDialog(self).show())
        self.ui.actionAboutQt.triggered.connect(lambda: QApplication.aboutQt())

        logging.debug("Connecting voltage/current min/max DoubleSpinBoxes to Dials")
        self.ui.voltageMinDoubleSpin.valueChanged.connect(self.ui.voltageDial.setMinimum)
        self.ui.voltageMaxDoubleSpin.valueChanged.connect(self.ui.voltageDial.setMaximum)
        self.ui.currentMinDoubleSpin.valueChanged.connect(self.ui.currentDial.setMinimum)
        self.ui.currentMaxDoubleSpin.valueChanged.connect(self.ui.currentDial.setMaximum)

        logging.debug("Connecting voltage/current min/max to DoubleSpinBoxes")
        self.ui.voltageMinDoubleSpin.valueChanged.connect(self.ui.voltageDoubleSpin.setMinimum)
        self.ui.voltageMaxDoubleSpin.valueChanged.connect(self.ui.voltageDoubleSpin.setMaximum)
        self.ui.currentMinDoubleSpin.valueChanged.connect(self.ui.currentDoubleSpin.setMinimum)
        self.ui.currentMaxDoubleSpin.valueChanged.connect(self.ui.currentDoubleSpin.setMaximum)

        logging.debug("Loading voltage/current min/max values from settings")
        self.ui.voltageMinDoubleSpin.setValue(int(self.settings.value("limits/voltage-min", 0)) / 1000)
        self.ui.voltageMaxDoubleSpin.setValue(int(self.settings.value("limits/voltage-max", self.default_voltage_max)) / 1000)
        self.ui.currentMinDoubleSpin.setValue(int(self.settings.value("limits/current-min", 0)) / 1000)
        self.ui.currentMaxDoubleSpin.setValue(int(self.settings.value("limits/current-max", self.default_current_max)) / 1000)

        logging.debug("Connecting voltage/current DoubleSpinBoxes to Dials")
        self.ui.voltageDoubleSpin.valueChanged.connect(self.ui.voltageDial.setValue)
        self.ui.currentDoubleSpin.valueChanged.connect(self.ui.currentDial.setValue)

        logging.debug("Connecting voltage/current Dials to DoubleSpinBoxes")
        self.ui.voltageDial.valueChanged.connect(self.ui.voltageDoubleSpin.setValue)
        self.ui.currentDial.valueChanged.connect(self.ui.currentDoubleSpin.setValue)

        logging.debug("Loading voltage/current values from settings")
        self.ui.voltageDoubleSpin.setValue(self.r.v_set)
        self.ui.currentDoubleSpin.setValue(self.r.i_set)

        logging.debug("Connecting voltage/current min/max DoubleSpinBoxes to settings")
        self.ui.voltageMinDoubleSpin.valueChanged.connect(lambda v: self.settings.setValue("limits/voltage-min", v * 1000))
        self.ui.voltageMaxDoubleSpin.valueChanged.connect(lambda v: self.settings.setValue("limits/voltage-max", v * 1000))
        self.ui.currentMinDoubleSpin.valueChanged.connect(lambda i: self.settings.setValue("limits/current-min", i * 1000))
        self.ui.currentMaxDoubleSpin.valueChanged.connect(lambda i: self.settings.setValue("limits/current-max", i * 1000))

        logging.debug("Connecting voltage/current step to DoubleSpinBoxes")

        def voltageStep(step: str):
            decimals = self.ui.voltageStepCombo.currentIndex()
            self.ui.voltageDoubleSpin.setSingleStep(float(step))
            self.ui.voltageDoubleSpin.setDecimals(decimals)
            self.ui.voltageMinDoubleSpin.setDecimals(decimals)
            self.ui.voltageMaxDoubleSpin.setDecimals(decimals)

        def currentStep(step: str):
            decimals = self.ui.currentStepCombo.currentIndex()
            self.ui.currentDoubleSpin.setSingleStep(float(step))
            self.ui.currentDoubleSpin.setDecimals(decimals)
            self.ui.currentMinDoubleSpin.setDecimals(decimals)
            self.ui.currentMaxDoubleSpin.setDecimals(decimals)

        self.ui.voltageStepCombo.currentTextChanged.connect(lambda s: voltageStep(s))
        self.ui.currentStepCombo.currentTextChanged.connect(lambda s: currentStep(s))

        logging.debug("Loading voltage/current step values from settings")
        self.ui.voltageStepCombo.setCurrentText(self.settings.value("limits/voltage-step", "0.01"))
        self.ui.currentStepCombo.setCurrentText(self.settings.value("limits/current-step", "0.01"))

        logging.debug("Connecting voltage/current step to settings")
        self.ui.voltageStepCombo.currentTextChanged.connect(lambda s: self.settings.setValue("limits/voltage-step", s))
        self.ui.currentStepCombo.currentTextChanged.connect(lambda s: self.settings.setValue("limits/current-step", s))

        logging.debug("Connecting output button to riden")
        self.ui.outputPush.clicked.connect(lambda: self.r.set_output(not self.r.output))

        logging.debug("Connecting voltage/current DoubleSpinBoxes to riden")
        self.ui.voltageDoubleSpin.valueChanged.connect(lambda v: self.r.set_v_set(v) if self.ui.realtimeCheck.isChecked() else None)
        self.ui.currentDoubleSpin.valueChanged.connect(lambda i: self.r.set_i_set(i) if self.ui.realtimeCheck.isChecked() else None)

        logging.debug("Connecting voltage/current PushButtons to riden")
        self.ui.voltagePush.clicked.connect(lambda: self.r.set_v_set(self.ui.voltageDoubleSpin.value()))
        self.ui.currentPush.clicked.connect(lambda: self.r.set_i_set(self.ui.currentDoubleSpin.value()))

    def worker_signal(self):
        self.ui.keypad.setText("Locked" if self.r.keypad else "Unlocked")
        self.ui.constant.setText(self.r.cv_cc)
        self.ui.fault.setText("CC" if self.r.cv_cc == "CC" else self.r.ovp_ocp or "None")
        self.ui.energy.setText(f"{self.r.ah:.2f} Ah | {self.r.wh:.2f} Wh")
        self.ui.intTemp.setText(f"{self.r.int_c} °C | {self.r.int_f} °F")
        self.ui.extTemp.setText(f"{self.r.ext_c} °C | {self.r.ext_f} °F")
        self.ui.voltageInput.setText(self.voltage_input_format % self.r.v_in)
        self.ui.voltageOutput.setText(self.voltage_output_format % self.r.v_out)
        self.ui.currentOutput.setText(self.current_output_format % self.r.i_out)
        self.ui.powerOutput.setText(self.power_output_format % self.r.p_out)
        self.ui.outputPush.setText("CC" if self.r.cv_cc == "CC" else "ON" if self.r.output else "OFF")
        self.ui.outputPush.setStyleSheet(self.output_fault if self.r.cv_cc == "CC" else self.output_on if self.r.output else self.output_off)

        if self.ui.realtimeCheck.isChecked():
            self.ui.voltagePush.setEnabled(False)
            self.ui.currentPush.setEnabled(False)
        else:
            if self.ui.voltageDoubleSpin.value() != self.prev_v_set:
                self.ui.voltagePush.setEnabled(True)

            if self.r.v_set != self.prev_v_set:
                self.ui.voltagePush.setEnabled(False)
                self.ui.voltageDoubleSpin.setValue(self.r.v_set)
                self.prev_v_set = self.r.v_set

            if self.ui.currentDoubleSpin.value() != self.prev_i_set:
                self.ui.currentPush.setEnabled(True)

            if self.r.i_set != self.prev_i_set:
                self.ui.currentPush.setEnabled(False)
                self.ui.currentDoubleSpin.setValue(self.r.i_set)
                self.prev_i_set = self.r.i_set
