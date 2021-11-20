from PySide2.QtCore import QSettings
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from riden import Riden
from ridengui.serial import open_serial
from ridengui.settings import open_general
from ridengui.ui import Ui_MainWindow
from threading import Lock, Thread
import signal
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage("Loading...", 1000)

        # Remember Toogle button text and prepare other things
        self.on_state_name = "ON"
        self.on_state_style = "background-color: lime;font-size: 36px;"
        self.off_state_name = "OFF"
        self.off_state_style = "background-color: gray;font-size: 36px;"
        self.style_cc = "background-color: red;font-size: 36px;"
        self.style_cc_text = "color:red;"

        # To keep status bar message permanent
        self.ui.statusbar_message = QLabel()
        self.ui.statusbar.addPermanentWidget(self.ui.statusbar_message)

        def set_controlls_precision(self):
            # Precition output formats
            # Display formats on real devices
            # Model     V      I       P-on<99W P-on>99W
            # RD6006P   00.000 0.0000  00.000   000.00
            # RD6006    00.00  0.000   00.00    000.0
            # RD6012    00.00  00.00   00.00    000.0
            # RD6018    00.00  00.00   00.00    000.0

            def set_per_model(self):
                def get_steps_list(decimals):
                    ilist = []
                    [base] = [1]
                    for c in range(decimals + 1):
                        ilist.append(str(base))
                        base = base / 10
                    return ilist

                # Formats used in main display
                self.oFCu = f"%.{self.Idecimals}f"
                self.oFVoPo = f"%.{self.Vdecimals}f"  # to be like '%.4f'

                # Fill IV step drop-downs by entries like 1, 0.1, 0.01, 0.001
                ilist = get_steps_list(self.Idecimals)
                self.ui.i_step_box.addItems(ilist)
                self.ui.i_set_spinbox.setDecimals(self.Idecimals)
                self.ui.i_set_spinbox.setSingleStep(float(ilist[-1]))

                vlist = get_steps_list(self.Vdecimals)
                self.ui.v_step_box.addItems(vlist)
                self.ui.v_set_spinbox.setDecimals(self.Vdecimals)
                self.ui.v_set_spinbox.setSingleStep(float(vlist[-1]))

            model = self.r.type
            # model = "RD6012" # uncomment for testing
            if model == "RD6006P":
                self.Idecimals = 4
                self.Vdecimals = 3
                set_per_model(self)
                self.ui.i_max_box.setMaximum(6.1)

            elif model == "RD6006":
                self.Idecimals = 3
                self.Vdecimals = 2
                set_per_model(self)
                self.ui.i_max_box.setMaximum(6.1)

            elif model == "RD6012":
                self.Idecimals = 2
                self.Vdecimals = 2
                set_per_model(self)
                self.ui.i_max_box.setMaximum(12.1)

            elif model == "RD6018":
                self.Idecimals = 2
                self.Vdecimals = 2
                set_per_model(self)
                self.ui.i_max_box.setMaximum(18.1)

        # Setup menubar actions
        self.ui.action_quit.triggered.connect(self.close)
        self.ui.action_general.triggered.connect(lambda: open_general(self.r, self.l))
        self.ui.action_serial.triggered.connect(lambda: open_serial(self.r, self.l))
        self.ui.action_about.triggered.connect(lambda: show_about())

        # Setup SpinBoxes and Dials
        self.ui.v_set_spinbox.valueChanged.connect(
            lambda v: self.ui.v_set_dial.setValue(v * self.r.voltage_multiplier)
        )
        self.ui.v_set_dial.valueChanged.connect(
            lambda v: self.ui.v_set_spinbox.setValue(v / self.r.voltage_multiplier)
        )

        self.ui.i_set_spinbox.valueChanged.connect(
            lambda i: self.ui.i_set_dial.setValue(i * self.r.current_multiplier)
        )
        self.ui.i_set_dial.valueChanged.connect(
            lambda i: self.ui.i_set_spinbox.setValue(i / self.r.current_multiplier)
        )

        self.ui.v_step_box.currentTextChanged.connect(lambda v: v_step_changed(self, v))
        self.ui.i_step_box.currentTextChanged.connect(lambda v: i_step_changed(self, v))

        def limits_changed(self, value, param, obj):
            # print("LOCAL:: " + str(value) + " || Sender: " + str(param))
            self.settings.setValue(f"limit/{param}", value)
            read_settings(self)
            load_limits(self)

        self.ui.i_max_box.valueChanged.connect(
            lambda x: limits_changed(self, x, "max_current", "i_max_box")
        )
        self.ui.i_min_box.valueChanged.connect(
            lambda x: limits_changed(self, x, "min_current", "i_min_box")
        )
        self.ui.v_max_box.valueChanged.connect(
            lambda x: limits_changed(self, x, "max_voltage", "v_max_box")
        )
        self.ui.v_min_box.valueChanged.connect(
            lambda x: limits_changed(self, x, "min_voltage", "v_min_box")
        )

        def show_about():
            msg = QMessageBox()
            msg.setWindowTitle("About")
            msg.setText(
                '<a href="https://github.com/ShayBox/RidenGUI"> RidenGUI home page </a>'
            )
            msg.exec_()

        # Read settings
        def read_settings(self):
            self.settings = QSettings("RidenGUI", "settings")
            self.port = str(self.settings.value("serial/port", "/dev/null"))
            self.baudrate = int(self.settings.value("serial/baudrate", 115200))
            self.address = int(self.settings.value("serial/address", 1))
            self.max_voltage = float(self.settings.value("limit/max_voltage", 1))
            self.max_current = float(self.settings.value("limit/max_current", 1))
            self.min_voltage = float(self.settings.value("limit/min_voltage", 0))
            self.min_current = float(self.settings.value("limit/min_current", 0))
            self.v_step = self.settings.value("step/voltage", "1")
            self.i_step = self.settings.value("step/current", "1")

        # Load max voltage/current
        def load_limits(self):
            self.ui.v_set_dial.setMaximum(self.max_voltage * self.r.voltage_multiplier)
            self.ui.v_set_spinbox.setMaximum(self.max_voltage)
            self.ui.v_max_box.setValue(self.max_voltage)
            self.ui.v_max_lab.setText(str(self.max_voltage))

            self.ui.v_set_dial.setMinimum(self.min_voltage * self.r.voltage_multiplier)
            self.ui.v_set_spinbox.setMinimum(self.min_voltage)
            self.ui.v_min_box.setValue(self.min_voltage)
            self.ui.v_min_lab.setText(str(self.min_voltage))

            self.ui.i_set_dial.setMaximum(self.max_current * self.r.current_multiplier)
            self.ui.i_set_spinbox.setMaximum(self.max_current)
            self.ui.i_max_box.setValue(self.max_current)
            self.ui.i_max_lab.setText(str(self.max_current))

            self.ui.i_set_dial.setMinimum(self.min_current * self.r.current_multiplier)
            self.ui.i_set_spinbox.setMinimum(self.min_current)
            self.ui.i_min_box.setValue(self.min_current)
            self.ui.i_min_lab.setText(str(self.min_current))

        def v_step_changed(self, v):
            step = float(v)
            decimals = self.ui.v_step_box.currentIndex()
            self.ui.v_set_spinbox.setSingleStep(step)
            self.ui.v_set_spinbox.setDecimals(decimals)
            # self.ui.v_set_dial.setSingleStep(step)
            # self.ui.v_set_dial.setPageStep(step * 10)  # does not help
            self.settings.setValue("step/voltage", step)

        def i_step_changed(self, i):
            step = float(i)
            decimals = self.ui.i_step_box.currentIndex()
            self.ui.i_set_spinbox.setSingleStep(step)
            self.ui.i_set_spinbox.setDecimals(decimals)
            # self.ui.i_set_dial.setSingleStep(step)
            # self.ui.i_set_dial.setPageStep(step * 10) # does not help
            self.settings.setValue("step/current", step)

        try:
            read_settings(self)
            # Setup Riden serial library
            self.r = Riden(self.port, self.baudrate, self.address)
            load_limits(self)
            set_controlls_precision(self)

            # Restore custom VI steps
            # Change if first entry is not with index 0
            self.ui.v_step_box.setCurrentText(self.v_step)
            self.ui.i_step_box.setCurrentText(self.i_step)
            # Call again for cases when first entry is with index 0 (value "1"), to update other GUI elements
            v_step_changed(self, self.v_step)
            i_step_changed(self, self.i_step)

            # Disable buttons initially, as they should indicate that values were not changed yet
            self.ui.v_set_button.setDisabled(True)
            self.ui.i_set_button.setDisabled(True)

            self.l = Lock()

            message = "Connected to %s using %s | FW: %s | SN: %s" % (
                self.r.type,
                self.port,
                self.r.fw,
                self.r.sn,
            )
            self.ui.statusbar_message.setText(message)

            # Setup UI thread
            self.t = Thread(target=self.update_ui)
            self.t.status = True
            self.t.start()

            # Setup Buttons
            self.ui.v_set_button.clicked.connect(lambda: v_set_button_clicked(self))

            def v_set_button_clicked(self):
                with self.l:
                    self.r.set_voltage_set(self.ui.v_set_spinbox.value())
                    current = self.r.get_current_set()
                    if current != self.ui.i_set_spinbox.value():
                        self.ui.i_set_spinbox.setValue(current)
                    self.ui.v_set_button.setDisabled(True)

            self.ui.i_set_button.clicked.connect(lambda: i_set_button_clicked(self))

            def i_set_button_clicked(self):
                with self.l:
                    self.r.set_current_set(self.ui.i_set_spinbox.value())
                    voltage = self.r.get_voltage_set()
                    if voltage != self.ui.v_set_spinbox.value():
                        self.ui.v_set_spinbox.setValue(voltage)
                    self.ui.i_set_button.setDisabled(True)

            self.ui.output_button.clicked.connect(lambda: output_button_clicked(self))

            def output_button_clicked(self):
                with self.l:
                    is_checked = self.ui.output_button.isChecked()
                    self.ui.output_button.setText(
                        self.on_state_name if is_checked else self.off_state_name
                    )
                    self.ui.output_button.setStyleSheet(
                        self.on_state_style if is_checked else self.off_state_style
                    )
                    self.r.set_output(is_checked)

            self.ui.realtime_box.clicked.connect(lambda: realtime_box_clicked(self))

            def realtime_box_clicked(self):
                if self.ui.realtime_box.isChecked():
                    self.ui.i_set_button.hide()
                    self.ui.v_set_button.hide()
                else:
                    self.ui.i_set_button.show()
                    self.ui.v_set_button.show()

        except:
            message = (
                "Failed to connect. Go to Settings -> Serial. Restart is required."
            )
            self.ui.statusbar_message.setText(message)
            open_serial()

    def update_ui(self):
        with self.l:
            self.r.update()

        self.ui.v_set_spinbox.setValue(self.r.voltage_set)
        self.ui.i_set_spinbox.setValue(self.r.current_set)
        self.ui.output_button.setChecked(self.r.output)

        self.ui.keypad.setText("Locked" if self.r.keypad_lock else "Unlocked")

        while self.t.status:
            constant_string = self.r.constant_string

            if self.r.output:
                self.ui.output_button.setText(self.on_state_name)
                if constant_string == "CV":
                    self.ui.output_button.setStyleSheet(self.on_state_style)
                else:
                    self.ui.output_button.setStyleSheet(self.style_cc)
            else:
                self.ui.output_button.setText(self.off_state_name)

            self.ui.protection.setText(self.r.protection_string)
            self.ui.constant.setText(constant_string)
            self.ui.constant.setStyleSheet(
                self.style_cc_text if constant_string == "CC" else ""
            )
            self.ui.input_voltage.setText("Input: " + str(self.r.voltage_input) + " V")

            Vo, Cu, Po = self.r.voltage, self.r.current, self.r.power
            self.ui.output_voltage.setText(self.oFVoPo % Vo)
            self.ui.output_current.setText(self.oFCu % Cu)
            self.ui.output_power.setText(self.oFVoPo % Po)

            c, f = self.r.int_temp_c, self.r.int_temp_f
            self.ui.temp.setText("Sys temp: " f"{c}°C | {f}°F")
            ah, wh = self.r.amperehour, self.r.watthour
            self.ui.energy.setText(f"{ah}Ah | {wh}Wh")

            # Syncronize dial/spinboxes to unit
            if self.ui.realtime_box.isChecked():
                if self.r.voltage_set != self.ui.v_set_spinbox.value():
                    with self.l:
                        self.r.set_voltage_set(self.ui.v_set_spinbox.value())
                        current = self.r.get_current_set()
                        if current != self.ui.i_set_spinbox.value():
                            self.ui.i_set_spinbox.setValue(current)
                if self.r.current_set != self.ui.i_set_spinbox.value():
                    with self.l:
                        self.r.set_current_set(self.ui.i_set_spinbox.value())
                        voltage = self.r.get_voltage_set()
                        if voltage != self.ui.v_set_spinbox.value():
                            self.ui.v_set_spinbox.setValue(voltage)

            # Enable buttons it values changed
            if self.r.voltage_set != self.ui.v_set_spinbox.value():
                self.ui.v_set_button.setDisabled(False)
            if self.r.current_set != self.ui.i_set_spinbox.value():
                self.ui.i_set_button.setDisabled(False)

            with self.l:
                self.r.update()

    # Native Qt event
    def closeEvent(self, *args, **kwargs):
        super(QMainWindow, self).closeEvent(*args, **kwargs)
        if hasattr(self, "t"):
            self.t.status = False


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
