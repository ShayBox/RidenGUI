# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SettingsWizard(object):
    def setupUi(self, SettingsWizard):
        if not SettingsWizard.objectName():
            SettingsWizard.setObjectName(u"SettingsWizard")
        SettingsWizard.resize(306, 606)
        icon = QIcon()
        iconThemeName = u"riden"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        SettingsWizard.setWindowIcon(icon)
        SettingsWizard.setOptions(QWizard.NoBackButtonOnStartPage)
        self.wizardPage1 = QWizardPage()
        self.wizardPage1.setObjectName(u"wizardPage1")
        self.formLayout = QFormLayout(self.wizardPage1)
        self.formLayout.setObjectName(u"formLayout")
        self.portLabel = QLabel(self.wizardPage1)
        self.portLabel.setObjectName(u"portLabel")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.portLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.portLabel)

        self.portLine = QLineEdit(self.wizardPage1)
        self.portLine.setObjectName(u"portLine")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.portLine)

        self.baudrateLabel = QLabel(self.wizardPage1)
        self.baudrateLabel.setObjectName(u"baudrateLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.baudrateLabel)

        self.baudrateCombo = QComboBox(self.wizardPage1)
        self.baudrateCombo.addItem("")
        self.baudrateCombo.addItem("")
        self.baudrateCombo.addItem("")
        self.baudrateCombo.addItem("")
        self.baudrateCombo.addItem("")
        self.baudrateCombo.addItem("")
        self.baudrateCombo.addItem("")
        self.baudrateCombo.addItem("")
        self.baudrateCombo.addItem("")
        self.baudrateCombo.addItem("")
        self.baudrateCombo.setObjectName(u"baudrateCombo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.baudrateCombo)

        self.addressLabel = QLabel(self.wizardPage1)
        self.addressLabel.setObjectName(u"addressLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.addressLabel)

        self.addressSpin = QSpinBox(self.wizardPage1)
        self.addressSpin.setObjectName(u"addressSpin")
        self.addressSpin.setMaximum(255)
        self.addressSpin.setValue(1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.addressSpin)

        self.pollingLabel = QLabel(self.wizardPage1)
        self.pollingLabel.setObjectName(u"pollingLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.pollingLabel)

        self.pollingSpin = QSpinBox(self.wizardPage1)
        self.pollingSpin.setObjectName(u"pollingSpin")
        self.pollingSpin.setMinimum(1)
        self.pollingSpin.setMaximum(10000)
        self.pollingSpin.setValue(500)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pollingSpin)

        SettingsWizard.setPage(1, self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName(u"wizardPage2")
        self.formLayout_2 = QFormLayout(self.wizardPage2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.colorsLabel = QLabel(self.wizardPage2)
        self.colorsLabel.setObjectName(u"colorsLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.colorsLabel)

        self.inputVoltagePush = QPushButton(self.wizardPage2)
        self.inputVoltagePush.setObjectName(u"inputVoltagePush")
        self.inputVoltagePush.setStyleSheet(u"color: #ff00ff")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.inputVoltagePush)

        self.outputVoltagePush = QPushButton(self.wizardPage2)
        self.outputVoltagePush.setObjectName(u"outputVoltagePush")
        self.outputVoltagePush.setStyleSheet(u"color: #ffff00")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.outputVoltagePush)

        self.outputCurrentPush = QPushButton(self.wizardPage2)
        self.outputCurrentPush.setObjectName(u"outputCurrentPush")
        self.outputCurrentPush.setStyleSheet(u"color: #00ffff")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.outputCurrentPush)

        self.outputPowerPush = QPushButton(self.wizardPage2)
        self.outputPowerPush.setObjectName(u"outputPowerPush")
        self.outputPowerPush.setStyleSheet(u"color: #ff00ff")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.outputPowerPush)

        self.outputOnPush = QPushButton(self.wizardPage2)
        self.outputOnPush.setObjectName(u"outputOnPush")
        self.outputOnPush.setStyleSheet(u"color: #00ff00")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.outputOnPush)

        self.outputOffPush = QPushButton(self.wizardPage2)
        self.outputOffPush.setObjectName(u"outputOffPush")
        self.outputOffPush.setStyleSheet(u"color: #808080")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.outputOffPush)

        self.outputFaultPush = QPushButton(self.wizardPage2)
        self.outputFaultPush.setObjectName(u"outputFaultPush")
        self.outputFaultPush.setStyleSheet(u"color: #ff0000")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.outputFaultPush)

        self.voltageSetPush = QPushButton(self.wizardPage2)
        self.voltageSetPush.setObjectName(u"voltageSetPush")
        self.voltageSetPush.setStyleSheet(u"color: #ffff00")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.voltageSetPush)

        self.currentSetPush = QPushButton(self.wizardPage2)
        self.currentSetPush.setObjectName(u"currentSetPush")
        self.currentSetPush.setStyleSheet(u"color: #ffff00")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.currentSetPush)

        SettingsWizard.setPage(2, self.wizardPage2)
        self.wizardPage3 = QWizardPage()
        self.wizardPage3.setObjectName(u"wizardPage3")
        self.formLayout_3 = QFormLayout(self.wizardPage3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.inputVoltageLine = QLineEdit(self.wizardPage3)
        self.inputVoltageLine.setObjectName(u"inputVoltageLine")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.inputVoltageLine)

        self.outputVoltageLine = QLineEdit(self.wizardPage3)
        self.outputVoltageLine.setObjectName(u"outputVoltageLine")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.outputVoltageLine)

        self.inputVoltageLabel = QLabel(self.wizardPage3)
        self.inputVoltageLabel.setObjectName(u"inputVoltageLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.inputVoltageLabel)

        self.outputVoltageLabel = QLabel(self.wizardPage3)
        self.outputVoltageLabel.setObjectName(u"outputVoltageLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.outputVoltageLabel)

        self.outputCurrentLabel = QLabel(self.wizardPage3)
        self.outputCurrentLabel.setObjectName(u"outputCurrentLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.outputCurrentLabel)

        self.outputCurrentLine = QLineEdit(self.wizardPage3)
        self.outputCurrentLine.setObjectName(u"outputCurrentLine")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.outputCurrentLine)

        self.outputPowerLabel = QLabel(self.wizardPage3)
        self.outputPowerLabel.setObjectName(u"outputPowerLabel")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.outputPowerLabel)

        self.outputPowerLine = QLineEdit(self.wizardPage3)
        self.outputPowerLine.setObjectName(u"outputPowerLine")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.outputPowerLine)

        SettingsWizard.setPage(3, self.wizardPage3)
