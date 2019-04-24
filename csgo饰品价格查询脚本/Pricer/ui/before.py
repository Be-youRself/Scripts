# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'before.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Before(object):
    def setupUi(self, Before):
        Before.setObjectName("Before")
        Before.resize(800, 710)
        self.centralwidget = QtWidgets.QWidget(Before)
        self.centralwidget.setObjectName("centralwidget")
        self.Details = QtWidgets.QTextBrowser(self.centralwidget)
        self.Details.setGeometry(QtCore.QRect(110, 130, 550, 341))
        self.Details.setObjectName("Details")
        self.Names = QtWidgets.QComboBox(self.centralwidget)
        self.Names.setGeometry(QtCore.QRect(120, 70, 291, 22))
        self.Names.setObjectName("Names")
        Before.setCentralWidget(self.centralwidget)

        self.retranslateUi(Before)
        QtCore.QMetaObject.connectSlotsByName(Before)

    def retranslateUi(self, Before):
        _translate = QtCore.QCoreApplication.translate
        Before.setWindowTitle(_translate("Before", "Pricer"))

