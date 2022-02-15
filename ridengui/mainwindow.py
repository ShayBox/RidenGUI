# Built-in modules
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
    def __init__(self):
        super().__init__()

        # Load mainwindow.ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load settings from disk
        self.settings = QSettings("ShayBox", "RidenGUI")

        # Show wizard on first run
        if self.settings.value("first-run", 1) == 1:
            SettingsWizard(self.settings, self).exec()

        # Set output text font to fixed-width, bold, and 36pt
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font.setBold(True)
        font.setPointSize(36)
        self.ui.voltageInput.setFont(font)
        self.ui.voltageOutput.setFont(font)
        self.ui.currentOutput.setFont(font)
        self.ui.powerOutput.setFont(font)

        # Adjust widget sizes and resize window
        self.adjustSize()
        self.resize(self.minimumSize())

        # Create Riden object
        self.r = Riden(
            port=self.settings.value("port", "/dev/ttyUSB0"),
            baudrate=int(self.settings.value("baudrate", 115200)),
            address=int(self.settings.value("address", 1)),
        )

        # Define stylesheet variables
        self.output_on = self.settings.value("output-on-style")
        self.output_off = self.settings.value("output-off-style")
        self.output_fault = self.settings.value("output-fault-style")

        # Precition output formats
        # Display formats on real devices
        # Model     V      I       P-on<99W P-on>99W
        # RD6006P   00.000 0.0000  00.000   000.00
        # RD6006    00.00  0.000   00.00    000.0
        # RD6012    00.00  00.00   00.00    000.0
        # RD6018    00.00  00.00   00.00    000.0

        # Define voltage/current/power defaults
        self.default_voltage_input_format = "%05.2f"
        self.default_voltage_output_format = "%05.2f"
        self.default_current_output_format = "%05.2f"
        self.default_power_output_format = "%6.2f"
        self.default_voltage_max = 61.0
        self.default_current_max = 0.0

        # Override defaults for some models
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

        # Define voltage/current/power format string variables
        self.voltage_input_format = self.settings.value("voltage-input-format", self.default_voltage_input_format)
        self.voltage_output_format = self.settings.value("voltage-output-format", self.default_voltage_output_format)
        self.current_output_format = self.settings.value("current-output-format", self.default_current_output_format)
        self.power_output_format = self.settings.value("power-output-format", self.default_power_output_format)

        # Define prev_v_set and prev_i_set variables
        self.prev_v_set = self.r.v_set
        self.prev_i_set = self.r.i_set

        # Connect signals
        self.connect_signals()

        # Show permenant message
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

        # Create worker for background polling
        self.worker = Worker(self.r, self.settings, self)
        self.worker.update.connect(self.worker_signal)
        self.worker.start()

    def closeEvent(self, _):
        # Save settings before closing
        self.settings.sync()

        # Stop the worker before closing
        if hasattr(self, "worker"):
            self.worker.running = False
            if not self.worker.wait(1000):
                self.worker.terminate()
                self.worker.wait()

    def connect_signals(self):
        # Connect actionbar signals
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionSettings.triggered.connect(lambda: SettingsWizard(self.settings, self).show())
        self.ui.actionAboutRiden.triggered.connect(lambda: AboutDialog(self).show())
        self.ui.actionAboutQt.triggered.connect(lambda: QApplication.aboutQt())

        # Connect voltage/current min/max DoubleSpinBoxes to Dials
        self.ui.voltageMinDoubleSpin.valueChanged.connect(self.ui.voltageDial.setMinimum)
        self.ui.voltageMaxDoubleSpin.valueChanged.connect(self.ui.voltageDial.setMaximum)
        self.ui.currentMinDoubleSpin.valueChanged.connect(self.ui.currentDial.setMinimum)
        self.ui.currentMaxDoubleSpin.valueChanged.connect(self.ui.currentDial.setMaximum)

        # Connect voltage/current min/max to voltage/current DoubleSpinBoxes
        self.ui.voltageMinDoubleSpin.valueChanged.connect(self.ui.voltageDoubleSpin.setMinimum)
        self.ui.voltageMaxDoubleSpin.valueChanged.connect(self.ui.voltageDoubleSpin.setMaximum)
        self.ui.currentMinDoubleSpin.valueChanged.connect(self.ui.currentDoubleSpin.setMinimum)
        self.ui.currentMaxDoubleSpin.valueChanged.connect(self.ui.currentDoubleSpin.setMaximum)

        # Load voltage/current min/max values for DoubleSpinBoxes
        self.ui.voltageMinDoubleSpin.setValue(int(self.settings.value("voltage-min", 0)) / 1000)
        self.ui.voltageMaxDoubleSpin.setValue(int(self.settings.value("voltage-max", self.default_voltage_max)) / 1000)
        self.ui.currentMinDoubleSpin.setValue(int(self.settings.value("current-min", 0)) / 1000)
        self.ui.currentMaxDoubleSpin.setValue(int(self.settings.value("current-max", self.default_current_max)) / 1000)

        # Connect voltage/current DoubleSpinBoxes to Dials
        self.ui.voltageDoubleSpin.valueChanged.connect(self.ui.voltageDial.setValue)
        self.ui.currentDoubleSpin.valueChanged.connect(self.ui.currentDial.setValue)

        # Connect voltage/current Dials to DoubleSpinBoxes
        self.ui.voltageDial.valueChanged.connect(self.ui.voltageDoubleSpin.setValue)
        self.ui.currentDial.valueChanged.connect(self.ui.currentDoubleSpin.setValue)

        # Load voltage/current values for DoubleSpinBoxes
        self.ui.voltageDoubleSpin.setValue(self.r.v_set)
        self.ui.currentDoubleSpin.setValue(self.r.i_set)

        # Connect voltage/current min/max DoubleSpinBoxes to settings
        self.ui.voltageMinDoubleSpin.valueChanged.connect(lambda v: self.settings.setValue("voltage-min", v * 1000))
        self.ui.voltageMaxDoubleSpin.valueChanged.connect(lambda v: self.settings.setValue("voltage-max", v * 1000))
        self.ui.currentMinDoubleSpin.valueChanged.connect(lambda i: self.settings.setValue("current-min", i * 1000))
        self.ui.currentMaxDoubleSpin.valueChanged.connect(lambda i: self.settings.setValue("current-max", i * 1000))

        # Connect voltage/current step to DoubleSpinBoxes
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

        # Load voltage/current step values for ComboBoxes
        self.ui.voltageStepCombo.setCurrentText(self.settings.value("voltage-step", "0.01"))
        self.ui.currentStepCombo.setCurrentText(self.settings.value("current-step", "0.01"))

        # Connect voltage/current step to settings
        self.ui.voltageStepCombo.currentTextChanged.connect(lambda s: self.settings.setValue("voltage-step", s))
        self.ui.currentStepCombo.currentTextChanged.connect(lambda s: self.settings.setValue("current-step", s))

        # Connect output button to riden
        self.ui.outputPush.clicked.connect(lambda: self.r.set_output(not self.r.output))

        # Connect voltage/current DoubleSpinBoxes to riden for realtime
        self.ui.voltageDoubleSpin.valueChanged.connect(lambda v: self.r.set_v_set(v) if self.ui.realtimeCheck.isChecked() else None)
        self.ui.currentDoubleSpin.valueChanged.connect(lambda i: self.r.set_i_set(i) if self.ui.realtimeCheck.isChecked() else None)

        # Connect voltage/current PushButtons to riden
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
