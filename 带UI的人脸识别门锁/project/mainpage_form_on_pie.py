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
        Form.resize(950, 500)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 700, 470))
        self.label.setObjectName("label")
        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setGeometry(QtCore.QRect(760, 130, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.message = QtWidgets.QLabel(Form)
        self.message.setGeometry(QtCore.QRect(750, 40, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.message.setFont(font)
        self.message.setObjectName("message")
        self.unlock_button = QtWidgets.QPushButton(Form)
        self.unlock_button.setGeometry(QtCore.QRect(760, 220, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        self.unlock_button.setFont(font)
        self.unlock_button.setObjectName("unlock_button")
        self.delete_button = QtWidgets.QPushButton(Form)
        self.delete_button.setGeometry(QtCore.QRect(760, 310, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.code_box_button = QtWidgets.QPushButton(Form)
        self.code_box_button.setGeometry(QtCore.QRect(760, 400, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        self.code_box_button.setFont(font)
        self.code_box_button.setObjectName("code_box_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "门禁系统"))
        self.label.setText(_translate("Form", " "))
        self.save_button.setText(_translate("Form", "增加成员"))
        self.message.setText(_translate("Form", "欢迎^_^"))
        self.unlock_button.setText(_translate("Form", "点此开锁"))
        self.delete_button.setText(_translate("Form", "删减成员"))
        self.code_box_button.setText(_translate("Form", "密码开锁"))
