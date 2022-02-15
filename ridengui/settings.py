# Built-in modules
import sys
from subprocess import Popen

# Third-party modules
if "PySide2" in sys.modules:
    from PySide2.QtCore import QSettings
    from PySide2.QtGui import QColor
    from PySide2.QtWidgets import QApplication, QColorDialog, QWizard
elif "PySide6" in sys.modules:
    from PySide6.QtCore import QSettings
    from PySide6.QtGui import QColor
    from PySide6.QtWidgets import QApplication, QColorDialog, QWizard
else:
    raise ModuleNotFoundError("PySide2 or PySide6 is required to run this program.")

# Local modules
from ridengui.ui.settings import Ui_SettingsWizard


class SettingsWizard(QWizard):
    def __init__(self, settings: QSettings, parent=None):
        super().__init__(parent)
        self.settings = settings
        self.parent = parent

        # Load wizard.ui
        self.ui = Ui_SettingsWizard()
        self.ui.setupUi(self)

        # Adjust widget sizes and resize window
        self.adjustSize()
        self.resize(self.minimumSize())

        # Center window on primary screen
        self.move(QApplication.primaryScreen().geometry().center() - self.rect().center())

        # Load settings and define defaults
        self.ui.portLine.setText(self.settings.value("port", "/dev/ttyUSB0"))
        self.ui.baudrateCombo.setCurrentText(self.settings.value("baudrate", "115200"))
        self.ui.addressSpin.setValue(int(self.settings.value("address", 1)))
        self.ui.pollingSpin.setValue(int(self.settings.value("polling", 500)))
        self.ui.inputVoltagePush.setStyleSheet(self.settings.value("input-voltage-style", "color:#00ff00"))
        self.ui.outputVoltagePush.setStyleSheet(self.settings.value("output-voltage-style", "color:#ffff00"))
        self.ui.outputCurrentPush.setStyleSheet(self.settings.value("output-current-style", "color:#ffff00"))
        self.ui.outputPowerPush.setStyleSheet(self.settings.value("output-power-style", "color:#00ffff"))
        self.ui.outputOnPush.setStyleSheet(self.settings.value("output-on-style", "background-color:#00ff00;color:#000000"))
        self.ui.outputOffPush.setStyleSheet(self.settings.value("output-off-style", "background-color:#808080;color:#000000"))
        self.ui.outputFaultPush.setStyleSheet(self.settings.value("output-fault-style", "background-color:#ff0000;color:#000000"))
        self.ui.voltageSetPush.setStyleSheet(self.settings.value("voltage-set-style", "color:#ffff00"))
        self.ui.currentSetPush.setStyleSheet(self.settings.value("current-set-style", "color:#ffff00"))

        for button in (
            self.ui.inputVoltagePush,
            self.ui.outputVoltagePush,
            self.ui.outputCurrentPush,
            self.ui.outputPowerPush,
            self.ui.outputOnPush,
            self.ui.outputOffPush,
            self.ui.outputFaultPush,
            self.ui.voltageSetPush,
            self.ui.currentSetPush,
        ):
            button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        # Get current style
        style = self.sender().styleSheet()

        # Create color dialog
        color = QColorDialog.getColor(QColor(style.split("#")[1]), self)

        # Set style
        if color.isValid():
            self.sender().setStyleSheet("color:%s" % color.name())

    def accept(self):
        # Save settings
        self.settings.setValue("port", self.ui.portLine.text())
        self.settings.setValue("baudrate", self.ui.baudrateCombo.currentText())
        self.settings.setValue("address", self.ui.addressSpin.value())
        self.settings.setValue("polling", self.ui.pollingSpin.value())
        self.settings.setValue("input-voltage-style", self.ui.inputVoltagePush.styleSheet())
        self.settings.setValue("output-voltage-style", self.ui.outputVoltagePush.styleSheet())
        self.settings.setValue("output-current-style", self.ui.outputCurrentPush.styleSheet())
        self.settings.setValue("output-power-style", self.ui.outputPowerPush.styleSheet())
        self.settings.setValue("output-on-style", self.ui.outputOnPush.styleSheet())
        self.settings.setValue("output-off-style", self.ui.outputOffPush.styleSheet())
        self.settings.setValue("output-fault-style", self.ui.outputFaultPush.styleSheet())
        self.settings.setValue("voltage-set-style", self.ui.voltageSetPush.styleSheet())
        self.settings.setValue("current-set-style", self.ui.currentSetPush.styleSheet())
        self.settings.setValue("first-run", 0)
        self.settings.sync()

        # Close window
        super().accept()

        # Spawn a new instance of the application
        self.parent.close()
        Popen(sys.argv, start_new_session=True)

    def reject(self):
        # Close window
        super().reject()
