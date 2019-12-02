# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_loginbox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Loginbox(object):
    def setupUi(self, Loginbox):
        Loginbox.setObjectName("Loginbox")
        Loginbox.resize(501, 321)
        Loginbox.setMinimumSize(QtCore.QSize(501, 321))
        Loginbox.setMaximumSize(QtCore.QSize(501, 321))
        Loginbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Loginbox)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_ID = QtWidgets.QLabel(self.centralwidget)
        self.Label_ID.setGeometry(QtCore.QRect(40, 60, 141, 71))
        self.Label_ID.setStyleSheet("font: 12pt \"华文楷体\";")
        self.Label_ID.setObjectName("Label_ID")
        self.Label_Key = QtWidgets.QLabel(self.centralwidget)
        self.Label_Key.setGeometry(QtCore.QRect(40, 110, 221, 91))
        self.Label_Key.setStyleSheet("font: 12pt \"华文楷体\";")
        self.Label_Key.setObjectName("Label_Key")
        self.Button_Finsh = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Finsh.setGeometry(QtCore.QRect(40, 240, 171, 51))
        self.Button_Finsh.setStyleSheet("font: 12pt \"华文楷体\";\n"
                                        "border-color: rgb(255, 255, 255);")
        self.Button_Finsh.setObjectName("Button_Finsh")
        self.Button_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Exit.setGeometry(QtCore.QRect(470, 0, 31, 31))
        self.Button_Exit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "color: rgb(255, 255, 255);")
        self.Button_Exit.setObjectName("Button_Exit")
        self.Input_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_ID.setGeometry(QtCore.QRect(160, 70, 301, 41))
        self.Input_ID.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.Input_ID.setObjectName("Input_ID")
        self.Input_key = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_key.setGeometry(QtCore.QRect(160, 130, 301, 41))
        self.Input_key.setObjectName("Input_key")
        self.Button_guide = QtWidgets.QPushButton(self.centralwidget)
        self.Button_guide.setGeometry(QtCore.QRect(290, 240, 171, 51))
        self.Button_guide.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                        "font: 12pt \"华文楷体\";")
        self.Button_guide.setObjectName("Button_guide")
        self.Tips = QtWidgets.QLabel(self.centralwidget)
        self.Tips.setGeometry(QtCore.QRect(120, 190, 411, 31))
        self.Tips.setStyleSheet("color: rgb(255, 0, 0);\n"
                                "font: 10pt \"华文楷体\";")
        self.Tips.setText("")
        self.Tips.setObjectName("Tips")
        Loginbox.setCentralWidget(self.centralwidget)

        self.retranslateUi(Loginbox)
        QtCore.QMetaObject.connectSlotsByName(Loginbox)

    def retranslateUi(self, Loginbox):
        _translate = QtCore.QCoreApplication.translate
        Loginbox.setWindowTitle(_translate("Loginbox", "MainWindow"))
        self.Label_ID.setText(_translate("Loginbox", "应用 ID"))
        self.Label_Key.setText(_translate("Loginbox", "应用密钥"))
        self.Button_Finsh.setText(_translate("Loginbox", "确 定"))
        self.Button_Exit.setText(_translate("Loginbox", "×"))
        self.Button_guide.setText(_translate("Loginbox", "注 册"))
