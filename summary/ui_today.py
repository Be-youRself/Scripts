# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'today.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Today(object):
    def setupUi(self, Today):
        Today.setObjectName("Today")
        Today.resize(800, 600)
        Today.setMinimumSize(QtCore.QSize(800, 600))
        Today.setMaximumSize(QtCore.QSize(800, 600))
        self.Note = QtWidgets.QLabel(Today)
        self.Note.setGeometry(QtCore.QRect(120, 40, 161, 61))
        self.Note.setObjectName("Note")

        self.retranslateUi(Today)
        QtCore.QMetaObject.connectSlotsByName(Today)

    def retranslateUi(self, Today):
        _translate = QtCore.QCoreApplication.translate
        Today.setWindowTitle(_translate("Today", "Form"))
        self.Note.setText(_translate("Today", "记录今日"))

