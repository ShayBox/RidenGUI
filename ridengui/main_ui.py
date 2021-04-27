# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 640)
        icon = QIcon()
        iconThemeName = u"riden"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        self.Action_Quit = QAction(MainWindow)
        self.Action_Quit.setObjectName(u"Action_Quit")
        self.Action_Settings = QAction(MainWindow)
        self.Action_Settings.setObjectName(u"Action_Settings")
        self.Action_About = QAction(MainWindow)
        self.Action_About.setObjectName(u"Action_About")
        self.Action_Serial = QAction(MainWindow)
        self.Action_Serial.setObjectName(u"Action_Serial")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Info_2_Layout = QVBoxLayout()
        self.Info_2_Layout.setObjectName(u"Info_2_Layout")
        self.InputV_Label = QLabel(self.centralwidget)
        self.InputV_Label.setObjectName(u"InputV_Label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.InputV_Label.setFont(font)
        self.InputV_Label.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.InputV_Label)

        self.InputV = QLabel(self.centralwidget)
        self.InputV.setObjectName(u"InputV")
        font1 = QFont()
        font1.setPointSize(12)
        self.InputV.setFont(font1)
        self.InputV.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.InputV)

        self.OutputV_Label = QLabel(self.centralwidget)
        self.OutputV_Label.setObjectName(u"OutputV_Label")
        self.OutputV_Label.setFont(font)
        self.OutputV_Label.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.OutputV_Label)

        self.OutputV = QLabel(self.centralwidget)
        self.OutputV.setObjectName(u"OutputV")
        self.OutputV.setFont(font1)
        self.OutputV.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.OutputV)

        self.OutputC_Label = QLabel(self.centralwidget)
        self.OutputC_Label.setObjectName(u"OutputC_Label")
        self.OutputC_Label.setFont(font)
        self.OutputC_Label.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.OutputC_Label)

        self.OutputC = QLabel(self.centralwidget)
        self.OutputC.setObjectName(u"OutputC")
        self.OutputC.setFont(font1)
        self.OutputC.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.OutputC)

        self.OutputP_Label = QLabel(self.centralwidget)
        self.OutputP_Label.setObjectName(u"OutputP_Label")
        self.OutputP_Label.setFont(font)
        self.OutputP_Label.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.OutputP_Label)

        self.OutputP = QLabel(self.centralwidget)
        self.OutputP.setObjectName(u"OutputP")
        self.OutputP.setFont(font1)
        self.OutputP.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.OutputP)

        self.Temp_Label = QLabel(self.centralwidget)
        self.Temp_Label.setObjectName(u"Temp_Label")
        self.Temp_Label.setFont(font)
        self.Temp_Label.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.Temp_Label)

        self.Temp = QLabel(self.centralwidget)
        self.Temp.setObjectName(u"Temp")
        self.Temp.setFont(font1)
        self.Temp.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.Temp)

        self.Energy_Label = QLabel(self.centralwidget)
        self.Energy_Label.setObjectName(u"Energy_Label")
        self.Energy_Label.setFont(font)
        self.Energy_Label.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.Energy_Label)

        self.Energy = QLabel(self.centralwidget)
        self.Energy.setObjectName(u"Energy")
        self.Energy.setFont(font1)
        self.Energy.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.Energy)

        self.Info_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Info_2_Layout.addItem(self.Info_verticalSpacer)

        self.OutputS = QLabel(self.centralwidget)
        self.OutputS.setObjectName(u"OutputS")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.OutputS.setFont(font2)
        self.OutputS.setAlignment(Qt.AlignCenter)

        self.Info_2_Layout.addWidget(self.OutputS)

        self.OutputS_Button = QPushButton(self.centralwidget)
        self.OutputS_Button.setObjectName(u"OutputS_Button")
        self.OutputS_Button.setCheckable(True)

        self.Info_2_Layout.addWidget(self.OutputS_Button)


        self.gridLayout.addLayout(self.Info_2_Layout, 0, 2, 2, 1)

        self.V_Set_Layout = QGridLayout()
        self.V_Set_Layout.setObjectName(u"V_Set_Layout")
        self.V_Set_Button = QToolButton(self.centralwidget)
        self.V_Set_Button.setObjectName(u"V_Set_Button")

        self.V_Set_Layout.addWidget(self.V_Set_Button, 4, 1, 1, 1)

        self.V_Set_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.V_Set_SpinBox.setObjectName(u"V_Set_SpinBox")
        self.V_Set_SpinBox.setFont(font1)
        self.V_Set_SpinBox.setAlignment(Qt.AlignCenter)
        self.V_Set_SpinBox.setMaximum(100.000000000000000)
        self.V_Set_SpinBox.setSingleStep(0.100000000000000)

        self.V_Set_Layout.addWidget(self.V_Set_SpinBox, 4, 0, 1, 1)

        self.V_Set_Label = QLabel(self.centralwidget)
        self.V_Set_Label.setObjectName(u"V_Set_Label")
        self.V_Set_Label.setMaximumSize(QSize(16777215, 12))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.V_Set_Label.setFont(font3)
        self.V_Set_Label.setAlignment(Qt.AlignCenter)

        self.V_Set_Layout.addWidget(self.V_Set_Label, 2, 0, 1, 2)

        self.V_Set_Dial = QDial(self.centralwidget)
        self.V_Set_Dial.setObjectName(u"V_Set_Dial")
        self.V_Set_Dial.setMaximum(10000)
        self.V_Set_Dial.setNotchTarget(100.000000000000000)
        self.V_Set_Dial.setNotchesVisible(True)

        self.V_Set_Layout.addWidget(self.V_Set_Dial, 3, 0, 1, 2)


        self.gridLayout.addLayout(self.V_Set_Layout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 6, 0, 1, 2)

        self.Constant = QLabel(self.centralwidget)
        self.Constant.setObjectName(u"Constant")
        self.Constant.setFont(font1)
        self.Constant.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Constant, 5, 0, 1, 2)

        self.Keypad_Label = QLabel(self.centralwidget)
        self.Keypad_Label.setObjectName(u"Keypad_Label")
        self.Keypad_Label.setFont(font)
        self.Keypad_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Keypad_Label, 0, 0, 1, 2)

        self.Protection = QLabel(self.centralwidget)
        self.Protection.setObjectName(u"Protection")
        self.Protection.setFont(font1)
        self.Protection.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Protection, 3, 0, 1, 2)

        self.Keypad = QLabel(self.centralwidget)
        self.Keypad.setObjectName(u"Keypad")
        self.Keypad.setFont(font1)
        self.Keypad.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Keypad, 1, 0, 1, 2)

        self.Protection_Label = QLabel(self.centralwidget)
        self.Protection_Label.setObjectName(u"Protection_Label")
        self.Protection_Label.setFont(font)
        self.Protection_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Protection_Label, 2, 0, 1, 2)

        self.Constant_Label = QLabel(self.centralwidget)
        self.Constant_Label.setObjectName(u"Constant_Label")
        self.Constant_Label.setFont(font)
        self.Constant_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Constant_Label, 4, 0, 1, 2)

        self.Live_Box = QCheckBox(self.centralwidget)
        self.Live_Box.setObjectName(u"Live_Box")

        self.gridLayout_2.addWidget(self.Live_Box, 7, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 2, 1)

        self.I_Set_Layout = QGridLayout()
        self.I_Set_Layout.setObjectName(u"I_Set_Layout")
        self.I_Set_Button = QToolButton(self.centralwidget)
        self.I_Set_Button.setObjectName(u"I_Set_Button")

        self.I_Set_Layout.addWidget(self.I_Set_Button, 3, 1, 1, 1)

        self.I_Set_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.I_Set_SpinBox.setObjectName(u"I_Set_SpinBox")
        self.I_Set_SpinBox.setFont(font1)
        self.I_Set_SpinBox.setAlignment(Qt.AlignCenter)
        self.I_Set_SpinBox.setMaximum(100.000000000000000)
        self.I_Set_SpinBox.setSingleStep(0.100000000000000)

        self.I_Set_Layout.addWidget(self.I_Set_SpinBox, 3, 0, 1, 1)

        self.I_Set_Dial = QDial(self.centralwidget)
        self.I_Set_Dial.setObjectName(u"I_Set_Dial")
        self.I_Set_Dial.setMaximum(10000)
        self.I_Set_Dial.setNotchTarget(100.000000000000000)
        self.I_Set_Dial.setNotchesVisible(True)

        self.I_Set_Layout.addWidget(self.I_Set_Dial, 1, 0, 1, 2)

        self.I_Set_Label = QLabel(self.centralwidget)
        self.I_Set_Label.setObjectName(u"I_Set_Label")
        self.I_Set_Label.setMaximumSize(QSize(16777215, 12))
        self.I_Set_Label.setFont(font3)
        self.I_Set_Label.setAlignment(Qt.AlignCenter)

        self.I_Set_Layout.addWidget(self.I_Set_Label, 0, 0, 1, 2)


        self.gridLayout.addLayout(self.I_Set_Layout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.Menu_Bar = QMenuBar(MainWindow)
        self.Menu_Bar.setObjectName(u"Menu_Bar")
        self.Menu_Bar.setGeometry(QRect(0, 0, 680, 30))
        self.Menu_File = QMenu(self.Menu_Bar)
        self.Menu_File.setObjectName(u"Menu_File")
        self.Menu_About = QMenu(self.Menu_Bar)
        self.Menu_About.setObjectName(u"Menu_About")
        self.Menu_Help = QMenu(self.Menu_Bar)
        self.Menu_Help.setObjectName(u"Menu_Help")
        MainWindow.setMenuBar(self.Menu_Bar)
        self.Status_Bar = QStatusBar(MainWindow)
        self.Status_Bar.setObjectName(u"Status_Bar")
        MainWindow.setStatusBar(self.Status_Bar)
#if QT_CONFIG(shortcut)
        self.OutputS.setBuddy(self.OutputS_Button)
        self.V_Set_Label.setBuddy(self.V_Set_Dial)
        self.I_Set_Label.setBuddy(self.I_Set_Dial)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.V_Set_Dial, self.V_Set_SpinBox)
        QWidget.setTabOrder(self.V_Set_SpinBox, self.V_Set_Button)
        QWidget.setTabOrder(self.V_Set_Button, self.I_Set_Dial)
        QWidget.setTabOrder(self.I_Set_Dial, self.I_Set_SpinBox)
        QWidget.setTabOrder(self.I_Set_SpinBox, self.I_Set_Button)
        QWidget.setTabOrder(self.I_Set_Button, self.OutputS_Button)

        self.Menu_Bar.addAction(self.Menu_File.menuAction())
        self.Menu_Bar.addAction(self.Menu_About.menuAction())
        self.Menu_Bar.addAction(self.Menu_Help.menuAction())
        self.Menu_File.addAction(self.Action_Quit)
        self.Menu_About.addAction(self.Action_Settings)
        self.Menu_About.addAction(self.Action_Serial)
        self.Menu_Help.addAction(self.Action_About)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RidenGUI", None))
        self.Action_Quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.Action_Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Action_About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Action_Serial.setText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.InputV_Label.setText(QCoreApplication.translate("MainWindow", u"Input Voltage (V)", None))
        self.InputV.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.OutputV_Label.setText(QCoreApplication.translate("MainWindow", u"Output Voltage (V)", None))
        self.OutputV.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.OutputC_Label.setText(QCoreApplication.translate("MainWindow", u"Output Current (A)", None))
        self.OutputC.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.OutputP_Label.setText(QCoreApplication.translate("MainWindow", u"Output Power (W)", None))
        self.OutputP.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.Temp_Label.setText(QCoreApplication.translate("MainWindow", u"System Tempature", None))
        self.Temp.setText(QCoreApplication.translate("MainWindow", u"00.00\u00b0C | 00.00\u00b0F", None))
        self.Energy_Label.setText(QCoreApplication.translate("MainWindow", u"Energy Usage", None))
        self.Energy.setText(QCoreApplication.translate("MainWindow", u"00.00 Ah | 00.00 Wh", None))
        self.OutputS.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.OutputS_Button.setText(QCoreApplication.translate("MainWindow", u"Toggle Output", None))
        self.V_Set_Button.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.V_Set_Label.setText(QCoreApplication.translate("MainWindow", u"V-Set", None))
        self.Constant.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.Keypad_Label.setText(QCoreApplication.translate("MainWindow", u"Keypad Lock", None))
        self.Protection.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.Keypad.setText(QCoreApplication.translate("MainWindow", u"Unlocked", None))
        self.Protection_Label.setText(QCoreApplication.translate("MainWindow", u"Protection Status", None))
        self.Constant_Label.setText(QCoreApplication.translate("MainWindow", u"Constant Status", None))
        self.Live_Box.setText(QCoreApplication.translate("MainWindow", u"Syncronize V/I Set", None))
        self.I_Set_Button.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.I_Set_Label.setText(QCoreApplication.translate("MainWindow", u"I-Set", None))
        self.Menu_File.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.Menu_About.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.Menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

