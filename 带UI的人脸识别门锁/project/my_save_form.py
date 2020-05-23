# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Save_ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(656, 646)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 551, 401))
        self.label.setObjectName("label")
        self.show_message = QtWidgets.QLabel(Form)
        self.show_message.setGeometry(QtCore.QRect(60, 500, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.show_message.setFont(font)
        self.show_message.setObjectName("show_message")
        self.name_editor = QtWidgets.QLineEdit(Form)
        self.name_editor.setGeometry(QtCore.QRect(320, 500, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.name_editor.setFont(font)
        self.name_editor.setObjectName("name_editor")
        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setGeometry(QtCore.QRect(150, 580, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.return_button = QtWidgets.QPushButton(Form)
        self.return_button.setGeometry(QtCore.QRect(380, 580, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "保存确认"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.show_message.setText(_translate("Form", "请输入名字:"))
        self.save_button.setText(_translate("Form", "保存"))
        self.return_button.setText(_translate("Form", "返回"))
