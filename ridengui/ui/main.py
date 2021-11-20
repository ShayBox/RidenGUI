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
        MainWindow.resize(852, 570)
        icon = QIcon()
        iconThemeName = u"riden"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../../../../opt/Batt-tools/RidenGUI/ridengui", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        self.action_general = QAction(MainWindow)
        self.action_general.setObjectName(u"action_general")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_serial = QAction(MainWindow)
        self.action_serial.setObjectName(u"action_serial")
        self.Action_Set_VI_ranges = QAction(MainWindow)
        self.Action_Set_VI_ranges.setObjectName(u"Action_Set_VI_ranges")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.gridLayout_3 = QGridLayout(self.central_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_3 = QFrame(self.central_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 0, 1, 1, 1)

        self.line_6 = QFrame(self.central_widget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(0, 12))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 3, 0, 1, 3)

        self.line = QFrame(self.central_widget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 12))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 3)

        self.line_5 = QFrame(self.central_widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 4, 1, 1, 1)

        self.output_layout = QVBoxLayout()
        self.output_layout.setSpacing(3)
        self.output_layout.setObjectName(u"output_layout")
        self.output_layout.setContentsMargins(3, 3, 3, 3)
        self.output_display = QGridLayout()
        self.output_display.setSpacing(3)
        self.output_display.setObjectName(u"output_display")
        self.output_display.setContentsMargins(3, 3, 3, 3)
        self.output_current = QLabel(self.central_widget)
        self.output_current.setObjectName(u"output_current")
        font = QFont()
        font.setFamily(u"DejaVu Sans Mono")
        font.setPointSize(36)
        self.output_current.setFont(font)
        self.output_current.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.output_current.setScaledContents(False)
        self.output_current.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.output_display.addWidget(self.output_current, 2, 0, 1, 1)

        self.output_voltage = QLabel(self.central_widget)
        self.output_voltage.setObjectName(u"output_voltage")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.output_voltage.sizePolicy().hasHeightForWidth())
        self.output_voltage.setSizePolicy(sizePolicy)
        self.output_voltage.setFont(font)
        self.output_voltage.setAutoFillBackground(False)
        self.output_voltage.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.output_voltage.setScaledContents(False)
        self.output_voltage.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.output_display.addWidget(self.output_voltage, 0, 0, 1, 1)

        self.output_voltage_label = QLabel(self.central_widget)
        self.output_voltage_label.setObjectName(u"output_voltage_label")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.output_voltage_label.setFont(font1)
        self.output_voltage_label.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.output_voltage_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.output_voltage_label.setMargin(5)

        self.output_display.addWidget(self.output_voltage_label, 0, 1, 1, 1)

        self.output_current_label = QLabel(self.central_widget)
        self.output_current_label.setObjectName(u"output_current_label")
        self.output_current_label.setFont(font1)
        self.output_current_label.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.output_current_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.output_current_label.setMargin(5)

        self.output_display.addWidget(self.output_current_label, 2, 1, 1, 1)

        self.vertical_spacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.output_display.addItem(self.vertical_spacer_2, 3, 0, 1, 2)

        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.output_display.addItem(self.vertical_spacer, 1, 0, 1, 2)

        self.output_power = QLabel(self.central_widget)
        self.output_power.setObjectName(u"output_power")
        self.output_power.setFont(font)
        self.output_power.setStyleSheet(u"color: rgb(255, 0, 255);")
        self.output_power.setScaledContents(False)
        self.output_power.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.output_display.addWidget(self.output_power, 4, 0, 2, 1)

        self.output_power_label = QLabel(self.central_widget)
        self.output_power_label.setObjectName(u"output_power_label")
        self.output_power_label.setFont(font1)
        self.output_power_label.setStyleSheet(u"color: rgb(255, 0, 255);")
        self.output_power_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.output_power_label.setMargin(5)
        self.output_power_label.setIndent(-1)

        self.output_display.addWidget(self.output_power_label, 4, 1, 2, 1)


        self.output_layout.addLayout(self.output_display)

        self.output_button = QPushButton(self.central_widget)
        self.output_button.setObjectName(u"output_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.output_button.sizePolicy().hasHeightForWidth())
        self.output_button.setSizePolicy(sizePolicy1)
        self.output_button.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setPointSize(12)
        self.output_button.setFont(font2)
        self.output_button.setCheckable(True)

        self.output_layout.addWidget(self.output_button)


        self.gridLayout_3.addLayout(self.output_layout, 0, 4, 7, 1)

        self.realtime_layout = QGridLayout()
        self.realtime_layout.setSpacing(3)
        self.realtime_layout.setObjectName(u"realtime_layout")
        self.realtime_layout.setContentsMargins(3, 3, 3, 3)
        self.realtime_box = QCheckBox(self.central_widget)
        self.realtime_box.setObjectName(u"realtime_box")
        self.realtime_box.setEnabled(True)
        self.realtime_box.setLayoutDirection(Qt.RightToLeft)

        self.realtime_layout.addWidget(self.realtime_box, 0, 1, 1, 1)

        self.horizontal_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.realtime_layout.addItem(self.horizontal_spacer_2, 0, 2, 1, 1)

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.realtime_layout.addItem(self.horizontal_spacer, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.realtime_layout, 2, 0, 1, 3)

        self.state_textual = QGridLayout()
        self.state_textual.setObjectName(u"state_textual")
        self.protection = QLabel(self.central_widget)
        self.protection.setObjectName(u"protection")
        self.protection.setFont(font2)
        self.protection.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.state_textual.addWidget(self.protection, 1, 1, 1, 1)

        self.keypad = QLabel(self.central_widget)
        self.keypad.setObjectName(u"keypad")
        self.keypad.setFont(font2)
        self.keypad.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.state_textual.addWidget(self.keypad, 0, 1, 1, 1)

        self.keypad_label = QLabel(self.central_widget)
        self.keypad_label.setObjectName(u"keypad_label")
        font3 = QFont()
        font3.setBold(False)
        font3.setWeight(50)
        self.keypad_label.setFont(font3)
        self.keypad_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.state_textual.addWidget(self.keypad_label, 0, 0, 1, 1)

        self.constant_label = QLabel(self.central_widget)
        self.constant_label.setObjectName(u"constant_label")
        self.constant_label.setFont(font3)
        self.constant_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.state_textual.addWidget(self.constant_label, 2, 0, 1, 1)

        self.constant = QLabel(self.central_widget)
        self.constant.setObjectName(u"constant")
        self.constant.setFont(font2)
        self.constant.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.state_textual.addWidget(self.constant, 2, 1, 1, 1)

        self.protection_label = QLabel(self.central_widget)
        self.protection_label.setObjectName(u"protection_label")
        self.protection_label.setFont(font3)
        self.protection_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.state_textual.addWidget(self.protection_label, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.state_textual, 0, 0, 1, 1)

        self.state_numeric = QGridLayout()
        self.state_numeric.setObjectName(u"state_numeric")
        self.state_numeric.setContentsMargins(-1, -1, 17, -1)
        self.input_voltage = QLabel(self.central_widget)
        self.input_voltage.setObjectName(u"input_voltage")
        self.input_voltage.setFont(font2)
        self.input_voltage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.state_numeric.addWidget(self.input_voltage, 2, 0, 1, 1)

        self.temp = QLabel(self.central_widget)
        self.temp.setObjectName(u"temp")
        self.temp.setFont(font2)
        self.temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.state_numeric.addWidget(self.temp, 1, 0, 1, 1)

        self.energy = QLabel(self.central_widget)
        self.energy.setObjectName(u"energy")
        self.energy.setFont(font2)
        self.energy.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.state_numeric.addWidget(self.energy, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.state_numeric, 0, 2, 1, 1)

        self.voltage_layout = QVBoxLayout()
        self.voltage_layout.setSpacing(3)
        self.voltage_layout.setObjectName(u"voltage_layout")
        self.voltage_layout.setContentsMargins(3, 3, 3, 3)
        self.v_set_label = QLabel(self.central_widget)
        self.v_set_label.setObjectName(u"v_set_label")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.v_set_label.setFont(font4)
        self.v_set_label.setAlignment(Qt.AlignCenter)
        self.v_set_label.setIndent(-1)

        self.voltage_layout.addWidget(self.v_set_label)

        self.voltage_steps_layout = QGridLayout()
        self.voltage_steps_layout.setObjectName(u"voltage_steps_layout")
        self.voltage_steps_layout.setHorizontalSpacing(3)
        self.voltage_steps_layout.setContentsMargins(3, 3, 3, 3)
        self.v_step_box = QComboBox(self.central_widget)
        self.v_step_box.setObjectName(u"v_step_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.v_step_box.sizePolicy().hasHeightForWidth())
        self.v_step_box.setSizePolicy(sizePolicy2)
        self.v_step_box.setEditable(False)

        self.voltage_steps_layout.addWidget(self.v_step_box, 1, 1, 1, 1)

        self.v_min_lab_2 = QLabel(self.central_widget)
        self.v_min_lab_2.setObjectName(u"v_min_lab_2")
        self.v_min_lab_2.setFont(font3)
        self.v_min_lab_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.voltage_steps_layout.addWidget(self.v_min_lab_2, 0, 0, 1, 1)

        self.v_max_lab_3 = QLabel(self.central_widget)
        self.v_max_lab_3.setObjectName(u"v_max_lab_3")
        self.v_max_lab_3.setFont(font3)
        self.v_max_lab_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.voltage_steps_layout.addWidget(self.v_max_lab_3, 0, 1, 1, 1)

        self.v_max_lab_2 = QLabel(self.central_widget)
        self.v_max_lab_2.setObjectName(u"v_max_lab_2")
        self.v_max_lab_2.setFont(font3)
        self.v_max_lab_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.voltage_steps_layout.addWidget(self.v_max_lab_2, 0, 2, 1, 1)

        self.v_min_box = QDoubleSpinBox(self.central_widget)
        self.v_min_box.setObjectName(u"v_min_box")
        self.v_min_box.setDecimals(1)
        self.v_min_box.setMaximum(62.000000000000000)

        self.voltage_steps_layout.addWidget(self.v_min_box, 1, 0, 1, 1)

        self.v_max_box = QDoubleSpinBox(self.central_widget)
        self.v_max_box.setObjectName(u"v_max_box")
        self.v_max_box.setDecimals(1)
        self.v_max_box.setMaximum(62.000000000000000)

        self.voltage_steps_layout.addWidget(self.v_max_box, 1, 2, 1, 1)


        self.voltage_layout.addLayout(self.voltage_steps_layout)

        self.v_set_dial = QDial(self.central_widget)
        self.v_set_dial.setObjectName(u"v_set_dial")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.v_set_dial.sizePolicy().hasHeightForWidth())
        self.v_set_dial.setSizePolicy(sizePolicy3)
        self.v_set_dial.setMinimumSize(QSize(150, 150))
        self.v_set_dial.setMaximum(10000)
        self.v_set_dial.setNotchTarget(100.000000000000000)
        self.v_set_dial.setNotchesVisible(True)

        self.voltage_layout.addWidget(self.v_set_dial)

        self.voltage_dial_layout = QHBoxLayout()
        self.voltage_dial_layout.setSpacing(3)
        self.voltage_dial_layout.setObjectName(u"voltage_dial_layout")
        self.voltage_dial_layout.setContentsMargins(3, 3, 3, 3)
        self.horizontal_spacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.voltage_dial_layout.addItem(self.horizontal_spacer_3)

        self.v_min_lab = QLabel(self.central_widget)
        self.v_min_lab.setObjectName(u"v_min_lab")
        self.v_min_lab.setFont(font2)
        self.v_min_lab.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.voltage_dial_layout.addWidget(self.v_min_lab)

        self.horizontal_spacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.voltage_dial_layout.addItem(self.horizontal_spacer_4)

        self.v_max_lab = QLabel(self.central_widget)
        self.v_max_lab.setObjectName(u"v_max_lab")
        self.v_max_lab.setFont(font2)
        self.v_max_lab.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.voltage_dial_layout.addWidget(self.v_max_lab)

        self.horizontal_spacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.voltage_dial_layout.addItem(self.horizontal_spacer_5)


        self.voltage_layout.addLayout(self.voltage_dial_layout)

        self.vertical_spacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.voltage_layout.addItem(self.vertical_spacer_3)

        self.voltage_set_layout = QHBoxLayout()
        self.voltage_set_layout.setObjectName(u"voltage_set_layout")
        self.voltage_set_layout.setContentsMargins(3, 3, 3, 3)
        self.v_set_spinbox = QDoubleSpinBox(self.central_widget)
        self.v_set_spinbox.setObjectName(u"v_set_spinbox")
        font5 = QFont()
        font5.setPointSize(16)
        self.v_set_spinbox.setFont(font5)
        self.v_set_spinbox.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.v_set_spinbox.setAlignment(Qt.AlignCenter)
        self.v_set_spinbox.setDecimals(4)
        self.v_set_spinbox.setMaximum(100.000000000000000)
        self.v_set_spinbox.setSingleStep(0.100000000000000)

        self.voltage_set_layout.addWidget(self.v_set_spinbox)

        self.v_set_button = QToolButton(self.central_widget)
        self.v_set_button.setObjectName(u"v_set_button")
        sizePolicy3.setHeightForWidth(self.v_set_button.sizePolicy().hasHeightForWidth())
        self.v_set_button.setSizePolicy(sizePolicy3)
        self.v_set_button.setFont(font5)

        self.voltage_set_layout.addWidget(self.v_set_button)


        self.voltage_layout.addLayout(self.voltage_set_layout)


        self.gridLayout_3.addLayout(self.voltage_layout, 4, 0, 1, 1)

        self.current_layout = QVBoxLayout()
        self.current_layout.setSpacing(3)
        self.current_layout.setObjectName(u"current_layout")
        self.current_layout.setContentsMargins(3, 3, 3, 3)
        self.i_set_label = QLabel(self.central_widget)
        self.i_set_label.setObjectName(u"i_set_label")
        self.i_set_label.setFont(font4)
        self.i_set_label.setAlignment(Qt.AlignCenter)

        self.current_layout.addWidget(self.i_set_label)

        self.current_steps_layout = QGridLayout()
        self.current_steps_layout.setObjectName(u"current_steps_layout")
        self.current_steps_layout.setHorizontalSpacing(3)
        self.current_steps_layout.setContentsMargins(3, 3, 3, 3)
        self.i_step_box = QComboBox(self.central_widget)
        self.i_step_box.setObjectName(u"i_step_box")
        sizePolicy2.setHeightForWidth(self.i_step_box.sizePolicy().hasHeightForWidth())
        self.i_step_box.setSizePolicy(sizePolicy2)
        self.i_step_box.setEditable(False)

        self.current_steps_layout.addWidget(self.i_step_box, 1, 1, 1, 1)

        self.v_max_lab_4 = QLabel(self.central_widget)
        self.v_max_lab_4.setObjectName(u"v_max_lab_4")
        self.v_max_lab_4.setFont(font3)
        self.v_max_lab_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.current_steps_layout.addWidget(self.v_max_lab_4, 0, 2, 1, 1)

        self.v_max_lab_5 = QLabel(self.central_widget)
        self.v_max_lab_5.setObjectName(u"v_max_lab_5")
        self.v_max_lab_5.setFont(font3)
        self.v_max_lab_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.current_steps_layout.addWidget(self.v_max_lab_5, 0, 1, 1, 1)

        self.v_min_lab_3 = QLabel(self.central_widget)
        self.v_min_lab_3.setObjectName(u"v_min_lab_3")
        self.v_min_lab_3.setFont(font3)
        self.v_min_lab_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.current_steps_layout.addWidget(self.v_min_lab_3, 0, 0, 1, 1)

        self.i_max_box = QDoubleSpinBox(self.central_widget)
        self.i_max_box.setObjectName(u"i_max_box")
        self.i_max_box.setDecimals(1)
        self.i_max_box.setMaximum(19.000000000000000)

        self.current_steps_layout.addWidget(self.i_max_box, 1, 2, 1, 1)

        self.i_min_box = QDoubleSpinBox(self.central_widget)
        self.i_min_box.setObjectName(u"i_min_box")
        self.i_min_box.setDecimals(1)

        self.current_steps_layout.addWidget(self.i_min_box, 1, 0, 1, 1)


        self.current_layout.addLayout(self.current_steps_layout)

        self.i_set_dial = QDial(self.central_widget)
        self.i_set_dial.setObjectName(u"i_set_dial")
        sizePolicy3.setHeightForWidth(self.i_set_dial.sizePolicy().hasHeightForWidth())
        self.i_set_dial.setSizePolicy(sizePolicy3)
        self.i_set_dial.setMinimumSize(QSize(150, 150))
        self.i_set_dial.setMaximum(10000)
        self.i_set_dial.setNotchTarget(100.000000000000000)
        self.i_set_dial.setNotchesVisible(True)

        self.current_layout.addWidget(self.i_set_dial)

        self.current_dial_layout = QHBoxLayout()
        self.current_dial_layout.setSpacing(3)
        self.current_dial_layout.setObjectName(u"current_dial_layout")
        self.current_dial_layout.setContentsMargins(3, 3, 3, 3)
        self.horizontal_spacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.current_dial_layout.addItem(self.horizontal_spacer_6)

        self.i_min_lab = QLabel(self.central_widget)
        self.i_min_lab.setObjectName(u"i_min_lab")
        self.i_min_lab.setFont(font2)
        self.i_min_lab.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.current_dial_layout.addWidget(self.i_min_lab, 0, Qt.AlignVCenter)

        self.horizontal_spacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.current_dial_layout.addItem(self.horizontal_spacer_7)

        self.i_max_lab = QLabel(self.central_widget)
        self.i_max_lab.setObjectName(u"i_max_lab")
        self.i_max_lab.setFont(font2)
        self.i_max_lab.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.current_dial_layout.addWidget(self.i_max_lab)

        self.horizontal_spacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.current_dial_layout.addItem(self.horizontal_spacer_8)


        self.current_layout.addLayout(self.current_dial_layout)

        self.vertical_spacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.current_layout.addItem(self.vertical_spacer_4)

        self.current_set_layout = QHBoxLayout()
        self.current_set_layout.setObjectName(u"current_set_layout")
        self.current_set_layout.setContentsMargins(3, 3, 3, 3)
        self.i_set_spinbox = QDoubleSpinBox(self.central_widget)
        self.i_set_spinbox.setObjectName(u"i_set_spinbox")
        self.i_set_spinbox.setFont(font5)
        self.i_set_spinbox.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.i_set_spinbox.setAlignment(Qt.AlignCenter)
        self.i_set_spinbox.setDecimals(4)
        self.i_set_spinbox.setMaximum(100.000000000000000)
        self.i_set_spinbox.setSingleStep(0.100000000000000)

        self.current_set_layout.addWidget(self.i_set_spinbox)

        self.i_set_button = QToolButton(self.central_widget)
        self.i_set_button.setObjectName(u"i_set_button")
        sizePolicy3.setHeightForWidth(self.i_set_button.sizePolicy().hasHeightForWidth())
        self.i_set_button.setSizePolicy(sizePolicy3)
        self.i_set_button.setFont(font5)

        self.current_set_layout.addWidget(self.i_set_button)


        self.current_layout.addLayout(self.current_set_layout)


        self.gridLayout_3.addLayout(self.current_layout, 4, 2, 1, 1)

        self.line_2 = QFrame(self.central_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 0, 3, 6, 1)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 852, 30))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.v_set_label.setBuddy(self.v_set_dial)
        self.i_set_label.setBuddy(self.i_set_dial)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.v_set_dial, self.i_set_dial)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_quit)
        self.menu_settings.addAction(self.action_general)
        self.menu_settings.addAction(self.action_serial)
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RidenGUI", None))
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.action_general.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_serial.setText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.Action_Set_VI_ranges.setText(QCoreApplication.translate("MainWindow", u"Set GUI V/I limits", None))
        self.output_current.setText(QCoreApplication.translate("MainWindow", u"00.0000", None))
        self.output_voltage.setText(QCoreApplication.translate("MainWindow", u"00.000", None))
        self.output_voltage_label.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.output_current_label.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.output_power.setText(QCoreApplication.translate("MainWindow", u"00.000", None))
        self.output_power_label.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.output_button.setText("")
        self.realtime_box.setText(QCoreApplication.translate("MainWindow", u"Apply V/I changes in realtime", None))
        self.protection.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.keypad.setText(QCoreApplication.translate("MainWindow", u"Unlocked", None))
        self.keypad_label.setText(QCoreApplication.translate("MainWindow", u"Keypad Lock", None))
        self.constant_label.setText(QCoreApplication.translate("MainWindow", u"CC/CV Status", None))
        self.constant.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.protection_label.setText(QCoreApplication.translate("MainWindow", u"Protection Status", None))
        self.input_voltage.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.temp.setText(QCoreApplication.translate("MainWindow", u"00.00\u00b0C | 00.00\u00b0F", None))
        self.energy.setText(QCoreApplication.translate("MainWindow", u"00.00 Ah | 00.00 Wh", None))
        self.v_set_label.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.v_step_box.setCurrentText("")
        self.v_min_lab_2.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.v_max_lab_3.setText(QCoreApplication.translate("MainWindow", u"step", None))
        self.v_max_lab_2.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.v_min_lab.setText(QCoreApplication.translate("MainWindow", u"v_min", None))
        self.v_max_lab.setText(QCoreApplication.translate("MainWindow", u"v_max", None))
        self.v_set_button.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.i_set_label.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.i_step_box.setCurrentText("")
        self.v_max_lab_4.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.v_max_lab_5.setText(QCoreApplication.translate("MainWindow", u"step", None))
        self.v_min_lab_3.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.i_min_lab.setText(QCoreApplication.translate("MainWindow", u"i_min", None))
        self.i_max_lab.setText(QCoreApplication.translate("MainWindow", u"i_max", None))
        self.i_set_button.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_settings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

