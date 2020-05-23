# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1124, 700)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 831, 621))
        self.label.setObjectName("label")
        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setGeometry(QtCore.QRect(960, 540, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.message = QtWidgets.QLabel(Form)
        self.message.setGeometry(QtCore.QRect(970, 90, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.message.setFont(font)
        self.message.setObjectName("message")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "门禁系统"))
        self.label.setText(_translate("Form", " "))
        self.save_button.setText(_translate("Form", "增加成员"))
        self.message.setText(_translate("Form", "欢迎^_^"))
