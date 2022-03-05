# Third-party modules
from qtpy.QtCore import QSettings, QThread, Signal

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
