from pathlib import Path
from subprocess import run


def gen() -> None:
    for path in Path("ridengui/ui").glob("*.ui"):
        # pyside2-uic may or may not be available, depending on the system
        # run(["pyside2-uic", path, "-o", path.with_suffix(".py")])
        run(["uic", "-g", "python", path, "-o", path.with_suffix(".py")])


if __name__ == "__main__":
    gen()
