from PySide2.QtCore import QSettings
from PySide2.QtWidgets import QDialog, QMessageBox
from riden import Riden
from ridengui.ui import Ui_Serial
from threading import Lock


class SerialDialog(QDialog):
    def __init__(self, r: Riden = None, l: Lock = None):
        super().__init__()

        # Setup UI
        self.ui = Ui_Serial()
        self.ui.setupUi(self)

        # Load settings
        settings = QSettings("RidenGUI", "settings")
        port = str(settings.value("serial/port", "/dev/ttyUSB0"))
        baudrate = int(settings.value("serial/baudrate", 115200))
        address = int(settings.value("serial/address", 1))

        self.ui.Serial_Line.setText(port)
        self.ui.Baudrate_Box.setCurrentText(str(baudrate))
        self.ui.Address_Box.setValue(address)

        # Setup OK button
        self.accepted.connect(lambda: save())

        def save():
            settings.setValue("serial/port", str(self.ui.Serial_Line.text()))
            settings.setValue(
                "serial/baudrate", int(self.ui.Baudrate_Box.currentText())
            )
            settings.setValue("serial/address", int(self.ui.Address_Box.value()))

            msg = QMessageBox()
            msg.setWindowTitle("Alert")
            msg.setText("Saved, restart to apply")
            msg.exec_()


def OpenSerialDialog(r: Riden = None, l: Lock = None):
    serial = SerialDialog(r, l)
    serial.setModal(True)
    serial.show()
    serial.exec_()
