import os


def main() -> None:
    path = "ridengui/ui"
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file() and entry.name.endswith(".ui"):
                name = entry.name[:-3]
                os.system(f"pyside2-uic {path}/{name}.ui -o {path}/{name}.py ")


if __name__ == "__main__":
    main()
