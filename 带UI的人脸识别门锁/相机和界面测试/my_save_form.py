# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myform.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Save_ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.save_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 1, 0, 1, 1)
        self.return_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save_button.setText(_translate("Form", "是否保存"))
        self.return_button.setText(_translate("Form", "返回"))
        self.label.setText(_translate("Form", ""))
