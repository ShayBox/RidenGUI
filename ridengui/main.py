# Built-in modules
import faulthandler
import signal
import sys

# Third-party modules
try:
    from PySide2.QtWidgets import QApplication
except ModuleNotFoundError:
    try:
        from PySide6.QtWidgets import QApplication
    except ModuleNotFoundError:
        raise ModuleNotFoundError("PySide2 or PySide6 is required to run this program.")

# Local modules
from ridengui.mainwindow import MainWindow


def main():
    # Enable built-in python fault handler for segfaults
    faulthandler.enable()

    # Enable built-in python signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
