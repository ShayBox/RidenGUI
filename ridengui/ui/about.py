# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(173, 156)
        icon = QIcon()
        iconThemeName = u"riden"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        AboutDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(AboutDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(AboutDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.sourceLabel = QLabel(AboutDialog)
        self.sourceLabel.setObjectName(u"sourceLabel")
        self.sourceLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.sourceLabel, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.titleLabel = QLabel(AboutDialog)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.firmwareLabel = QLabel(AboutDialog)
        self.firmwareLabel.setObjectName(u"firmwareLabel")
        self.firmwareLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.firmwareLabel, 3, 0, 1, 1)


        self.retranslateUi(AboutDialog)
        self.buttonBox.accepted.connect(AboutDialog.accept)
        self.buttonBox.rejected.connect(AboutDialog.reject)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.sourceLabel.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p><a href=\"https://github.com/ShayBox/RidenGUI\"><span style=\" text-decoration: underline; color:#0057ae;\">RidenGUI Source Code </span></a></p></body></html>", None))
        self.titleLabel.setText(QCoreApplication.translate("AboutDialog", u"RidenGUI", None))
        self.firmwareLabel.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p><a href=\"https://eevblog.com/forum/testgear/ruideng-riden-rd6006-dc-power-supply\"><span style=\" text-decoration: underline; color:#0057ae;\">Custom Firmware</span></a></p></body></html>", None))
    # retranslateUi

