# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_instant_translation.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Make_newWordBook = QtWidgets.QPushButton(self.centralwidget)
        self.Make_newWordBook.setGeometry(QtCore.QRect(100, 160, 181, 61))
        self.Make_newWordBook.setObjectName("Make_newWordBook")
        self.Tips = QtWidgets.QLabel(self.centralwidget)
        self.Tips.setGeometry(QtCore.QRect(100, 190, 191, 31))
        self.Tips.setText("")
        self.Tips.setObjectName("Tips")
        self.Translation_mode = QtWidgets.QPushButton(self.centralwidget)
        self.Translation_mode.setGeometry(QtCore.QRect(100, 70, 171, 61))
        self.Translation_mode.setObjectName("Translation_mode")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "I.T."))
        self.Make_newWordBook.setText(_translate("MainWindow", "生成生词本"))
        self.Translation_mode.setText(_translate("MainWindow", "翻译模式"))

