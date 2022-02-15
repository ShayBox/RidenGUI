# Built-in modules
from os import system
from pathlib import Path

# Third-party modules
try:
    import PySide2

    uic = "pyside2-uic"
except ModuleNotFoundError:
    try:
        import PySide6

        uic = "pyside6-uic"
    except ModuleNotFoundError:
        raise ModuleNotFoundError("PySide2 or PySide6 is required to run this program.")


def gen() -> None:
    for path in Path("ridengui/ui").glob("*.ui"):
        system(f"{uic} {path} -o {path.with_suffix('.py')}")


if __name__ == "__main__":
    gen()
