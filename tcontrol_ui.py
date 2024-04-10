# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'py-tcontrol.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(Dialog.minimumSizeHint())
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.scanButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scanButton.setFont(font)
        self.scanButton.setObjectName("scanButton")
        self.gridLayout_2.addWidget(self.scanButton, 1, 0, 1, 1)
        self.instrList = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.instrList.setFont(font)
        self.instrList.setObjectName("instrList")
        self.gridLayout_2.addWidget(self.instrList, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.getButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.getButton.setFont(font)
        self.getButton.setObjectName("getButton")
        self.gridLayout_3.addWidget(self.getButton, 1, 0, 1, 1)
        self.ConfigBox = QtWidgets.QTextEdit(Dialog)
        self.ConfigBox.setObjectName("ConfigBox")
        self.gridLayout_3.addWidget(self.ConfigBox, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.setpUpd = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setpUpd.setFont(font)
        self.setpUpd.setObjectName("setpUpd")
        self.verticalLayout_3.addWidget(self.setpUpd)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.setpSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.setpSpin.setObjectName("setpSpin")
        self.setpSpin.setMinimum(0)
        self.setpSpin.setMinimum(350)
        self.verticalLayout_3.addWidget(self.setpSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rampUpd = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rampUpd.setFont(font)
        self.rampUpd.setObjectName("rampUpd")
        self.verticalLayout_4.addWidget(self.rampUpd)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.rampSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.rampSpin.setObjectName("rampSpin")
        self.rampSpin.setMinimum(0)
        self.rampSpin.setMaximum(20)
        self.verticalLayout_4.addWidget(self.rampSpin)
        self.rampSwitch = QtWidgets.QCheckBox(self.groupBox)
        self.rampSwitch.setObjectName("rampSwitch")
        self.verticalLayout_4.addWidget(self.rampSwitch)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.heaterCombo = QtWidgets.QLabel(self.groupBox_2)
        self.heaterCombo.setObjectName("heaterCombo")
        self.gridLayout_4.addWidget(self.heaterCombo, 1, 0, 1, 1)
        self.hrangeCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.hrangeCombo.setObjectName("hrangeCombo")
        self.gridLayout_4.addWidget(self.hrangeCombo, 2, 0, 1, 1)
        self.heaterUpd = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.heaterUpd.setFont(font)
        self.heaterUpd.setObjectName("heaterUpd")
        self.gridLayout_4.addWidget(self.heaterUpd, 0, 0, 1, 1)
        self.analogSpin = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.analogSpin.setObjectName("analogSpin")
        self.analogSpin.setMinimum(0)
        self.analogSpin.setMaximum(100)
        self.gridLayout_4.addWidget(self.analogSpin, 12, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 11, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 1, 1, 1)
        self.houtSpin = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.houtSpin.setObjectName("houtSpin")
        self.gridLayout_4.addWidget(self.houtSpin, 2, 1, 1, 1)
        self.loopCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.loopCombo.setObjectName("loopCombo")
        self.gridLayout_4.addWidget(self.loopCombo, 8, 1, 1, 1)
        self.analogUpd = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.analogUpd.setFont(font)
        self.analogUpd.setObjectName("analogUpd")
        self.gridLayout_4.addWidget(self.analogUpd, 10, 0, 1, 1)
        self.analogCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.analogCombo.setObjectName("analogCombo")
        self.gridLayout_4.addWidget(self.analogCombo, 12, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 11, 1, 1, 1)
        self.powerSwitch = QtWidgets.QCheckBox(self.groupBox_2)
        self.powerSwitch.setObjectName("powerSwitch")
        self.gridLayout_4.addWidget(self.powerSwitch, 8, 0, 1, 1)
        self.hoffBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.hoffBtn.setObjectName("hoffBtn")
        self.gridLayout_4.addWidget(self.hoffBtn, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 5, 0, 1, 1)
        self.setResBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.setResBtn.setObjectName("setResBtn")
        self.gridLayout_4.addWidget(self.setResBtn, 6, 1, 1, 1)
        self.hResSpin = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.hResSpin.setObjectName("hResSpin")
        self.hResSpin.setMinimum(1)
        self.hResSpin.setMaximum(10000)
        self.gridLayout_4.addWidget(self.hResSpin, 6, 0, 1, 1)
        self.loopLabel = QtWidgets.QLabel(self.groupBox_2)
        self.loopLabel.setObjectName("loopLabel")
        self.gridLayout_4.addWidget(self.loopLabel, 7, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 2, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName("formLayout")
        self.prunBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.prunBtn.setObjectName("prunBtn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.prunBtn)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.ptermBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.ptermBtn.setObjectName("ptermBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ptermBtn)
        self.programCombo = QtWidgets.QComboBox(self.groupBox_3)
        self.programCombo.setObjectName("programCombo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.programCombo)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.messageLabel.setFont(font)
        self.messageLabel.setObjectName("messageLabel")
        self.verticalLayout.addWidget(self.messageLabel)
        self.messageBox = QtWidgets.QTextEdit(Dialog)
        self.messageBox.setObjectName("messageBox")
        self.verticalLayout.addWidget(self.messageBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.exitButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_2.addWidget(self.exitButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lakecontrol"))
        self.label.setText(_translate("Dialog", "Instrument List"))
        self.scanButton.setText(_translate("Dialog", "Scan for Lakeshores"))
        self.label_2.setText(_translate("Dialog", "Current instrument configuration"))
        self.getButton.setText(_translate("Dialog", "Get Current State"))
        self.groupBox.setTitle(_translate("Dialog", "Setpoint config"))
        self.setpUpd.setText(_translate("Dialog", "Update Setpoint"))
        self.label_3.setText(_translate("Dialog", "Current Setpoint [K]"))
        self.rampUpd.setText(_translate("Dialog", "Update Ramp"))
        self.label_5.setText(_translate("Dialog", "Ramp value [K/min]"))
        self.rampSwitch.setText(_translate("Dialog", "Ramp ON"))
        self.groupBox_2.setTitle(_translate("Dialog", "Heater config"))
        self.heaterCombo.setText(_translate("Dialog", "Heater Range"))
        self.heaterUpd.setText(_translate("Dialog", "Update Heater Settings"))
        self.label_8.setText(_translate("Dialog", "Analog Output [%]"))
        self.label_4.setText(_translate("Dialog", "Heater output [%]"))
        self.analogUpd.setText(_translate("Dialog", "Update AnalogOutput"))
        self.label_9.setText(_translate("Dialog", "Analog Channel"))
        self.powerSwitch.setText(_translate("Dialog", "Powerup Enable"))
        self.hoffBtn.setText(_translate("Dialog", "Heater off"))
        self.label_6.setText(_translate("Dialog", "Heater resistance"))
        self.setResBtn.setText(_translate("Dialog", "Set heater resistance"))
        self.loopLabel.setText(_translate("Dialog", "Control Loop"))
        self.groupBox_3.setTitle(_translate("Dialog", "Program settings"))
        self.prunBtn.setText(_translate("Dialog", "Run program"))
        self.label_7.setText(_translate("Dialog", "Program number"))
        self.ptermBtn.setText(_translate("Dialog", "Terminate program"))
        self.messageLabel.setText(_translate("Dialog", "Message Box"))
        self.exitButton.setText(_translate("Dialog", "Exit"))