#if QT_CONFIG(shortcut)
        self.portLabel.setBuddy(self.portLine)
        self.baudrateLabel.setBuddy(self.baudrateCombo)
        self.addressLabel.setBuddy(self.addressSpin)
        self.colorsLabel.setBuddy(self.inputVoltagePush)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.portLine, self.inputVoltagePush)
        QWidget.setTabOrder(self.inputVoltagePush, self.outputVoltagePush)
        QWidget.setTabOrder(self.outputVoltagePush, self.outputCurrentPush)
        QWidget.setTabOrder(self.outputCurrentPush, self.outputPowerPush)
        QWidget.setTabOrder(self.outputPowerPush, self.outputOnPush)
        QWidget.setTabOrder(self.outputOnPush, self.outputOffPush)
        QWidget.setTabOrder(self.outputOffPush, self.outputFaultPush)
        QWidget.setTabOrder(self.outputFaultPush, self.voltageSetPush)
        QWidget.setTabOrder(self.voltageSetPush, self.currentSetPush)

        self.retranslateUi(SettingsWizard)

        self.baudrateCombo.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(SettingsWizard)
    # setupUi

    def retranslateUi(self, SettingsWizard):
        SettingsWizard.setWindowTitle(QCoreApplication.translate("SettingsWizard", u"Settings Wizard", None))
        self.wizardPage1.setTitle(QCoreApplication.translate("SettingsWizard", u"Serial", None))
        self.wizardPage1.setSubTitle(QCoreApplication.translate("SettingsWizard", u"Serial communication", None))
        self.portLabel.setText(QCoreApplication.translate("SettingsWizard", u"Serial Port", None))
        self.portLine.setText(QCoreApplication.translate("SettingsWizard", u"/dev/ttyUSB0", None))
        self.baudrateLabel.setText(QCoreApplication.translate("SettingsWizard", u"Baudrate", None))
        self.baudrateCombo.setItemText(0, QCoreApplication.translate("SettingsWizard", u"9600", None))
        self.baudrateCombo.setItemText(1, QCoreApplication.translate("SettingsWizard", u"19200", None))
        self.baudrateCombo.setItemText(2, QCoreApplication.translate("SettingsWizard", u"38400", None))
        self.baudrateCombo.setItemText(3, QCoreApplication.translate("SettingsWizard", u"57600", None))
        self.baudrateCombo.setItemText(4, QCoreApplication.translate("SettingsWizard", u"115200", None))
        self.baudrateCombo.setItemText(5, QCoreApplication.translate("SettingsWizard", u"230400", None))
        self.baudrateCombo.setItemText(6, QCoreApplication.translate("SettingsWizard", u"250000", None))
        self.baudrateCombo.setItemText(7, QCoreApplication.translate("SettingsWizard", u"460800", None))
        self.baudrateCombo.setItemText(8, QCoreApplication.translate("SettingsWizard", u"921600", None))
        self.baudrateCombo.setItemText(9, QCoreApplication.translate("SettingsWizard", u"1000000", None))

        self.addressLabel.setText(QCoreApplication.translate("SettingsWizard", u"Address", None))
        self.pollingLabel.setText(QCoreApplication.translate("SettingsWizard", u"Polling (ms)", None))
        self.wizardPage2.setTitle(QCoreApplication.translate("SettingsWizard", u"Style", None))
        self.wizardPage2.setSubTitle(QCoreApplication.translate("SettingsWizard", u"CSS stylesheet", None))
        self.colorsLabel.setText(QCoreApplication.translate("SettingsWizard", u"Custom Colors", None))
        self.inputVoltagePush.setText(QCoreApplication.translate("SettingsWizard", u"Input Voltage", None))
        self.outputVoltagePush.setText(QCoreApplication.translate("SettingsWizard", u"Output Voltage", None))
        self.outputCurrentPush.setText(QCoreApplication.translate("SettingsWizard", u"Output Current", None))
        self.outputPowerPush.setText(QCoreApplication.translate("SettingsWizard", u"Output Power", None))
        self.outputOnPush.setText(QCoreApplication.translate("SettingsWizard", u"Output ON", None))
        self.outputOffPush.setText(QCoreApplication.translate("SettingsWizard", u"Output OFF", None))
        self.outputFaultPush.setText(QCoreApplication.translate("SettingsWizard", u"Output Fault", None))
        self.voltageSetPush.setText(QCoreApplication.translate("SettingsWizard", u"Voltage Set", None))
        self.currentSetPush.setText(QCoreApplication.translate("SettingsWizard", u"Current Set", None))
        self.wizardPage3.setTitle(QCoreApplication.translate("SettingsWizard", u"Format", None))
        self.wizardPage3.setSubTitle(QCoreApplication.translate("SettingsWizard", u"Python format strings", None))
        self.inputVoltageLine.setText(QCoreApplication.translate("SettingsWizard", u"%05.2f", None))
        self.outputVoltageLine.setText(QCoreApplication.translate("SettingsWizard", u"%05.2f", None))
        self.inputVoltageLabel.setText(QCoreApplication.translate("SettingsWizard", u"Voltage In", None))
        self.outputVoltageLabel.setText(QCoreApplication.translate("SettingsWizard", u"Voltage Out", None))
        self.outputCurrentLabel.setText(QCoreApplication.translate("SettingsWizard", u"Current Out", None))
        self.outputCurrentLine.setText(QCoreApplication.translate("SettingsWizard", u"%05.2f", None))
        self.outputPowerLabel.setText(QCoreApplication.translate("SettingsWizard", u"Power Out", None))
        self.outputPowerLine.setText(QCoreApplication.translate("SettingsWizard", u"%6.2f", None))
    # retranslateUi

