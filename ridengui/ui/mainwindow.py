# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        MainWindow.resize(1040, 728)
        icon = QIcon()
        iconThemeName = u"riden"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAboutRiden = QAction(MainWindow)
        self.actionAboutRiden.setObjectName(u"actionAboutRiden")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionOptions = QAction(MainWindow)
        self.actionOptions.setObjectName(u"actionOptions")
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.keypadLabel = QLabel(self.centralwidget)
        self.keypadLabel.setObjectName(u"keypadLabel")
        font = QFont()
        font.setPointSize(12)
        self.keypadLabel.setFont(font)
        self.keypadLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.keypadLabel, 0, 0, 1, 1)

        self.constantLabel = QLabel(self.centralwidget)
        self.constantLabel.setObjectName(u"constantLabel")
        self.constantLabel.setFont(font)
        self.constantLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.constantLabel, 1, 0, 1, 1)

        self.keypad = QLabel(self.centralwidget)
        self.keypad.setObjectName(u"keypad")
        self.keypad.setFont(font)

        self.gridLayout.addWidget(self.keypad, 0, 1, 1, 1)

        self.constant = QLabel(self.centralwidget)
        self.constant.setObjectName(u"constant")
        self.constant.setFont(font)

        self.gridLayout.addWidget(self.constant, 1, 1, 1, 1)

        self.faultLabel = QLabel(self.centralwidget)
        self.faultLabel.setObjectName(u"faultLabel")
        self.faultLabel.setFont(font)
        self.faultLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.faultLabel, 2, 0, 1, 1)

        self.fault = QLabel(self.centralwidget)
        self.fault.setObjectName(u"fault")
        self.fault.setFont(font)

        self.gridLayout.addWidget(self.fault, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 3, 0, 1, 3)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 0, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.realtimeCheck = QCheckBox(self.centralwidget)
        self.realtimeCheck.setObjectName(u"realtimeCheck")
        self.realtimeCheck.setFont(font)
        self.realtimeCheck.setStyleSheet(u"color:#ff0000")

        self.gridLayout_7.addWidget(self.realtimeCheck, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_7, 2, 0, 1, 3)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 1, 0, 1, 3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.energy = QLabel(self.centralwidget)
        self.energy.setObjectName(u"energy")
        self.energy.setFont(font)

        self.gridLayout_3.addWidget(self.energy, 0, 1, 1, 1)

        self.intTemp = QLabel(self.centralwidget)
        self.intTemp.setObjectName(u"intTemp")
        self.intTemp.setFont(font)

        self.gridLayout_3.addWidget(self.intTemp, 1, 1, 1, 1)

        self.energyLabel = QLabel(self.centralwidget)
        self.energyLabel.setObjectName(u"energyLabel")
        self.energyLabel.setFont(font)
        self.energyLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.energyLabel, 0, 0, 1, 1)

        self.intTempLabel = QLabel(self.centralwidget)
        self.intTempLabel.setObjectName(u"intTempLabel")
        self.intTempLabel.setFont(font)
        self.intTempLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.intTempLabel, 1, 0, 1, 1)

        self.extTempLabel = QLabel(self.centralwidget)
        self.extTempLabel.setObjectName(u"extTempLabel")
        self.extTempLabel.setFont(font)
        self.extTempLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.extTempLabel, 2, 0, 1, 1)

        self.extTemp = QLabel(self.centralwidget)
        self.extTemp.setObjectName(u"extTemp")
        self.extTemp.setFont(font)

        self.gridLayout_3.addWidget(self.extTemp, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 2, 1, 1)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 4, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.voltageLabel = QLabel(self.centralwidget)
        self.voltageLabel.setObjectName(u"voltageLabel")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.voltageLabel.setFont(font1)
        self.voltageLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.voltageLabel, 0, 0, 1, 3)

        self.voltageMinDoubleSpin = QDoubleSpinBox(self.centralwidget)
        self.voltageMinDoubleSpin.setObjectName(u"voltageMinDoubleSpin")
        self.voltageMinDoubleSpin.setFont(font)
        self.voltageMinDoubleSpin.setMaximum(1000.000000000000000)

        self.gridLayout_5.addWidget(self.voltageMinDoubleSpin, 4, 0, 1, 1)

        self.voltageDoubleSpin = QDoubleSpinBox(self.centralwidget)
        self.voltageDoubleSpin.setObjectName(u"voltageDoubleSpin")
        font2 = QFont()
        font2.setPointSize(16)
        self.voltageDoubleSpin.setFont(font2)
        self.voltageDoubleSpin.setStyleSheet(u"color: #ffff00")
        self.voltageDoubleSpin.setAlignment(Qt.AlignCenter)
        self.voltageDoubleSpin.setMaximum(0.000000000000000)
        self.voltageDoubleSpin.setSingleStep(0.100000000000000)

        self.gridLayout_5.addWidget(self.voltageDoubleSpin, 5, 0, 1, 2)

        self.voltageMinLabel = QLabel(self.centralwidget)
        self.voltageMinLabel.setObjectName(u"voltageMinLabel")
        self.voltageMinLabel.setFont(font)
        self.voltageMinLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.voltageMinLabel, 3, 0, 1, 1)

        self.voltageMaxLabel = QLabel(self.centralwidget)
        self.voltageMaxLabel.setObjectName(u"voltageMaxLabel")
        self.voltageMaxLabel.setFont(font)
        self.voltageMaxLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.voltageMaxLabel, 3, 2, 1, 1)

        self.voltageMaxDoubleSpin = QDoubleSpinBox(self.centralwidget)
        self.voltageMaxDoubleSpin.setObjectName(u"voltageMaxDoubleSpin")
        self.voltageMaxDoubleSpin.setFont(font)
        self.voltageMaxDoubleSpin.setMaximum(1000.000000000000000)

        self.gridLayout_5.addWidget(self.voltageMaxDoubleSpin, 4, 2, 1, 1)

        self.voltageStepCombo = QComboBox(self.centralwidget)
        self.voltageStepCombo.addItem("")
        self.voltageStepCombo.addItem("")
        self.voltageStepCombo.addItem("")
        self.voltageStepCombo.addItem("")
        self.voltageStepCombo.addItem("")
        self.voltageStepCombo.setObjectName(u"voltageStepCombo")
        self.voltageStepCombo.setFont(font)

        self.gridLayout_5.addWidget(self.voltageStepCombo, 4, 1, 1, 1)

        self.voltageDial = QDial(self.centralwidget)
        self.voltageDial.setObjectName(u"voltageDial")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.voltageDial.sizePolicy().hasHeightForWidth())
        self.voltageDial.setSizePolicy(sizePolicy)
        self.voltageDial.setMinimumSize(QSize(350, 350))
        self.voltageDial.setMaximum(0)
        self.voltageDial.setPageStep(1)
        self.voltageDial.setNotchesVisible(True)

        self.gridLayout_5.addWidget(self.voltageDial, 1, 0, 1, 3)

        self.voltageStepLabel = QLabel(self.centralwidget)
        self.voltageStepLabel.setObjectName(u"voltageStepLabel")
        self.voltageStepLabel.setFont(font)
        self.voltageStepLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.voltageStepLabel, 3, 1, 1, 1)

        self.voltagePush = QPushButton(self.centralwidget)
        self.voltagePush.setObjectName(u"voltagePush")
        self.voltagePush.setEnabled(False)
        self.voltagePush.setFont(font2)

        self.gridLayout_5.addWidget(self.voltagePush, 5, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout_5, 4, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.currentStepLabel = QLabel(self.centralwidget)
        self.currentStepLabel.setObjectName(u"currentStepLabel")
        self.currentStepLabel.setFont(font)
        self.currentStepLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.currentStepLabel, 3, 1, 1, 1)

        self.currentDoubleSpin = QDoubleSpinBox(self.centralwidget)
        self.currentDoubleSpin.setObjectName(u"currentDoubleSpin")
        self.currentDoubleSpin.setFont(font2)
        self.currentDoubleSpin.setStyleSheet(u"color: #ffff00")
        self.currentDoubleSpin.setAlignment(Qt.AlignCenter)
        self.currentDoubleSpin.setMaximum(0.000000000000000)
        self.currentDoubleSpin.setSingleStep(0.100000000000000)

        self.gridLayout_6.addWidget(self.currentDoubleSpin, 5, 0, 1, 2)

        self.currentMinLabel = QLabel(self.centralwidget)
        self.currentMinLabel.setObjectName(u"currentMinLabel")
        self.currentMinLabel.setFont(font)
        self.currentMinLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.currentMinLabel, 3, 0, 1, 1)

        self.currentDial = QDial(self.centralwidget)
        self.currentDial.setObjectName(u"currentDial")
        sizePolicy.setHeightForWidth(self.currentDial.sizePolicy().hasHeightForWidth())
        self.currentDial.setSizePolicy(sizePolicy)
        self.currentDial.setMinimumSize(QSize(350, 350))
        self.currentDial.setMaximum(0)
        self.currentDial.setPageStep(1)
        self.currentDial.setNotchesVisible(True)

        self.gridLayout_6.addWidget(self.currentDial, 1, 0, 1, 3)

        self.currentMinDoubleSpin = QDoubleSpinBox(self.centralwidget)
        self.currentMinDoubleSpin.setObjectName(u"currentMinDoubleSpin")
        self.currentMinDoubleSpin.setFont(font)
        self.currentMinDoubleSpin.setMaximum(1000.000000000000000)

        self.gridLayout_6.addWidget(self.currentMinDoubleSpin, 4, 0, 1, 1)

        self.currentMaxDoubleSpin = QDoubleSpinBox(self.centralwidget)
        self.currentMaxDoubleSpin.setObjectName(u"currentMaxDoubleSpin")
        self.currentMaxDoubleSpin.setFont(font)
        self.currentMaxDoubleSpin.setMaximum(1000.000000000000000)

        self.gridLayout_6.addWidget(self.currentMaxDoubleSpin, 4, 2, 1, 1)

        self.currentMaxLabel = QLabel(self.centralwidget)
        self.currentMaxLabel.setObjectName(u"currentMaxLabel")
        self.currentMaxLabel.setFont(font)
        self.currentMaxLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.currentMaxLabel, 3, 2, 1, 1)

        self.currentStepCombo = QComboBox(self.centralwidget)
        self.currentStepCombo.addItem("")
        self.currentStepCombo.addItem("")
        self.currentStepCombo.addItem("")
        self.currentStepCombo.addItem("")
        self.currentStepCombo.addItem("")
        self.currentStepCombo.setObjectName(u"currentStepCombo")
        self.currentStepCombo.setFont(font)

        self.gridLayout_6.addWidget(self.currentStepCombo, 4, 1, 1, 1)

        self.currentLabel = QLabel(self.centralwidget)
        self.currentLabel.setObjectName(u"currentLabel")
        self.currentLabel.setFont(font1)
        self.currentLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.currentLabel, 0, 0, 1, 3)

        self.currentPush = QPushButton(self.centralwidget)
        self.currentPush.setObjectName(u"currentPush")
        self.currentPush.setEnabled(False)
        self.currentPush.setFont(font2)

        self.gridLayout_6.addWidget(self.currentPush, 5, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 2, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout_6, 4, 2, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.voltageInput = QLabel(self.centralwidget)
        self.voltageInput.setObjectName(u"voltageInput")
        sizePolicy.setHeightForWidth(self.voltageInput.sizePolicy().hasHeightForWidth())
        self.voltageInput.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(36)
        font3.setBold(True)
        font3.setWeight(75)
        self.voltageInput.setFont(font3)
        self.voltageInput.setStyleSheet(u"color: #ff00ff")
        self.voltageInput.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout_12.addWidget(self.voltageInput, 0, 0, 1, 1)

        self.powerOutputLabel = QLabel(self.centralwidget)
        self.powerOutputLabel.setObjectName(u"powerOutputLabel")
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.powerOutputLabel.setFont(font4)
        self.powerOutputLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.powerOutputLabel, 6, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_4, 3, 0, 1, 2)

        self.powerOutput = QLabel(self.centralwidget)
        self.powerOutput.setObjectName(u"powerOutput")
        self.powerOutput.setFont(font3)
        self.powerOutput.setStyleSheet(u"color: #ff00ff")
        self.powerOutput.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout_12.addWidget(self.powerOutput, 6, 0, 1, 1)

        self.currentOutputLabel = QLabel(self.centralwidget)
        self.currentOutputLabel.setObjectName(u"currentOutputLabel")
        self.currentOutputLabel.setFont(font4)
        self.currentOutputLabel.setStyleSheet(u"color: #00ffff")
        self.currentOutputLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.currentOutputLabel, 4, 1, 1, 1)

        self.currentOutput = QLabel(self.centralwidget)
        self.currentOutput.setObjectName(u"currentOutput")
        self.currentOutput.setFont(font3)
        self.currentOutput.setStyleSheet(u"color: #00ffff")
        self.currentOutput.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout_12.addWidget(self.currentOutput, 4, 0, 1, 1)

        self.voltageOutput = QLabel(self.centralwidget)
        self.voltageOutput.setObjectName(u"voltageOutput")
        self.voltageOutput.setFont(font3)
        self.voltageOutput.setStyleSheet(u"color: #00ff00")
        self.voltageOutput.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout_12.addWidget(self.voltageOutput, 2, 0, 1, 1)

        self.voltageOutputLabel = QLabel(self.centralwidget)
        self.voltageOutputLabel.setObjectName(u"voltageOutputLabel")
        self.voltageOutputLabel.setFont(font4)
        self.voltageOutputLabel.setStyleSheet(u"color: #00ff00")
        self.voltageOutputLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.voltageOutputLabel, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_3, 1, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_5, 5, 0, 1, 2)

        self.voltageInputLabel = QLabel(self.centralwidget)
        self.voltageInputLabel.setObjectName(u"voltageInputLabel")
        self.voltageInputLabel.setFont(font4)
        self.voltageInputLabel.setStyleSheet(u"color: #ff00ff")
        self.voltageInputLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.voltageInputLabel, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_12, 5, 0, 1, 1)

        self.outputPush = QPushButton(self.centralwidget)
        self.outputPush.setObjectName(u"outputPush")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.outputPush.sizePolicy().hasHeightForWidth())
        self.outputPush.setSizePolicy(sizePolicy1)
        self.outputPush.setMinimumSize(QSize(250, 250))
        self.outputPush.setFont(font3)

        self.gridLayout_4.addWidget(self.outputPush, 6, 0, 2, 2)


        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 4, 5, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 0, 3, 5, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1040, 32))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.voltageLabel.setBuddy(self.voltageDial)
        self.voltageMinLabel.setBuddy(self.voltageMinDoubleSpin)
        self.voltageMaxLabel.setBuddy(self.voltageMaxDoubleSpin)
        self.voltageStepLabel.setBuddy(self.voltageStepCombo)
        self.currentStepLabel.setBuddy(self.currentStepCombo)
        self.currentMinLabel.setBuddy(self.currentMinDoubleSpin)
        self.currentMaxLabel.setBuddy(self.currentMaxDoubleSpin)
        self.currentLabel.setBuddy(self.currentDial)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.realtimeCheck, self.voltageDial)
        QWidget.setTabOrder(self.voltageDial, self.voltageMinDoubleSpin)
        QWidget.setTabOrder(self.voltageMinDoubleSpin, self.voltageStepCombo)
        QWidget.setTabOrder(self.voltageStepCombo, self.voltageMaxDoubleSpin)
        QWidget.setTabOrder(self.voltageMaxDoubleSpin, self.voltageDoubleSpin)
        QWidget.setTabOrder(self.voltageDoubleSpin, self.voltagePush)
        QWidget.setTabOrder(self.voltagePush, self.currentDial)
        QWidget.setTabOrder(self.currentDial, self.currentMinDoubleSpin)
        QWidget.setTabOrder(self.currentMinDoubleSpin, self.currentStepCombo)
        QWidget.setTabOrder(self.currentStepCombo, self.currentMaxDoubleSpin)
        QWidget.setTabOrder(self.currentMaxDoubleSpin, self.currentDoubleSpin)
        QWidget.setTabOrder(self.currentDoubleSpin, self.currentPush)
        QWidget.setTabOrder(self.currentPush, self.outputPush)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionSettings)
        self.menuEdit.addAction(self.actionOptions)
        self.menuHelp.addAction(self.actionAboutRiden)
        self.menuHelp.addAction(self.actionAboutQt)

        self.retranslateUi(MainWindow)

        self.voltageStepCombo.setCurrentIndex(2)
        self.currentStepCombo.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RidenGUI", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAboutRiden.setText(QCoreApplication.translate("MainWindow", u"About RidenGUI", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"GUI Settings", None))
