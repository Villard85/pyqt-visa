# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphs.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class graph_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(214, 381)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.g1xcombo = QtWidgets.QComboBox(self.groupBox)
        self.g1xcombo.setObjectName("g1xcombo")
        self.gridLayout.addWidget(self.g1xcombo, 1, 0, 1, 1)
        self.g1xscale = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.g1xscale.setDecimals(5)
        self.g1xscale.setMaximum(1000000.0)
        self.g1xscale.setProperty("value", 1.0)
        self.g1xscale.setObjectName("g1xscale")
        self.gridLayout.addWidget(self.g1xscale, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.g1ycombo = QtWidgets.QComboBox(self.groupBox)
        self.g1ycombo.setObjectName("g1ycombo")
        self.gridLayout.addWidget(self.g1ycombo, 3, 0, 1, 1)
        self.g1yscale = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.g1yscale.setDecimals(5)
        self.g1yscale.setMaximum(1000000.0)
        self.g1yscale.setProperty("value", 1.0)
        self.g1yscale.setObjectName("g1yscale")
        self.gridLayout.addWidget(self.g1yscale, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 1, 1, 1)
        self.g2xcombo = QtWidgets.QComboBox(self.groupBox_2)
        self.g2xcombo.setObjectName("g2xcombo")
        self.gridLayout_2.addWidget(self.g2xcombo, 1, 0, 1, 1)
        self.g2xscale = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.g2xscale.setDecimals(5)
        self.g2xscale.setMaximum(1000000.0)
        self.g2xscale.setProperty("value", 1.0)
        self.g2xscale.setObjectName("g2xscale")
        self.gridLayout_2.addWidget(self.g2xscale, 1, 1, 1, 1)
        self.g2ycombo = QtWidgets.QComboBox(self.groupBox_2)
        self.g2ycombo.setObjectName("g2ycombo")
        self.gridLayout_2.addWidget(self.g2ycombo, 3, 0, 1, 1)
        self.g2yscale = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.g2yscale.setDecimals(5)
        self.g2yscale.setMaximum(1000000.0)
        self.g2yscale.setProperty("value", 1.0)
        self.g2yscale.setObjectName("g2yscale")
        self.gridLayout_2.addWidget(self.g2yscale, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)
        self.g3xcombo = QtWidgets.QComboBox(self.groupBox_3)
        self.g3xcombo.setObjectName("g3xcombo")
        self.gridLayout_3.addWidget(self.g3xcombo, 1, 0, 1, 1)
        self.g3xscale = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.g3xscale.setDecimals(5)
        self.g3xscale.setMaximum(1000000.0)
        self.g3xscale.setProperty("value", 1.0)
        self.g3xscale.setObjectName("g3xscale")
        self.gridLayout_3.addWidget(self.g3xscale, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 2, 1, 1, 1)
        self.g3ycombo = QtWidgets.QComboBox(self.groupBox_3)
        self.g3ycombo.setObjectName("g3ycombo")
        self.gridLayout_3.addWidget(self.g3ycombo, 3, 0, 1, 1)
        self.g3yscale = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.g3yscale.setDecimals(5)
        self.g3yscale.setMaximum(1000000.0)
        self.g3yscale.setProperty("value", 1.0)
        self.g3yscale.setObjectName("g3yscale")
        self.gridLayout_3.addWidget(self.g3yscale, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Graph #1 settings"))
        self.label_3.setText(_translate("Dialog", "X-variable"))
        self.label.setText(_translate("Dialog", "X-scale"))
        self.label_4.setText(_translate("Dialog", "Y-variable"))
        self.label_2.setText(_translate("Dialog", "Y-scale"))
        self.groupBox_2.setTitle(_translate("Dialog", "Graph #2 settings"))
        self.label_10.setText(_translate("Dialog", "Y-variable"))
        self.label_11.setText(_translate("Dialog", "Y-scale"))
        self.label_7.setText(_translate("Dialog", "X-variable"))
        self.label_8.setText(_translate("Dialog", "X-scale"))
        self.groupBox_3.setTitle(_translate("Dialog", "Graph #3 settings"))
        self.label_13.setText(_translate("Dialog", "X-variable"))
        self.label_14.setText(_translate("Dialog", "X-scale"))
        self.label_16.setText(_translate("Dialog", "Y-variable"))
        self.label_17.setText(_translate("Dialog", "Y-scale"))

class graphDialog(QtWidgets.QDialog, graph_Ui_Dialog):
	def __init__(self):
		super(graphDialog, self).__init__()
		self.setupUi(self)
		
		# self.okBtn.clicked.connect(self.accept)
		# self.cancelBtn.clicked.connect(self.reject)
		
