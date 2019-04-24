# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(350, 600)
        Menu.setMinimumSize(QtCore.QSize(350, 600))
        Menu.setMaximumSize(QtCore.QSize(350, 600))
        Menu.setStyleSheet("")
        Menu.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.Inquiry = QtWidgets.QPushButton(self.centralwidget)
        self.Inquiry.setGeometry(QtCore.QRect(65, 360, 220, 40))
        self.Inquiry.setObjectName("Inquiry")
        self.Before = QtWidgets.QPushButton(self.centralwidget)
        self.Before.setGeometry(QtCore.QRect(65, 425, 220, 40))
        self.Before.setObjectName("Before")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(80, 260, 220, 60))
        self.Title.setStyleSheet("font: 40pt \"华文隶书\";\n"
"background: transparent;")
        self.Title.setObjectName("Title")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(55, 40, 230, 210))
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.About = QtWidgets.QPushButton(self.centralwidget)
        self.About.setGeometry(QtCore.QRect(65, 490, 220, 40))
        self.About.setObjectName("About")
        Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Pricer"))
        self.Inquiry.setText(_translate("Menu", "查询价格"))
        self.Before.setText(_translate("Menu", "历史价格"))
        self.Title.setText(_translate("Menu", "Pricer"))
        self.About.setText(_translate("Menu", "关于"))

