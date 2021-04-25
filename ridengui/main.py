from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from ridengui.settings import OpenSettingsDialog
from ridengui.serial import OpenSerialDialog
from ridengui.main_ui import Ui_MainWindow
from PySide2.QtCore import QSettings
from threading import Lock, Thread
from riden import Riden
from sys import exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Status_Bar.showMessage("Loading...", 1000)

        # Setup menubar actions
        self.ui.Action_Quit.triggered.connect(self.close)
        self.ui.Action_Settings.triggered.connect(lambda: OpenSettingsDialog(self.r, self.l))
        self.ui.Action_Serial.triggered.connect(lambda: OpenSerialDialog())

        # Setup SpinBoxes and Dials
        self.ui.V_Set_SpinBox.valueChanged.connect(lambda v: self.ui.V_Set_Dial.setValue(v * 100))
        self.ui.V_Set_Dial.valueChanged.connect(lambda v: self.ui.V_Set_SpinBox.setValue(v / 100))
        self.ui.I_Set_SpinBox.valueChanged.connect(lambda v: self.ui.I_Set_Dial.setValue(v * 100))
        self.ui.I_Set_Dial.valueChanged.connect(lambda v: self.ui.I_Set_SpinBox.setValue(v / 100))

        # Setup settings
        settings = QSettings("Riden", "settings")
        port = str(settings.value("serial/port", "/dev/ttyUSB0"))
        baudrate = int(settings.value("serial/baudrate", 115200))
        address = int(settings.value("serial/address", 1))

        try:
            # Setup Riden serial library
            self.r = Riden(port, baudrate, address)
            self.l = Lock()

            # Setup UI thread
            self.t = Thread(target=self.updateUI)
            self.t.status = True
            self.t.start()

            # Setup Buttons
            self.ui.V_Set_Button.clicked.connect(lambda: V_Set_Button_clicked(self))

            def V_Set_Button_clicked(self):
                with self.l:
                    self.r.set_voltage_set(self.ui.V_Set_SpinBox.value())

            self.ui.I_Set_Button.clicked.connect(lambda: I_Set_Button_clicked(self))

            def I_Set_Button_clicked(self):
                with self.l:
                    self.r.set_current_set(self.ui.I_Set_SpinBox.value())

            self.ui.OutputS_Button.clicked.connect(lambda: OutputS_Button_clicked(self))

            def OutputS_Button_clicked(self):
                with self.l:
                    is_checked = self.ui.OutputS_Button.isChecked()
                    self.ui.OutputS.setText("Enabled" if is_checked else "Disabled")
                    self.r.set_output(is_checked)
        except:
            self.ui.Status_Bar.showMessage("Failed to connect, Edit > Serial, Restart required", 0)
            OpenSerialDialog()

    def updateUI(self):
        with self.l:
            self.r.update()

        self.ui.V_Set_SpinBox.setValue(self.r.voltage_set)
        self.ui.I_Set_SpinBox.setValue(self.r.current_set)
        self.ui.OutputS.setText("Enabled" if self.r.output else "Disabled")
        self.ui.OutputS_Button.setChecked(self.r.output)
        self.ui.Keypad.setText("Locked" if self.r.keypad_lock else "Unlocked")

        while self.t.status:
            self.ui.Protection.setText(self.r.protection_string)
            self.ui.Constant.setText(self.r.constant_string)
            self.ui.InputV.setText(str(self.r.voltage_input))
            self.ui.OutputV.setText(str(self.r.voltage))
            self.ui.OutputC.setText(str(self.r.current))
            self.ui.OutputP.setText(str(self.r.power))
            c, f = self.r.int_temp_c, self.r.int_temp_f
            self.ui.Temp.setText(f"{c}°C | {f}°F")
            ah, wh = self.r.amperehour, self.r.watthour
            self.ui.Energy.setText(f"{ah}Ah | {wh}Wh")

            with self.l:
                self.r.update()

    # Stop UI thread
    def closeEvent(self, *args, **kwargs):
        super(QMainWindow, self).closeEvent(*args, **kwargs)
        if hasattr(self, 't'):
            self.t.status = False


def main():
    application = QApplication()
    window = MainWindow()
    window.show()
    exit(application.exec_())


if __name__ == "__main__":
    main()
