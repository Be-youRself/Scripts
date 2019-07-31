# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(449, 304)
        About.setMinimumSize(QtCore.QSize(449, 304))
        About.setMaximumSize(QtCore.QSize(449, 304))
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 80, 291, 131))
        self.label.setStyleSheet("font: 16pt \"华文楷体\";")
        self.label.setObjectName("label")
        About.setCentralWidget(self.centralwidget)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "进程调度系统"))
        self.label.setText(_translate("About", "进程调度系统 V 1.0.0"))

