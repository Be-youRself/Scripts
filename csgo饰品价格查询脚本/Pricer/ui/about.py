# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(490, 256)
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 531, 41))
        self.label.setStyleSheet("font: 16pt \"华文行楷\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 511, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 461, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 150, 451, 16))
        self.label_4.setObjectName("label_4")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(180, 200, 101, 31))
        self.Back.setObjectName("Back")
        About.setCentralWidget(self.centralwidget)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Pricer"))
        self.label.setText(_translate("About", "★CSGO饰品价格查询软件★"))
        self.label_2.setText(_translate("About", "本软件用于查询并且比对igxe网站上csgo饰品售价"))
        self.label_3.setText(_translate("About", "仅供个人查询使用，不得用于商业用途！"))
        self.label_4.setText(_translate("About", "更多请联系作者QQ：1090671860"))
        self.Back.setText(_translate("About", "Back"))

