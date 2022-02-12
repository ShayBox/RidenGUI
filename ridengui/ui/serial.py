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
        Serial.resize(292, 177)
        icon = QIcon()
        iconThemeName = u"riden"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        Serial.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Serial)
        self.gridLayout.setObjectName(u"gridLayout")
        self.serial_label = QLabel(Serial)
        self.serial_label.setObjectName(u"serial_label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.serial_label.setFont(font)
        self.serial_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.serial_label, 2, 0, 1, 1)

        self.baudrate_label = QLabel(Serial)
        self.baudrate_label.setObjectName(u"baudrate_label")
        self.baudrate_label.setFont(font)
        self.baudrate_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.baudrate_label, 4, 0, 1, 1)

        self.serial_line = QLineEdit(Serial)
        self.serial_line.setObjectName(u"serial_line")
        self.serial_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.serial_line, 2, 1, 1, 2)

        self.address_box = QSpinBox(Serial)
        self.address_box.setObjectName(u"address_box")
        self.address_box.setMinimum(1)
        self.address_box.setMaximum(255)

        self.gridLayout.addWidget(self.address_box, 5, 1, 1, 2)

        self.baudrate_box = QComboBox(Serial)
        self.baudrate_box.addItem("")
        self.baudrate_box.addItem("")
        self.baudrate_box.addItem("")
        self.baudrate_box.addItem("")
        self.baudrate_box.addItem("")
        self.baudrate_box.addItem("")
        self.baudrate_box.addItem("")
        self.baudrate_box.addItem("")
        self.baudrate_box.addItem("")
        self.baudrate_box.addItem("")
        self.baudrate_box.setObjectName(u"baudrate_box")
        self.baudrate_box.setMaxCount(1000000)

        self.gridLayout.addWidget(self.baudrate_box, 4, 1, 1, 2)

        self.address_label = QLabel(Serial)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setFont(font)
        self.address_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.address_label, 5, 0, 1, 1)

        self.buttons = QDialogButtonBox(Serial)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttons, 9, 2, 1, 1)


        self.retranslateUi(Serial)
        self.buttons.accepted.connect(Serial.accept)
        self.buttons.rejected.connect(Serial.reject)

        self.baudrate_box.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Serial)
    # setupUi

    def retranslateUi(self, Serial):
        Serial.setWindowTitle(QCoreApplication.translate("Serial", u"Serial", None))
        self.serial_label.setText(QCoreApplication.translate("Serial", u"Serial Port", None))
        self.baudrate_label.setText(QCoreApplication.translate("Serial", u"Baudrate", None))
        self.serial_line.setText(QCoreApplication.translate("Serial", u"/dev/ttyUSB0", None))
        self.baudrate_box.setItemText(0, QCoreApplication.translate("Serial", u"1000000", None))
        self.baudrate_box.setItemText(1, QCoreApplication.translate("Serial", u"921600", None))
        self.baudrate_box.setItemText(2, QCoreApplication.translate("Serial", u"460800", None))
        self.baudrate_box.setItemText(3, QCoreApplication.translate("Serial", u"250000", None))
        self.baudrate_box.setItemText(4, QCoreApplication.translate("Serial", u"230400", None))
        self.baudrate_box.setItemText(5, QCoreApplication.translate("Serial", u"115200", None))
        self.baudrate_box.setItemText(6, QCoreApplication.translate("Serial", u"57600", None))
        self.baudrate_box.setItemText(7, QCoreApplication.translate("Serial", u"38400", None))
        self.baudrate_box.setItemText(8, QCoreApplication.translate("Serial", u"19200", None))
        self.baudrate_box.setItemText(9, QCoreApplication.translate("Serial", u"9600", None))

        self.address_label.setText(QCoreApplication.translate("Serial", u"Address", None))
    # retranslateUi

