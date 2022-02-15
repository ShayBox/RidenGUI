# Built-in modules
import faulthandler
import logging
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
import click

# Local modules
from ridengui.mainwindow import MainWindow


@click.command()
@click.option("-p", "--port", default=None, help="Serial port")
@click.option("-b", "--baudrate", default=None, help="Serial baudrate")
@click.option("-a", "--address", default=None, help="Modbus address")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose mode")
def main(port: str, baudrate: int, address: int, verbose: bool):
    logging.basicConfig(level=logging.DEBUG if verbose else logging.WARNING)

    logging.debug("Enabled built-in python fault handler for segfaults")
    faulthandler.enable()

    logging.debug("Enabled built-in python signal handler for Ctrl+C")
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    logging.debug("Starting QApplication and MainWindow")
    app = QApplication(sys.argv)
    window = MainWindow(port, baudrate, address)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
