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


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(312, 288)
        icon = QIcon()
        iconThemeName = u"riden"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        Settings.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Backlight_Slider = QSlider(Settings)
        self.Backlight_Slider.setObjectName(u"Backlight_Slider")
        self.Backlight_Slider.setMaximum(5)
        self.Backlight_Slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Backlight_Slider, 1, 2, 1, 2)

        self.Language_ComboBox = QComboBox(Settings)
        self.Language_ComboBox.addItem("")
        self.Language_ComboBox.addItem("")
        self.Language_ComboBox.addItem("")
        self.Language_ComboBox.addItem("")
        self.Language_ComboBox.setObjectName(u"Language_ComboBox")

        self.gridLayout.addWidget(self.Language_ComboBox, 0, 2, 1, 2)

        self.Backlight_Label = QLabel(Settings)
        self.Backlight_Label.setObjectName(u"Backlight_Label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Backlight_Label.setFont(font)
        self.Backlight_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Backlight_Label, 1, 1, 1, 1)

        self.Language_Label = QLabel(Settings)
        self.Language_Label.setObjectName(u"Language_Label")
        self.Language_Label.setFont(font)
        self.Language_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Language_Label, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Confirm_Box = QCheckBox(Settings)
        self.Confirm_Box.setObjectName(u"Confirm_Box")

        self.gridLayout_2.addWidget(self.Confirm_Box, 1, 0, 1, 1)

        self.Logo_Box = QCheckBox(Settings)
        self.Logo_Box.setObjectName(u"Logo_Box")

        self.gridLayout_2.addWidget(self.Logo_Box, 5, 0, 1, 1)

        self.Restore_Box = QCheckBox(Settings)
        self.Restore_Box.setObjectName(u"Restore_Box")

        self.gridLayout_2.addWidget(self.Restore_Box, 2, 0, 1, 1)

        self.Power_Box = QCheckBox(Settings)
        self.Power_Box.setObjectName(u"Power_Box")

        self.gridLayout_2.addWidget(self.Power_Box, 3, 0, 1, 1)

        self.Buzzer_Box = QCheckBox(Settings)
        self.Buzzer_Box.setObjectName(u"Buzzer_Box")

        self.gridLayout_2.addWidget(self.Buzzer_Box, 4, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 3)

        self.Time_Button = QPushButton(Settings)
        self.Time_Button.setObjectName(u"Time_Button")

        self.gridLayout.addWidget(self.Time_Button, 6, 1, 1, 1)

        self.Buttons = QDialogButtonBox(Settings)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setOrientation(Qt.Horizontal)
        self.Buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.Buttons, 6, 2, 1, 1)


        self.retranslateUi(Settings)
        self.Buttons.accepted.connect(Settings.accept)
        self.Buttons.rejected.connect(Settings.reject)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.Language_ComboBox.setItemText(0, QCoreApplication.translate("Settings", u"English", None))
        self.Language_ComboBox.setItemText(1, QCoreApplication.translate("Settings", u"Chinese", None))
        self.Language_ComboBox.setItemText(2, QCoreApplication.translate("Settings", u"Deutsch", None))
        self.Language_ComboBox.setItemText(3, QCoreApplication.translate("Settings", u"Fran\u00e7ais", None))

        self.Backlight_Label.setText(QCoreApplication.translate("Settings", u"Backlight", None))
        self.Language_Label.setText(QCoreApplication.translate("Settings", u"Language", None))
        self.Confirm_Box.setText(QCoreApplication.translate("Settings", u"Confirm memory state change", None))
        self.Logo_Box.setText(QCoreApplication.translate("Settings", u"Enable Boot Logo", None))
        self.Restore_Box.setText(QCoreApplication.translate("Settings", u"Restore state on boot", None))
        self.Power_Box.setText(QCoreApplication.translate("Settings", u"Power-on after power-loss", None))
        self.Buzzer_Box.setText(QCoreApplication.translate("Settings", u"Enable Buzzer", None))
        self.Time_Button.setText(QCoreApplication.translate("Settings", u"Sync Time", None))
    # retranslateUi

