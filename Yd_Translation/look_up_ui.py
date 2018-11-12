# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'look_up.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Look_up(object):
    def setupUi(self, Look_up):
        Look_up.setObjectName("Look_up")
        Look_up.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Look_up)
        self.centralwidget.setObjectName("centralwidget")
        self.Word = QtWidgets.QLabel(self.centralwidget)
        self.Word.setGeometry(QtCore.QRect(130, 130, 531, 91))
        self.Word.setText("")
        self.Word.setObjectName("Word")
        self.Explanation = QtWidgets.QLabel(self.centralwidget)
        self.Explanation.setGeometry(QtCore.QRect(70, 390, 621, 91))
        self.Explanation.setText("")
        self.Explanation.setObjectName("Explanation")
        self.Check = QtWidgets.QPushButton(self.centralwidget)
        self.Check.setGeometry(QtCore.QRect(330, 280, 93, 28))
        self.Check.setObjectName("Check")
        Look_up.setCentralWidget(self.centralwidget)

        self.retranslateUi(Look_up)
        QtCore.QMetaObject.connectSlotsByName(Look_up)

    def retranslateUi(self, Look_up):
        _translate = QtCore.QCoreApplication.translate
        Look_up.setWindowTitle(_translate("Look_up", "Look_up"))
        self.Check.setText(_translate("Look_up", "Meaning"))

