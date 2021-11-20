from datetime import datetime
from PySide2.QtWidgets import QDialog
from riden import Riden
from ridengui.ui import Ui_Settings
from threading import Lock


class GeneralDialog(QDialog):
    def __init__(self, r: Riden, l: Lock):
        super().__init__()

        # Setup UI
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        with l:
            self.ui.language_box.setCurrentIndex(r.get_language())
            self.ui.backlight_slider.setSliderPosition(r.get_backlight())
            self.ui.confirm_box.setChecked(r.is_confirm())
            self.ui.restore_box.setChecked(r.is_restore())
            self.ui.power_box.setChecked(r.is_boot_power())
            self.ui.buzzer_box.setChecked(r.is_buzzer())
            self.ui.logo_box.setChecked(r.is_boot_logo())

        self.ui.time_button.clicked.connect(lambda: r.set_date_time(datetime.now()))

        # Setup OK button
        self.accepted.connect(lambda: save())

        def save():
            r.set_language(self.ui.language_box.currentIndex())
            r.set_backlight(self.ui.backlight_slider.value())
            r.set_confirm(self.ui.confirm_box.isChecked())
            r.set_restore(self.ui.restore_box.isChecked())
            r.set_boot_power(self.ui.power_box.isChecked())
            r.set_buzzer(self.ui.buzzer_box.isChecked())
            r.set_boot_logo(self.ui.logo_box.isChecked())


def open_general(r: Riden, l: Lock):
    settings = GeneralDialog(r, l)
    settings.setModal(True)
    settings.show()
    settings.exec_()