#if QT_CONFIG(tooltip)
        self.actionSettings.setToolTip(QCoreApplication.translate("MainWindow", u"GUI Settings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.actionSettings.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.actionOptions.setText(QCoreApplication.translate("MainWindow", u"Riden Options", None))
#if QT_CONFIG(tooltip)
        self.actionOptions.setToolTip(QCoreApplication.translate("MainWindow", u"Riden Options", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.actionOptions.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.keypadLabel.setText(QCoreApplication.translate("MainWindow", u"Keypad", None))
        self.constantLabel.setText(QCoreApplication.translate("MainWindow", u"Constant", None))
        self.keypad.setText(QCoreApplication.translate("MainWindow", u"Unlocked", None))
        self.constant.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.faultLabel.setText(QCoreApplication.translate("MainWindow", u"Fault", None))
        self.fault.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.realtimeCheck.setText(QCoreApplication.translate("MainWindow", u"Apply Voltage and Current changes in realtime", None))
        self.energy.setText(QCoreApplication.translate("MainWindow", u"00.00 Ah | 00.00 Wh", None))
        self.intTemp.setText(QCoreApplication.translate("MainWindow", u"00.00\u00b0C | 00.00\u00b0F", None))
        self.energyLabel.setText(QCoreApplication.translate("MainWindow", u"Energy", None))
        self.intTempLabel.setText(QCoreApplication.translate("MainWindow", u"Int Temp", None))
        self.extTempLabel.setText(QCoreApplication.translate("MainWindow", u"Ext Temp", None))
        self.extTemp.setText(QCoreApplication.translate("MainWindow", u"00.00\u00b0C | 00.00\u00b0F", None))
        self.voltageLabel.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.voltageMinLabel.setText(QCoreApplication.translate("MainWindow", u"Minimum", None))
        self.voltageMaxLabel.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.voltageStepCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.voltageStepCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"0.1", None))
        self.voltageStepCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"0.01", None))
        self.voltageStepCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"0.001", None))
        self.voltageStepCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"0.0001", None))

        self.voltageStepLabel.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.voltagePush.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.currentStepLabel.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.currentMinLabel.setText(QCoreApplication.translate("MainWindow", u"Minimum", None))
        self.currentMaxLabel.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.currentStepCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.currentStepCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"0.1", None))
        self.currentStepCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"0.01", None))
        self.currentStepCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"0.001", None))
        self.currentStepCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"0.0001", None))

        self.currentLabel.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.currentPush.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.voltageInput.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.powerOutputLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #ff00ff", None))
        self.powerOutputLabel.setText(QCoreApplication.translate("MainWindow", u"Watts", None))
        self.powerOutput.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.currentOutputLabel.setText(QCoreApplication.translate("MainWindow", u"Amps", None))
        self.currentOutput.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.voltageOutput.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.voltageOutputLabel.setText(QCoreApplication.translate("MainWindow", u"Volts", None))
        self.voltageInputLabel.setText(QCoreApplication.translate("MainWindow", u"Volts", None))
        self.outputPush.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

