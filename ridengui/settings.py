from ridengui.settings_ui import Ui_Settings
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import QSettings
from datetime import datetime
from threading import Lock
from riden import Riden


class SettingsWindow(QDialog):
    def __init__(self, r: Riden, l: Lock):
        super().__init__()

        # Setup UI
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        # Load settings
        settings = QSettings("Riden", "settings")

        with l:
            self.ui.SerialPort.setText(settings.value("serial/port", "/dev/ttyUSB0"))
            self.ui.Language_ComboBox.setCurrentIndex(r.get_language())
            self.ui.Backlight_Slider.setSliderPosition(r.get_backlight())
            self.ui.Confirm_Box.setChecked(r.is_confirm())
            self.ui.Restore_Box.setChecked(r.is_restore())
            self.ui.Power_Box.setChecked(r.is_boot_power())
            self.ui.Buzzer_Box.setChecked(r.is_buzzer())
            self.ui.Logo_Box.setChecked(r.is_boot_logo())

        self.ui.Time_Button.clicked.connect(lambda: r.set_date_time(datetime.now()))

        # Setup OK button
        self.accepted.connect(lambda: save())

        def save():
            settings.setValue("serial/port", self.ui.SerialPort.text())
            r.set_language(self.ui.Language_ComboBox.currentIndex())
            r.set_backlight(self.ui.Backlight_Slider.value())
            r.set_confirm(self.ui.Confirm_Box.isChecked())
            r.set_restore(self.ui.Restore_Box.isChecked())
            r.set_boot_power(self.ui.Power_Box.isChecked())
            r.set_buzzer(self.ui.Buzzer_Box.isChecked())
            r.set_boot_logo(self.ui.Logo_Box.isChecked())


def OpenSettings(r: Riden, l: Lock):
    settings = SettingsWindow(r, l)
    settings.show()
    settings.exec_()
