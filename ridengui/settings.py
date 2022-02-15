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
        self.ui.portLine.setText(self.settings.value("serial/port", "/dev/ttyUSB0"))
        self.ui.baudrateCombo.setCurrentText(self.settings.value("serial/baudrate", "115200"))
        self.ui.addressSpin.setValue(int(self.settings.value("serial/address", 1)))
        self.ui.pollingSpin.setValue(int(self.settings.value("polling", 500)))
        self.ui.inputVoltagePush.setStyleSheet(self.settings.value("style/input-voltage", "color:#00ff00"))
        self.ui.outputVoltagePush.setStyleSheet(self.settings.value("style/output-voltage", "color:#ffff00"))
        self.ui.outputCurrentPush.setStyleSheet(self.settings.value("style/output-current", "color:#ffff00"))
        self.ui.outputPowerPush.setStyleSheet(self.settings.value("style/output-power", "color:#00ffff"))
        self.ui.outputOnPush.setStyleSheet(self.settings.value("style/output-on", "background-color:#00ff00;color:#000000"))
        self.ui.outputOffPush.setStyleSheet(self.settings.value("style/output-off", "background-color:#808080;color:#000000"))
        self.ui.outputFaultPush.setStyleSheet(self.settings.value("style/output-fault", "background-color:#ff0000;color:#000000"))
        self.ui.voltageSetPush.setStyleSheet(self.settings.value("style/voltage-set", "color:#ffff00"))
        self.ui.currentSetPush.setStyleSheet(self.settings.value("style/current-set", "color:#ffff00"))
        self.ui.inputVoltageLine.setText(self.settings.value("format/voltage-input", self.parent.default_voltage_input_format))
        self.ui.outputVoltageLine.setText(self.settings.value("format/voltage-output", self.parent.default_voltage_output_format))
        self.ui.outputCurrentLine.setText(self.settings.value("format/current-output", self.parent.default_current_output_format))
        self.ui.outputPowerLine.setText(self.settings.value("format/power-output", self.parent.default_power_output_format))

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
        self.settings.setValue("serial/port", self.ui.portLine.text())
        self.settings.setValue("serial/baudrate", self.ui.baudrateCombo.currentText())
        self.settings.setValue("serial/address", self.ui.addressSpin.value())
        self.settings.setValue("polling", self.ui.pollingSpin.value())
        self.settings.setValue("style/input-voltage", self.ui.inputVoltagePush.styleSheet())
        self.settings.setValue("style/output-voltage", self.ui.outputVoltagePush.styleSheet())
        self.settings.setValue("style/output-current", self.ui.outputCurrentPush.styleSheet())
        self.settings.setValue("style/output-power", self.ui.outputPowerPush.styleSheet())
        self.settings.setValue("style/output-on", self.ui.outputOnPush.styleSheet())
        self.settings.setValue("style/output-off", self.ui.outputOffPush.styleSheet())
        self.settings.setValue("style/output-fault", self.ui.outputFaultPush.styleSheet())
        self.settings.setValue("style/voltage-set", self.ui.voltageSetPush.styleSheet())
        self.settings.setValue("style/current-set", self.ui.currentSetPush.styleSheet())
        self.settings.setValue("format/voltage-input", self.ui.inputVoltageLine.text())
        self.settings.setValue("format/voltage-output", self.ui.outputVoltageLine.text())
        self.settings.setValue("format/current-output", self.ui.outputCurrentLine.text())
        self.settings.setValue("format/power-output", self.ui.outputPowerLine.text())
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
