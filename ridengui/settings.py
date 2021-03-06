# Built-in modules
import sys
from os.path import dirname
from subprocess import Popen

# Third-party modules
from qtpy.QtCore import QSettings
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QApplication, QColorDialog, QWizard
from qtpy.uic import loadUi


class SettingsWizard(QWizard):
    def __init__(self, settings: QSettings, parent=None):
        super().__init__(parent)
        self.settings = settings
        self.parent = parent

        # Load wizard.ui
        self.ui = loadUi(dirname(__file__) + "/settings.ui", self)

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
        self.ui.inputVoltagePush.setStyleSheet(self.settings.value("style/input-voltage", self.ui.inputVoltagePush.styleSheet()))
        self.ui.outputVoltagePush.setStyleSheet(self.settings.value("style/output-voltage", self.ui.outputVoltagePush.styleSheet()))
        self.ui.outputCurrentPush.setStyleSheet(self.settings.value("style/output-current", self.ui.outputCurrentPush.styleSheet()))
        self.ui.outputPowerPush.setStyleSheet(self.settings.value("style/output-power", self.ui.outputPowerPush.styleSheet()))
        self.ui.voltageSetPush.setStyleSheet(self.settings.value("style/voltage-set", self.ui.voltageSetPush.styleSheet()))
        self.ui.currentSetPush.setStyleSheet(self.settings.value("style/current-set", self.ui.currentSetPush.styleSheet()))
        self.ui.outputOnTextPush.setStyleSheet(self.settings.value("style/output-on-text", self.ui.outputOnTextPush.styleSheet()))
        self.ui.outputOffTextPush.setStyleSheet(self.settings.value("style/output-off-text", self.ui.outputOffTextPush.styleSheet()))
        self.ui.outputFaultTextPush.setStyleSheet(self.settings.value("style/output-fault-text", self.ui.outputFaultTextPush.styleSheet()))
        self.ui.outputOnButtonPush.setStyleSheet(self.settings.value("style/output-on-bg", self.ui.outputOnButtonPush.styleSheet()))
        self.ui.outputOffButtonPush.setStyleSheet(self.settings.value("style/output-off-bg", self.ui.outputOffButtonPush.styleSheet()))
        self.ui.outputFaultButtonPush.setStyleSheet(self.settings.value("style/output-fault-bg", self.ui.outputFaultButtonPush.styleSheet()))
        self.ui.inputVoltageLine.setText(self.settings.value("format/voltage-input", self.parent.default_voltage_input_format))
        self.ui.outputVoltageLine.setText(self.settings.value("format/voltage-output", self.parent.default_voltage_output_format))
        self.ui.outputCurrentLine.setText(self.settings.value("format/current-output", self.parent.default_current_output_format))
        self.ui.outputPowerLine.setText(self.settings.value("format/power-output", self.parent.default_power_output_format))

        for button in (
            self.ui.inputVoltagePush,
            self.ui.outputVoltagePush,
            self.ui.outputCurrentPush,
            self.ui.outputPowerPush,
            self.ui.voltageSetPush,
            self.ui.currentSetPush,
            self.ui.outputOnTextPush,
            self.ui.outputOffTextPush,
            self.ui.outputFaultTextPush,
            self.ui.outputOnButtonPush,
            self.ui.outputOffButtonPush,
            self.ui.outputFaultButtonPush,
        ):
            button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        sender = self.sender()
        stylesheet: str = sender.styleSheet()
        old_color = stylesheet.split(";")[-1].split(":")[1]
        new_color = QColor(old_color.replace("#", ""))
        new_color = QColorDialog.getColor(new_color, self)
        if new_color.isValid():
            sender.setStyleSheet(stylesheet.replace(old_color, new_color.name()))

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
        self.settings.setValue("style/voltage-set", self.ui.voltageSetPush.styleSheet())
        self.settings.setValue("style/current-set", self.ui.currentSetPush.styleSheet())
        self.settings.setValue("style/output-on-text", self.ui.outputOnTextPush.styleSheet())
        self.settings.setValue("style/output-off-text", self.ui.outputOffTextPush.styleSheet())
        self.settings.setValue("style/output-fault-text", self.ui.outputFaultTextPush.styleSheet())
        self.settings.setValue("style/output-on-bg", self.ui.outputOnButtonPush.styleSheet())
        self.settings.setValue("style/output-off-bg", self.ui.outputOffButtonPush.styleSheet())
        self.settings.setValue("style/output-fault-bg", self.ui.outputFaultButtonPush.styleSheet())
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
