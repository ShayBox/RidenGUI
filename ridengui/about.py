# Built-in modules
import sys

# Third-party modules
if "PySide2" in sys.modules:
    from PySide2.QtWidgets import QDialog
elif "PySide6" in sys.modules:
    from PySide6.QtWidgets import QDialog
else:
    raise ModuleNotFoundError("PySide2 or PySide6 is required to run this program.")

# Local modules
from ridengui.ui.about import Ui_AboutDialog


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
