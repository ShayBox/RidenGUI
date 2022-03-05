# Built-in modules
from os.path import dirname

# Third-party modules
from qtpy.QtWidgets import QDialog
from qtpy.uic import loadUi


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = loadUi(dirname(__file__) + "/about.ui", self)
