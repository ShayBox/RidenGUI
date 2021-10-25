from logging import Formatter
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLabel
from ridengui.settings import OpenSettingsDialog
from ridengui.serial import OpenSerialDialog
from ridengui.main_ui import Ui_MainWindow
from PySide2.QtCore import QSettings
from threading import Lock, Thread
from riden import Riden
from sys import exit



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Status_Bar.showMessage("Loading...", 1000)

        # remember Toogle button text and prepare other things
        self.OrigButtonName = self.ui.OutputS_Button.text()
        self.ONStateName = "ON"
        self.ONStateStyle = "background-color: lime;font-size: 36px;"
        self.ONStateStyleCC = "background-color: red;font-size: 36px;"
        self.ONStateStyleCCText = "color:red;"

        # to keep status bar message permanent
        self.ui.StBarMessage = QLabel()
        self.ui.Status_Bar.addPermanentWidget(self.ui.StBarMessage)

        def setControllsPrecision(self):
            # precition output formats
            # display formats on real devices
            # Model     V      I       P-on<99W P-on>99W
            # RD6006P   00.000 0.0000  00.000   000.00
            # RD6006    00.00  0.000   00.00    000.0
            # RD6012    00.00  00.00   00.00    000.0
            # RD6018    00.00  00.00   00.00    000.0

            def setPerModel(self):

                def getStepsList(decimals):
                    ilist = []
                    [base] = [1]
                    for c in range(decimals + 1):
                        ilist.append(str(base))
                        base = base / 10
                    return ilist

                # formats used in main display
                self.oFCu = f'%.{self.Idecimals}f'
                self.oFVoPo = f'%.{self.Vdecimals}f' # to be like '%.4f'

                #fill IV step drop-downs by entries like 1, 0.1, 0.01, 0.001
                ilist = getStepsList(self.Idecimals)     
                self.ui.i_step_box.addItems(ilist)
                self.ui.I_Set_SpinBox.setDecimals(self.Idecimals)
                self.ui.I_Set_SpinBox.setSingleStep(float(ilist[-1]))

                vlist = getStepsList(self.Vdecimals)
                self.ui.v_step_box.addItems(vlist)
                self.ui.V_Set_SpinBox.setDecimals(self.Vdecimals)
                self.ui.V_Set_SpinBox.setSingleStep(float(vlist[-1]))

            model = self.r.type
            #model = "RD6012" # uncomment for testing
            if model == "RD6006P":
                self.Idecimals = 4
                self.Vdecimals = 3
                setPerModel(self)
                self.ui.i_max_box.setMaximum(6.1)

            elif model == "RD6006":
                self.Idecimals = 3
                self.Vdecimals = 2
                setPerModel(self)
                self.ui.i_max_box.setMaximum(6.1)

            elif model == "RD6012":
                self.Idecimals = 2
                self.Vdecimals = 2
                setPerModel(self)
                self.ui.i_max_box.setMaximum(12.1)

            elif model == "RD6018":
                self.Idecimals = 2
                self.Vdecimals = 2
                setPerModel(self)
                self.ui.i_max_box.setMaximum(18.1)



        # Setup menubar actions
        self.ui.Action_Quit.triggered.connect(self.close)
        self.ui.Action_Settings.triggered.connect(
            lambda: OpenSettingsDialog(self.r, self.l))
        self.ui.Action_Serial.triggered.connect(
            lambda: OpenSerialDialog(self.r, self.l))
        self.ui.Action_About.triggered.connect(
            lambda: showAbout())


        # Setup SpinBoxes and Dials
        self.ui.V_Set_SpinBox.valueChanged.connect(
            lambda v: self.ui.V_Set_Dial.setValue(v * self.r.voltage_multiplier))
        self.ui.V_Set_Dial.valueChanged.connect(            
            lambda v: self.ui.V_Set_SpinBox.setValue(v / self.r.voltage_multiplier))

        self.ui.I_Set_SpinBox.valueChanged.connect(
            lambda i: self.ui.I_Set_Dial.setValue(i * self.r.current_multiplier))
        self.ui.I_Set_Dial.valueChanged.connect(            
            lambda i: self.ui.I_Set_SpinBox.setValue(i / self.r.current_multiplier))

        self.ui.v_step_box.currentTextChanged.connect(
            lambda v: VStepChanged(self, v))
        self.ui.i_step_box.currentTextChanged.connect(
            lambda v: IStepChanged(self, v))

        def limitsChanged(self, value, param, obj):
            #print("LOCAL:: " + str(value) + " || Sender: " + str(param))
            self.settings.setValue(f"limit/{param}", value)
            readSettings(self)
            loadLimits(self)


        self.ui.i_max_box.valueChanged.connect(
            lambda x: limitsChanged(self, x, "max_current", "i_max_box"))
        self.ui.i_min_box.valueChanged.connect(
            lambda x: limitsChanged(self, x, "min_current", "i_min_box"))
        self.ui.v_max_box.valueChanged.connect(
            lambda x: limitsChanged(self, x, "max_voltage", "v_max_box"))
        self.ui.v_min_box.valueChanged.connect(
            lambda x: limitsChanged(self, x, "min_voltage", "v_min_box"))





        def showAbout():
            msg = QMessageBox()
            msg.setWindowTitle("About")
            msg.setText('<a href="https://github.com/ShayBox/Riden"> RidenGUI home page </a>')
            msg.exec_()

        # Read settings
        def readSettings(self):
            self.settings = QSettings("RidenGUI", "settings")
            self.port = str(self.settings.value("serial/port", "/dev/null"))
            self.baudrate = int(self.settings.value("serial/baudrate", 115200))
            self.address = int(self.settings.value("serial/address", 1))
            self.max_voltage = float(self.settings.value("limit/max_voltage", 1))
            self.max_current = float(self.settings.value("limit/max_current", 1))
            self.min_voltage = float(self.settings.value("limit/min_voltage", 0))
            self.min_current = float(self.settings.value("limit/min_current", 0))
            self.v_step = self.settings.value("step/voltage", "1")
            self.i_step = self.settings.value("step/current", "1")

        #readSettings(self)
        
        

        # Load max voltage/current
        def loadLimits(self):
            self.ui.V_Set_Dial.setMaximum(self.max_voltage * self.r.voltage_multiplier)
            self.ui.V_Set_SpinBox.setMaximum(self.max_voltage)
            self.ui.v_max_box.setValue(self.max_voltage)
            self.ui.v_max_lab.setText(str(self.max_voltage))

            self.ui.V_Set_Dial.setMinimum(self.min_voltage * self.r.voltage_multiplier)
            self.ui.V_Set_SpinBox.setMinimum(self.min_voltage)
            self.ui.v_min_box.setValue(self.min_voltage)
            self.ui.v_min_lab.setText(str(self.min_voltage))

            self.ui.I_Set_Dial.setMaximum(self.max_current * self.r.current_multiplier)
            self.ui.I_Set_SpinBox.setMaximum(self.max_current)
            self.ui.i_max_box.setValue(self.max_current)
            self.ui.i_max_lab.setText(str(self.max_current))

            self.ui.I_Set_Dial.setMinimum(self.min_current * self.r.current_multiplier)
            self.ui.I_Set_SpinBox.setMinimum(self.min_current)
            self.ui.i_min_box.setValue(self.min_current)
            self.ui.i_min_lab.setText(str(self.min_current))

        def VStepChanged(self, v):
            step = float(v)
            decimals = self.ui.v_step_box.currentIndex()
            self.ui.V_Set_SpinBox.setSingleStep(step)
            self.ui.V_Set_SpinBox.setDecimals(decimals)
            #self.ui.V_Set_Dial.setSingleStep(step)
            #self.ui.V_Set_Dial.setPageStep(step * 10)  # does not help
            self.settings.setValue("step/voltage", step)
        
        def IStepChanged(self, i):
            step = float(i)
            decimals = self.ui.i_step_box.currentIndex()
            self.ui.I_Set_SpinBox.setSingleStep(step)
            self.ui.I_Set_SpinBox.setDecimals(decimals)
            #self.ui.I_Set_Dial.setSingleStep(step)
            #self.ui.I_Set_Dial.setPageStep(step * 10) # does not help
            self.settings.setValue("step/current", step)
   

        try:
            readSettings(self)
            # Setup Riden serial library
            self.r = Riden(self.port, self.baudrate, self.address)
            loadLimits(self)
            setControllsPrecision(self)
            
            # restore custom VI steps
            # change if first entry is not with index 0
            self.ui.v_step_box.setCurrentText(self.v_step)
            self.ui.i_step_box.setCurrentText(self.i_step)
            # call again for cases when first entry is with index 0 (value "1"), to update other GUI elements
            VStepChanged(self, self.v_step)
            IStepChanged(self, self.i_step)

            # disable buttons initially, as they should indicate that values were not changed yet
            self.ui.V_Set_Button.setDisabled(True)
            self.ui.I_Set_Button.setDisabled(True)

            self.l = Lock()

            message = "Connected to %s using %s | FW: %s | SN: %s" % (self.r.type, self.port, self.r.fw, self.r.sn)
            self.ui.StBarMessage.setText(message)

            # Setup UI thread
            self.t = Thread(target=self.updateUI)
            self.t.status = True
            self.t.start()

            # Setup Buttons
            self.ui.V_Set_Button.clicked.connect(
                lambda: V_Set_Button_clicked(self))

            def V_Set_Button_clicked(self):
                with self.l:
                    self.r.set_voltage_set(self.ui.V_Set_SpinBox.value())
                    current = self.r.get_current_set()
                    if current != self.ui.I_Set_SpinBox.value():
                        self.ui.I_Set_SpinBox.setValue(current)
                    self.ui.V_Set_Button.setDisabled(True)

            self.ui.I_Set_Button.clicked.connect(
                lambda: I_Set_Button_clicked(self))

            def I_Set_Button_clicked(self):
                with self.l:
                    self.r.set_current_set(self.ui.I_Set_SpinBox.value())
                    voltage = self.r.get_voltage_set()
                    if voltage != self.ui.V_Set_SpinBox.value():
                        self.ui.V_Set_SpinBox.setValue(voltage)
                    self.ui.I_Set_Button.setDisabled(True)

            self.ui.OutputS_Button.clicked.connect(
                lambda: OutputS_Button_clicked(self))

            def OutputS_Button_clicked(self):
                with self.l:
                    is_checked = self.ui.OutputS_Button.isChecked()
                    self.ui.OutputS_Button.setText(
                        self.ONStateName if is_checked else self.OrigButtonName)
                    self.ui.OutputS_Button.setStyleSheet(
                        self.ONStateStyle if is_checked else "")
                    self.r.set_output(is_checked)
        
            self.ui.Live_Box.clicked.connect(
                lambda: Live_Box_clicked(self))

            def Live_Box_clicked(self):
                if self.ui.Live_Box.isChecked():
                    self.ui.I_Set_Button.hide()
                    self.ui.V_Set_Button.hide()
                else:
                    self.ui.I_Set_Button.show()
                    self.ui.V_Set_Button.show()


        except:
            message = "Failed to connect. Go to Settings -> Serial. Restart is required."
            self.ui.StBarMessage.setText(message)
            OpenSerialDialog()


    def updateUI(self):
        with self.l:
            self.r.update()
        
        self.ui.V_Set_SpinBox.setValue(self.r.voltage_set)
        self.ui.I_Set_SpinBox.setValue(self.r.current_set)
        self.ui.OutputS_Button.setChecked(self.r.output)

        self.ui.Keypad.setText("Locked" if self.r.keypad_lock else "Unlocked")

        while self.t.status:
            constant_string = self.r.constant_string
            
            if self.r.output:
                self.ui.OutputS_Button.setText(self.ONStateName)
                if constant_string == "CV":
                    self.ui.OutputS_Button.setStyleSheet(self.ONStateStyle)
                else:
                    self.ui.OutputS_Button.setStyleSheet(self.ONStateStyleCC)
            else:
                self.ui.OutputS_Button.setText(self.OrigButtonName)


            self.ui.Protection.setText(self.r.protection_string)
            self.ui.CCCV.setText(constant_string)
            self.ui.CCCV.setStyleSheet(
                    self.ONStateStyleCCText if constant_string == "CC" else "")
            self.ui.InputV.setText("Input: " + str(self.r.voltage_input) + " V")
            
            Vo, Cu, Po = self.r.voltage, self.r.current, self.r.power
            self.ui.OutputV.setText(self.oFVoPo % Vo)
            self.ui.OutputC.setText(self.oFCu % Cu)
            self.ui.OutputP.setText(self.oFVoPo % Po)
            
            c, f = self.r.int_temp_c, self.r.int_temp_f
            self.ui.Temp.setText("Sys temp: "f"{c}°C | {f}°F")
            ah, wh = self.r.amperehour, self.r.watthour
            self.ui.Energy.setText(f"{ah}Ah | {wh}Wh")

            # Syncronize dial/spinboxes to unit
            if self.ui.Live_Box.isChecked():
                if self.r.voltage_set != self.ui.V_Set_SpinBox.value():
                    with self.l:
                        self.r.set_voltage_set(self.ui.V_Set_SpinBox.value())
                        current = self.r.get_current_set()
                        if current != self.ui.I_Set_SpinBox.value():
                            self.ui.I_Set_SpinBox.setValue(current)
                if self.r.current_set != self.ui.I_Set_SpinBox.value():
                    with self.l:
                        self.r.set_current_set(self.ui.I_Set_SpinBox.value())
                        voltage = self.r.get_voltage_set()
                        if voltage != self.ui.V_Set_SpinBox.value():
                            self.ui.V_Set_SpinBox.setValue(voltage)

            # enable buttons it values changed
            if self.r.voltage_set != self.ui.V_Set_SpinBox.value():
                self.ui.V_Set_Button.setDisabled(False)
            if self.r.current_set != self.ui.I_Set_SpinBox.value():
                self.ui.I_Set_Button.setDisabled(False)


            with self.l:
                self.r.update()

    # Stop UI thread
    def closeEvent(self, *args, **kwargs):
        super(QMainWindow, self).closeEvent(*args, **kwargs)
        if hasattr(self, 't'):
            self.t.status = False


def main():
    application = QApplication()
    window = MainWindow()
    window.show()
    exit(application.exec_())


if __name__ == "__main__":
    main()
