from PySide2.QtWidgets import QDialog, QMessageBox
from ridengui.serial_ui import Ui_Serial
from PySide2.QtCore import QSettings
from threading import Lock
from riden import Riden


class SerialDialog(QDialog):
    def __init__(self, r: Riden = None, l: Lock = None):
        super().__init__()

        # Setup UI
        self.ui = Ui_Serial()
        self.ui.setupUi(self)

        # Load settings
        settings = QSettings("Riden", "settings")
        port = str(settings.value("serial/port", "/dev/ttyUSB0"))
        baudrate = int(settings.value("serial/baudrate", 115200))
        address = int(settings.value("serial/address", 1))

        self.ui.Serial_Line.setText(port)
        self.ui.Baudrate_Box.setCurrentText(str(baudrate))
        self.ui.Address_Box.setValue(address)

        if r is None or l is None:
            self.ui.Calibrate_Button.setDisabled(True)
        else:
            self.ui.Calibrate_Button.clicked.connect(lambda: Calibrate_Button_clicked())

            def Calibrate_Button_clicked():
                with l:
                    r.set_output(False)

                    for v in (0, 61):
                        r.set_voltage_set(v)
                        voltage = r.get_voltage_set()
                        if voltage == v:
                            max_voltage = voltage
                        else:
                            break

                    for v in (0, 6.1, 18.1):
                        r.set_current_set(v)
                        current = r.get_current_set()
                        if current == v:
                            max_current = current
                        else:
                            break

                settings.setValue("serial/max_voltage", max_voltage)
                settings.setValue("serial/max_current", max_current)

                msg = QMessageBox()
                msg.setWindowTitle("Alert")
                msg.setText("Calibrated, restart to apply")
                msg.exec_()

        # Setup OK button
        self.accepted.connect(lambda: save())

        def save():
            settings.setValue("serial/port", str(self.ui.Serial_Line.text()))
            settings.setValue("serial/baudrate", int(self.ui.Baudrate_Box.currentText()))
            settings.setValue("serial/address", int(self.ui.Address_Box.value()))

            msg = QMessageBox()
            msg.setWindowTitle("Alert")
            msg.setText("Saved, restart to apply")
            msg.exec_()


def OpenSerialDialog(r: Riden = None, l: Lock = None):
    serial = SerialDialog(r, l)
    serial.show()
    serial.exec_()
