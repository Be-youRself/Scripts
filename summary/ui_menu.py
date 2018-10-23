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
        Menu.resize(800, 600)
        Menu.setMinimumSize(QtCore.QSize(800, 600))
        Menu.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.Today = QtWidgets.QPushButton(self.centralwidget)
        self.Today.setGeometry(QtCore.QRect(290, 350, 211, 31))
        self.Today.setObjectName("Today")
        self.Before = QtWidgets.QPushButton(self.centralwidget)
        self.Before.setGeometry(QtCore.QRect(290, 410, 211, 31))
        self.Before.setObjectName("Before")
        Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "MainWindow"))
        self.Today.setText(_translate("Menu", "记录今天"))
        self.Before.setText(_translate("Menu", "查看以前"))

