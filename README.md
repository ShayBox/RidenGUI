# RidenGUI
Riden Qt GUI using Qt for Python (PySide2)

#### Install
Install my [Riden](https://github.com/ShayBox/Riden) library first
```
git clone https://github.com/ShayBox/RidenGUI.git
cd RidenGUI
python setup.py install --user
```

#### Usage
A desktop entry for `RidenGUI` and a `ridengui` command are added to your system.
After very first execution, you will have to specify serial port, apply change and restart application.
After that you could set GUI V/I limits and change steps. This is, for exampe, handy for safety if you work with low voltage electronics.
These settings are not the same as OCP and OVP on device itself, they are just limits in this RidenGUI.
All these settings are preserved between RidenGUI restarts.

#### Compatibility
Compatible with models RD6006, RD6006P, RD6012, RD6018.

#### Screenshots thumbnail. Full scale ones are in screenshots folder.
![](screebshots/thumbnails.png)