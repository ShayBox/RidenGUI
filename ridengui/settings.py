# Built-in modules
from datetime import datetime
from threading import Lock

# Third-party modules
from PySide2.QtWidgets import QDialog
from riden import Riden

# Local modules
from ridengui.ui import Ui_Settings


class GeneralDialog(QDialog):
    def __init__(self, r: Riden, l: Lock):
        super().__init__()

        # Setup UI
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        with l:
            self.ui.language_box.setCurrentIndex(r.get_lang())
            self.ui.backlight_slider.setSliderPosition(r.get_light())
            self.ui.confirm_box.setChecked(r.is_take_ok())
            self.ui.restore_box.setChecked(r.is_take_out())
            self.ui.power_box.setChecked(r.is_boot_pow())
            self.ui.buzzer_box.setChecked(r.is_buzz())
            self.ui.logo_box.setChecked(r.is_logo())

        self.ui.time_button.clicked.connect(lambda: r.set_date_time(datetime.now()))

        # Setup OK button
        self.accepted.connect(lambda: save())

        def save():
            r.set_lang(self.ui.language_box.currentIndex())
            r.set_light(self.ui.backlight_slider.value())
            r.set_take_ok(self.ui.confirm_box.isChecked())
            r.set_take_out(self.ui.restore_box.isChecked())
            r.set_boot_pow(self.ui.power_box.isChecked())
            r.set_buzz(self.ui.buzzer_box.isChecked())
            r.set_logo(self.ui.logo_box.isChecked())


def open_general(r: Riden, l: Lock):
    settings = GeneralDialog(r, l)
    settings.setModal(True)
    settings.show()
    settings.exec_()
