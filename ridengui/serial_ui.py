# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serial.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Serial(object):
    def setupUi(self, Serial):
        if not Serial.objectName():
            Serial.setObjectName(u"Serial")
        Serial.resize(265, 149)
        icon = QIcon()
        iconThemeName = u"riden"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        Serial.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Serial)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Serial_Label = QLabel(Serial)
        self.Serial_Label.setObjectName(u"Serial_Label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Serial_Label.setFont(font)
        self.Serial_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.Serial_Label, 2, 0, 1, 1)

        self.Baudrate_Label = QLabel(Serial)
        self.Baudrate_Label.setObjectName(u"Baudrate_Label")
        self.Baudrate_Label.setFont(font)
        self.Baudrate_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.Baudrate_Label, 4, 0, 1, 1)

        self.Serial_Line = QLineEdit(Serial)
        self.Serial_Line.setObjectName(u"Serial_Line")
        self.Serial_Line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Serial_Line, 2, 1, 1, 2)

        self.Address_Box = QSpinBox(Serial)
        self.Address_Box.setObjectName(u"Address_Box")
        self.Address_Box.setMinimum(1)
        self.Address_Box.setMaximum(255)

        self.gridLayout.addWidget(self.Address_Box, 5, 1, 1, 2)

        self.Baudrate_Box = QComboBox(Serial)
        self.Baudrate_Box.addItem("")
        self.Baudrate_Box.addItem("")
        self.Baudrate_Box.addItem("")
        self.Baudrate_Box.addItem("")
        self.Baudrate_Box.addItem("")
        self.Baudrate_Box.setObjectName(u"Baudrate_Box")

        self.gridLayout.addWidget(self.Baudrate_Box, 4, 1, 1, 2)

        self.Address_Label = QLabel(Serial)
        self.Address_Label.setObjectName(u"Address_Label")
        self.Address_Label.setFont(font)
        self.Address_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.Address_Label, 5, 0, 1, 1)

        self.Buttons = QDialogButtonBox(Serial)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setOrientation(Qt.Horizontal)
        self.Buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.Buttons, 9, 2, 1, 1)


        self.retranslateUi(Serial)
        self.Buttons.accepted.connect(Serial.accept)
        self.Buttons.rejected.connect(Serial.reject)

        QMetaObject.connectSlotsByName(Serial)
    # setupUi

    def retranslateUi(self, Serial):
        Serial.setWindowTitle(QCoreApplication.translate("Serial", u"Serial", None))
        self.Serial_Label.setText(QCoreApplication.translate("Serial", u"Serial Port", None))
        self.Baudrate_Label.setText(QCoreApplication.translate("Serial", u"Baudrate", None))
        self.Serial_Line.setText(QCoreApplication.translate("Serial", u"/dev/ttyUSB0", None))
        self.Baudrate_Box.setItemText(0, QCoreApplication.translate("Serial", u"115200", None))
        self.Baudrate_Box.setItemText(1, QCoreApplication.translate("Serial", u"57600", None))
        self.Baudrate_Box.setItemText(2, QCoreApplication.translate("Serial", u"38400", None))
        self.Baudrate_Box.setItemText(3, QCoreApplication.translate("Serial", u"19200", None))
        self.Baudrate_Box.setItemText(4, QCoreApplication.translate("Serial", u"9600", None))

        self.Address_Label.setText(QCoreApplication.translate("Serial", u"Address", None))
    # retranslateUi

