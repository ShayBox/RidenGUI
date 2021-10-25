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
        MainWindow.resize(765, 523)
        icon = QIcon()
        iconThemeName = u"riden"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../../../../opt/Batt-tools/RidenGUI/ridengui", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        self.Action_Quit = QAction(MainWindow)
        self.Action_Quit.setObjectName(u"Action_Quit")
        self.Action_Settings = QAction(MainWindow)
        self.Action_Settings.setObjectName(u"Action_Settings")
        self.Action_About = QAction(MainWindow)
        self.Action_About.setObjectName(u"Action_About")
        self.Action_Serial = QAction(MainWindow)
        self.Action_Serial.setObjectName(u"Action_Serial")
        self.Action_Set_VI_ranges = QAction(MainWindow)
        self.Action_Set_VI_ranges.setObjectName(u"Action_Set_VI_ranges")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 0, 1, 1, 1)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(0, 12))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 3, 0, 1, 3)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 12))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 3)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 4, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.Main_Display = QGridLayout()
        self.Main_Display.setSpacing(3)
        self.Main_Display.setObjectName(u"Main_Display")
        self.Main_Display.setContentsMargins(3, 3, 3, 3)
        self.OutputC = QLabel(self.centralwidget)
        self.OutputC.setObjectName(u"OutputC")
        font = QFont()
        font.setFamily(u"DejaVu Sans Mono")
        font.setPointSize(36)
        self.OutputC.setFont(font)
        self.OutputC.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.OutputC.setScaledContents(False)
        self.OutputC.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.Main_Display.addWidget(self.OutputC, 2, 0, 1, 1)

        self.OutputV = QLabel(self.centralwidget)
        self.OutputV.setObjectName(u"OutputV")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OutputV.sizePolicy().hasHeightForWidth())
        self.OutputV.setSizePolicy(sizePolicy)
        self.OutputV.setFont(font)
        self.OutputV.setAutoFillBackground(False)
        self.OutputV.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.OutputV.setScaledContents(False)
        self.OutputV.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.Main_Display.addWidget(self.OutputV, 0, 0, 1, 1)

        self.OutputV_Label = QLabel(self.centralwidget)
        self.OutputV_Label.setObjectName(u"OutputV_Label")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.OutputV_Label.setFont(font1)
        self.OutputV_Label.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.OutputV_Label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.OutputV_Label.setMargin(5)

        self.Main_Display.addWidget(self.OutputV_Label, 0, 1, 1, 1)

        self.OutputC_Label = QLabel(self.centralwidget)
        self.OutputC_Label.setObjectName(u"OutputC_Label")
        self.OutputC_Label.setFont(font1)
        self.OutputC_Label.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.OutputC_Label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.OutputC_Label.setMargin(5)

        self.Main_Display.addWidget(self.OutputC_Label, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Main_Display.addItem(self.verticalSpacer_2, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Main_Display.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.OutputP = QLabel(self.centralwidget)
        self.OutputP.setObjectName(u"OutputP")
        self.OutputP.setFont(font)
        self.OutputP.setStyleSheet(u"color: rgb(255, 0, 255);")
        self.OutputP.setScaledContents(False)
        self.OutputP.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.Main_Display.addWidget(self.OutputP, 4, 0, 2, 1)

        self.OutputP_Label = QLabel(self.centralwidget)
        self.OutputP_Label.setObjectName(u"OutputP_Label")
        self.OutputP_Label.setFont(font1)
        self.OutputP_Label.setStyleSheet(u"color: rgb(255, 0, 255);")
        self.OutputP_Label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.OutputP_Label.setMargin(5)
        self.OutputP_Label.setIndent(-1)

        self.Main_Display.addWidget(self.OutputP_Label, 4, 1, 2, 1)


        self.verticalLayout_3.addLayout(self.Main_Display)

        self.OutputS_Button = QPushButton(self.centralwidget)
        self.OutputS_Button.setObjectName(u"OutputS_Button")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.OutputS_Button.sizePolicy().hasHeightForWidth())
        self.OutputS_Button.setSizePolicy(sizePolicy1)
        self.OutputS_Button.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setPointSize(12)
        self.OutputS_Button.setFont(font2)
        self.OutputS_Button.setCheckable(True)

        self.verticalLayout_3.addWidget(self.OutputS_Button)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 4, 7, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.Live_Box = QCheckBox(self.centralwidget)
        self.Live_Box.setObjectName(u"Live_Box")
        self.Live_Box.setEnabled(True)
        self.Live_Box.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_2.addWidget(self.Live_Box, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 3)

        self.State_Textual = QGridLayout()
        self.State_Textual.setObjectName(u"State_Textual")
        self.Protection = QLabel(self.centralwidget)
        self.Protection.setObjectName(u"Protection")
        self.Protection.setFont(font2)
        self.Protection.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.State_Textual.addWidget(self.Protection, 1, 1, 1, 1)

        self.Keypad = QLabel(self.centralwidget)
        self.Keypad.setObjectName(u"Keypad")
        self.Keypad.setFont(font2)
        self.Keypad.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.State_Textual.addWidget(self.Keypad, 0, 1, 1, 1)

        self.Keypad_Label = QLabel(self.centralwidget)
        self.Keypad_Label.setObjectName(u"Keypad_Label")
        font3 = QFont()
        font3.setBold(False)
        font3.setWeight(50)
        self.Keypad_Label.setFont(font3)
        self.Keypad_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.State_Textual.addWidget(self.Keypad_Label, 0, 0, 1, 1)

        self.Constant_Label = QLabel(self.centralwidget)
        self.Constant_Label.setObjectName(u"Constant_Label")
        self.Constant_Label.setFont(font3)
        self.Constant_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.State_Textual.addWidget(self.Constant_Label, 2, 0, 1, 1)

        self.CCCV = QLabel(self.centralwidget)
        self.CCCV.setObjectName(u"CCCV")
        self.CCCV.setFont(font2)
        self.CCCV.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.State_Textual.addWidget(self.CCCV, 2, 1, 1, 1)

        self.Protection_Label = QLabel(self.centralwidget)
        self.Protection_Label.setObjectName(u"Protection_Label")
        self.Protection_Label.setFont(font3)
        self.Protection_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.State_Textual.addWidget(self.Protection_Label, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.State_Textual, 0, 0, 1, 1)

        self.State_Numeric = QGridLayout()
        self.State_Numeric.setObjectName(u"State_Numeric")
        self.State_Numeric.setContentsMargins(-1, -1, 17, -1)
        self.InputV = QLabel(self.centralwidget)
        self.InputV.setObjectName(u"InputV")
        self.InputV.setFont(font2)
        self.InputV.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.State_Numeric.addWidget(self.InputV, 2, 0, 1, 1)

        self.Temp = QLabel(self.centralwidget)
        self.Temp.setObjectName(u"Temp")
        self.Temp.setFont(font2)
        self.Temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.State_Numeric.addWidget(self.Temp, 1, 0, 1, 1)

        self.Energy = QLabel(self.centralwidget)
        self.Energy.setObjectName(u"Energy")
        self.Energy.setFont(font2)
        self.Energy.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.State_Numeric.addWidget(self.Energy, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.State_Numeric, 0, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.V_Set_Label = QLabel(self.centralwidget)
        self.V_Set_Label.setObjectName(u"V_Set_Label")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.V_Set_Label.setFont(font4)
        self.V_Set_Label.setAlignment(Qt.AlignCenter)
        self.V_Set_Label.setIndent(-1)

        self.verticalLayout.addWidget(self.V_Set_Label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.v_step_box = QComboBox(self.centralwidget)
        self.v_step_box.setObjectName(u"v_step_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.v_step_box.sizePolicy().hasHeightForWidth())
        self.v_step_box.setSizePolicy(sizePolicy2)
        self.v_step_box.setEditable(False)

        self.gridLayout.addWidget(self.v_step_box, 1, 1, 1, 1)

        self.v_min_lab_2 = QLabel(self.centralwidget)
        self.v_min_lab_2.setObjectName(u"v_min_lab_2")
        self.v_min_lab_2.setFont(font3)
        self.v_min_lab_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.v_min_lab_2, 0, 0, 1, 1)

        self.v_max_lab_3 = QLabel(self.centralwidget)
        self.v_max_lab_3.setObjectName(u"v_max_lab_3")
        self.v_max_lab_3.setFont(font3)
        self.v_max_lab_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.v_max_lab_3, 0, 1, 1, 1)

        self.v_max_lab_2 = QLabel(self.centralwidget)
        self.v_max_lab_2.setObjectName(u"v_max_lab_2")
        self.v_max_lab_2.setFont(font3)
        self.v_max_lab_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.v_max_lab_2, 0, 2, 1, 1)

        self.v_min_box = QDoubleSpinBox(self.centralwidget)
        self.v_min_box.setObjectName(u"v_min_box")
        self.v_min_box.setDecimals(1)
        self.v_min_box.setMaximum(62.000000000000000)

        self.gridLayout.addWidget(self.v_min_box, 1, 0, 1, 1)

        self.v_max_box = QDoubleSpinBox(self.centralwidget)
        self.v_max_box.setObjectName(u"v_max_box")
        self.v_max_box.setDecimals(1)
        self.v_max_box.setMaximum(62.000000000000000)

        self.gridLayout.addWidget(self.v_max_box, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.V_Set_Dial = QDial(self.centralwidget)
        self.V_Set_Dial.setObjectName(u"V_Set_Dial")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.V_Set_Dial.sizePolicy().hasHeightForWidth())
        self.V_Set_Dial.setSizePolicy(sizePolicy3)
        self.V_Set_Dial.setMinimumSize(QSize(150, 150))
        self.V_Set_Dial.setMaximum(10000)
        self.V_Set_Dial.setNotchTarget(100.000000000000000)
        self.V_Set_Dial.setNotchesVisible(True)

        self.verticalLayout.addWidget(self.V_Set_Dial)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.v_min_lab = QLabel(self.centralwidget)
        self.v_min_lab.setObjectName(u"v_min_lab")
        self.v_min_lab.setFont(font2)
        self.v_min_lab.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout.addWidget(self.v_min_lab)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.v_max_lab = QLabel(self.centralwidget)
        self.v_max_lab.setObjectName(u"v_max_lab")
        self.v_max_lab.setFont(font2)
        self.v_max_lab.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.v_max_lab)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.V_Set_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.V_Set_SpinBox.setObjectName(u"V_Set_SpinBox")
        font5 = QFont()
        font5.setPointSize(16)
        self.V_Set_SpinBox.setFont(font5)
        self.V_Set_SpinBox.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.V_Set_SpinBox.setAlignment(Qt.AlignCenter)
        self.V_Set_SpinBox.setDecimals(4)
        self.V_Set_SpinBox.setMaximum(100.000000000000000)
        self.V_Set_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.V_Set_SpinBox)

        self.V_Set_Button = QToolButton(self.centralwidget)
        self.V_Set_Button.setObjectName(u"V_Set_Button")
        sizePolicy3.setHeightForWidth(self.V_Set_Button.sizePolicy().hasHeightForWidth())
        self.V_Set_Button.setSizePolicy(sizePolicy3)
        self.V_Set_Button.setFont(font5)

        self.horizontalLayout_3.addWidget(self.V_Set_Button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_3.addLayout(self.verticalLayout, 4, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.I_Set_Label = QLabel(self.centralwidget)
        self.I_Set_Label.setObjectName(u"I_Set_Label")
        self.I_Set_Label.setFont(font4)
        self.I_Set_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.I_Set_Label)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(3)
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.i_step_box = QComboBox(self.centralwidget)
        self.i_step_box.setObjectName(u"i_step_box")
        sizePolicy2.setHeightForWidth(self.i_step_box.sizePolicy().hasHeightForWidth())
        self.i_step_box.setSizePolicy(sizePolicy2)
        self.i_step_box.setEditable(False)

        self.gridLayout_4.addWidget(self.i_step_box, 1, 1, 1, 1)

        self.v_max_lab_4 = QLabel(self.centralwidget)
        self.v_max_lab_4.setObjectName(u"v_max_lab_4")
        self.v_max_lab_4.setFont(font3)
        self.v_max_lab_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_4.addWidget(self.v_max_lab_4, 0, 2, 1, 1)

        self.v_max_lab_5 = QLabel(self.centralwidget)
        self.v_max_lab_5.setObjectName(u"v_max_lab_5")
        self.v_max_lab_5.setFont(font3)
        self.v_max_lab_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_4.addWidget(self.v_max_lab_5, 0, 1, 1, 1)

        self.v_min_lab_3 = QLabel(self.centralwidget)
        self.v_min_lab_3.setObjectName(u"v_min_lab_3")
        self.v_min_lab_3.setFont(font3)
        self.v_min_lab_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_4.addWidget(self.v_min_lab_3, 0, 0, 1, 1)

        self.i_max_box = QDoubleSpinBox(self.centralwidget)
        self.i_max_box.setObjectName(u"i_max_box")
        self.i_max_box.setDecimals(1)
        self.i_max_box.setMaximum(19.000000000000000)

        self.gridLayout_4.addWidget(self.i_max_box, 1, 2, 1, 1)

        self.i_min_box = QDoubleSpinBox(self.centralwidget)
        self.i_min_box.setObjectName(u"i_min_box")
        self.i_min_box.setDecimals(1)

        self.gridLayout_4.addWidget(self.i_min_box, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.I_Set_Dial = QDial(self.centralwidget)
        self.I_Set_Dial.setObjectName(u"I_Set_Dial")
        sizePolicy3.setHeightForWidth(self.I_Set_Dial.sizePolicy().hasHeightForWidth())
        self.I_Set_Dial.setSizePolicy(sizePolicy3)
        self.I_Set_Dial.setMinimumSize(QSize(150, 150))
        self.I_Set_Dial.setMaximum(10000)
        self.I_Set_Dial.setNotchTarget(100.000000000000000)
        self.I_Set_Dial.setNotchesVisible(True)

        self.verticalLayout_2.addWidget(self.I_Set_Dial)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.i_min_lab = QLabel(self.centralwidget)
        self.i_min_lab.setObjectName(u"i_min_lab")
        self.i_min_lab.setFont(font2)
        self.i_min_lab.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_2.addWidget(self.i_min_lab, 0, Qt.AlignVCenter)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.i_max_lab = QLabel(self.centralwidget)
        self.i_max_lab.setObjectName(u"i_max_lab")
        self.i_max_lab.setFont(font2)
        self.i_max_lab.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.i_max_lab)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.I_Set_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.I_Set_SpinBox.setObjectName(u"I_Set_SpinBox")
        self.I_Set_SpinBox.setFont(font5)
        self.I_Set_SpinBox.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.I_Set_SpinBox.setAlignment(Qt.AlignCenter)
        self.I_Set_SpinBox.setDecimals(4)
        self.I_Set_SpinBox.setMaximum(100.000000000000000)
        self.I_Set_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_4.addWidget(self.I_Set_SpinBox)

        self.I_Set_Button = QToolButton(self.centralwidget)
        self.I_Set_Button.setObjectName(u"I_Set_Button")
        sizePolicy3.setHeightForWidth(self.I_Set_Button.sizePolicy().hasHeightForWidth())
        self.I_Set_Button.setSizePolicy(sizePolicy3)
        self.I_Set_Button.setFont(font5)

        self.horizontalLayout_4.addWidget(self.I_Set_Button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 4, 2, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 0, 3, 6, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.Menu_Bar = QMenuBar(MainWindow)
        self.Menu_Bar.setObjectName(u"Menu_Bar")
        self.Menu_Bar.setGeometry(QRect(0, 0, 765, 29))
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
        self.V_Set_Label.setBuddy(self.V_Set_Dial)
        self.I_Set_Label.setBuddy(self.I_Set_Dial)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.V_Set_Dial, self.I_Set_Dial)

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
        self.Action_Settings.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.Action_About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Action_Serial.setText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.Action_Set_VI_ranges.setText(QCoreApplication.translate("MainWindow", u"Set GUI V/I limits", None))
        self.OutputC.setText(QCoreApplication.translate("MainWindow", u"00.0000", None))
        self.OutputV.setText(QCoreApplication.translate("MainWindow", u"00.000", None))
        self.OutputV_Label.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.OutputC_Label.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.OutputP.setText(QCoreApplication.translate("MainWindow", u"00.000", None))
        self.OutputP_Label.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.OutputS_Button.setText(QCoreApplication.translate("MainWindow", u"Toggle Output", None))
        self.Live_Box.setText(QCoreApplication.translate("MainWindow", u"Apply V/I changes in realtime", None))
        self.Protection.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.Keypad.setText(QCoreApplication.translate("MainWindow", u"Unlocked", None))
        self.Keypad_Label.setText(QCoreApplication.translate("MainWindow", u"Keypad Lock", None))
        self.Constant_Label.setText(QCoreApplication.translate("MainWindow", u"CC/CV Status", None))
        self.CCCV.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.Protection_Label.setText(QCoreApplication.translate("MainWindow", u"Protection Status", None))
        self.InputV.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.Temp.setText(QCoreApplication.translate("MainWindow", u"00.00\u00b0C | 00.00\u00b0F", None))
        self.Energy.setText(QCoreApplication.translate("MainWindow", u"00.00 Ah | 00.00 Wh", None))
        self.V_Set_Label.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.v_step_box.setCurrentText("")
        self.v_min_lab_2.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.v_max_lab_3.setText(QCoreApplication.translate("MainWindow", u"step", None))
        self.v_max_lab_2.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.v_min_lab.setText(QCoreApplication.translate("MainWindow", u"v_min", None))
        self.v_max_lab.setText(QCoreApplication.translate("MainWindow", u"v_max", None))
        self.V_Set_Button.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.I_Set_Label.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.i_step_box.setCurrentText("")
        self.v_max_lab_4.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.v_max_lab_5.setText(QCoreApplication.translate("MainWindow", u"step", None))
        self.v_min_lab_3.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.i_min_lab.setText(QCoreApplication.translate("MainWindow", u"i_min", None))
        self.i_max_lab.setText(QCoreApplication.translate("MainWindow", u"i_max", None))
        self.I_Set_Button.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.Menu_File.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.Menu_About.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

