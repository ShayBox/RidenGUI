# Built-in modules
import sys

# Third-party modules
if "PySide2" in sys.modules:
    from PySide2.QtCore import QSettings, QThread, Signal
elif "PySide6" in sys.modules:
    from PySide6.QtCore import QSettings, QThread, Signal
else:
    raise ModuleNotFoundError("PySide2 or PySide6 is required to run this program.")

# Local modules
from riden import Riden


class Worker(QThread):
    update = Signal()

    def __init__(self, riden: Riden, settings: QSettings, parent=None):
        super().__init__(parent)
        self.riden = riden
        self.settings = settings
        self.sleep = int(self.settings.value("polling", 500))
        self.running = True

    def run(self):
        while self.running:
            self.riden.update()
            self.update.emit()
            self.msleep(self.sleep)
