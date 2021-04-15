from setuptools import setup, find_packages

setup(
    name="ridengui",
    version="0.1.0",
    description="Riden Qt GUI using PyQt",
    url="https://github.com/ShayBox/RidenGUI.git",
    license="MIT",
    author="Shayne Hartford",
    packages=find_packages(),
    install_requires=["riden"],
    entry_points={
        "console_scripts": ["ridengui=ridengui.main:main"],
    },
    data_files=[
        ('share/applications', ['data/riden.desktop']),
        ('share/icons/hicolor/32x32/apps', ['data/riden.png']),
    ],
)
