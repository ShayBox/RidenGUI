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
        self.backlight_slider = QSlider(Settings)
        self.backlight_slider.setObjectName(u"backlight_slider")
        self.backlight_slider.setMaximum(5)
        self.backlight_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.backlight_slider, 1, 2, 1, 2)

        self.language_box = QComboBox(Settings)
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.setObjectName(u"language_box")

        self.gridLayout.addWidget(self.language_box, 0, 2, 1, 2)

        self.backlight_label = QLabel(Settings)
        self.backlight_label.setObjectName(u"backlight_label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.backlight_label.setFont(font)
        self.backlight_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.backlight_label, 1, 1, 1, 1)

        self.language_label = QLabel(Settings)
        self.language_label.setObjectName(u"language_label")
        self.language_label.setFont(font)
        self.language_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.language_label, 0, 1, 1, 1)

        self.settings_layout = QGridLayout()
        self.settings_layout.setObjectName(u"settings_layout")
        self.confirm_box = QCheckBox(Settings)
        self.confirm_box.setObjectName(u"confirm_box")

        self.settings_layout.addWidget(self.confirm_box, 1, 0, 1, 1)

        self.logo_box = QCheckBox(Settings)
        self.logo_box.setObjectName(u"logo_box")

        self.settings_layout.addWidget(self.logo_box, 5, 0, 1, 1)

        self.restore_box = QCheckBox(Settings)
        self.restore_box.setObjectName(u"restore_box")

        self.settings_layout.addWidget(self.restore_box, 2, 0, 1, 1)

        self.power_box = QCheckBox(Settings)
        self.power_box.setObjectName(u"power_box")

        self.settings_layout.addWidget(self.power_box, 3, 0, 1, 1)

        self.buzzer_box = QCheckBox(Settings)
        self.buzzer_box.setObjectName(u"buzzer_box")

        self.settings_layout.addWidget(self.buzzer_box, 4, 0, 1, 1)


        self.gridLayout.addLayout(self.settings_layout, 2, 1, 1, 3)

        self.time_button = QPushButton(Settings)
        self.time_button.setObjectName(u"time_button")

        self.gridLayout.addWidget(self.time_button, 6, 1, 1, 1)

        self.buttons = QDialogButtonBox(Settings)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttons, 6, 2, 1, 1)


        self.retranslateUi(Settings)
        self.buttons.accepted.connect(Settings.accept)
        self.buttons.rejected.connect(Settings.reject)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"General", None))
        self.language_box.setItemText(0, QCoreApplication.translate("Settings", u"English", None))
        self.language_box.setItemText(1, QCoreApplication.translate("Settings", u"Chinese", None))
        self.language_box.setItemText(2, QCoreApplication.translate("Settings", u"Deutsch", None))
        self.language_box.setItemText(3, QCoreApplication.translate("Settings", u"Fran\u00e7ais", None))

        self.backlight_label.setText(QCoreApplication.translate("Settings", u"Backlight", None))
        self.language_label.setText(QCoreApplication.translate("Settings", u"Language", None))
        self.confirm_box.setText(QCoreApplication.translate("Settings", u"Confirm memory state change", None))
        self.logo_box.setText(QCoreApplication.translate("Settings", u"Enable Boot Logo", None))
        self.restore_box.setText(QCoreApplication.translate("Settings", u"Restore state on boot", None))
        self.power_box.setText(QCoreApplication.translate("Settings", u"Power-on after power-loss", None))
        self.buzzer_box.setText(QCoreApplication.translate("Settings", u"Enable Buzzer", None))
        self.time_button.setText(QCoreApplication.translate("Settings", u"Sync Time", None))
    # retranslateUi

