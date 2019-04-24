# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inquiry.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Inquiry(object):
    def setupUi(self, Inquiry):
        Inquiry.setObjectName("Inquiry")
        Inquiry.resize(650, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Inquiry.sizePolicy().hasHeightForWidth())
        Inquiry.setSizePolicy(sizePolicy)
        Inquiry.setMinimumSize(QtCore.QSize(650, 700))
        Inquiry.setMaximumSize(QtCore.QSize(650, 99999))
        self.centralwidget = QtWidgets.QWidget(Inquiry)
        self.centralwidget.setObjectName("centralwidget")
        self.Note = QtWidgets.QLabel(self.centralwidget)
        self.Note.setGeometry(QtCore.QRect(40, 20, 501, 61))
        self.Note.setObjectName("Note")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(490, 650, 101, 31))
        self.Back.setObjectName("Back")
        self.Sure = QtWidgets.QPushButton(self.centralwidget)
        self.Sure.setGeometry(QtCore.QRect(380, 100, 101, 31))
        self.Sure.setObjectName("Sure")
        self.Names = QtWidgets.QLineEdit(self.centralwidget)
        self.Names.setGeometry(QtCore.QRect(40, 100, 321, 31))
        self.Names.setObjectName("Names")
        self.Warning = QtWidgets.QLabel(self.centralwidget)
        self.Warning.setGeometry(QtCore.QRect(40, 140, 221, 31))
        self.Warning.setStyleSheet("color: rgb(255, 0, 0);")
        self.Warning.setText("")
        self.Warning.setObjectName("Warning")
        self.Result = QtWidgets.QTextBrowser(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(40, 180, 550, 341))
        self.Result.setObjectName("Result")
        self.Fuzzy = QtWidgets.QPushButton(self.centralwidget)
        self.Fuzzy.setGeometry(QtCore.QRect(490, 100, 101, 31))
        self.Fuzzy.setObjectName("Fuzzy")
        self.Up_sort = QtWidgets.QPushButton(self.centralwidget)
        self.Up_sort.setGeometry(QtCore.QRect(370, 570, 101, 31))
        self.Up_sort.setObjectName("Up_sort")
        self.Down_sort = QtWidgets.QPushButton(self.centralwidget)
        self.Down_sort.setGeometry(QtCore.QRect(490, 570, 101, 31))
        self.Down_sort.setObjectName("Down_sort")
        self.Result_sum = QtWidgets.QLabel(self.centralwidget)
        self.Result_sum.setGeometry(QtCore.QRect(40, 530, 221, 31))
        self.Result_sum.setStyleSheet("")
        self.Result_sum.setText("")
        self.Result_sum.setObjectName("Result_sum")
        self.More_results = QtWidgets.QPushButton(self.centralwidget)
        self.More_results.setGeometry(QtCore.QRect(250, 570, 101, 31))
        self.More_results.setObjectName("More_results")
        Inquiry.setCentralWidget(self.centralwidget)

        self.retranslateUi(Inquiry)
        QtCore.QMetaObject.connectSlotsByName(Inquiry)

    def retranslateUi(self, Inquiry):
        _translate = QtCore.QCoreApplication.translate
        Inquiry.setWindowTitle(_translate("Inquiry", "Pricer"))
        self.Note.setText(_translate("Inquiry", "输入饰品名称（查询多个时用\";\"隔开）："))
        self.Back.setText(_translate("Inquiry", "Back"))
        self.Sure.setText(_translate("Inquiry", "精确查询"))
        self.Fuzzy.setText(_translate("Inquiry", "模糊查询"))
        self.Up_sort.setText(_translate("Inquiry", "价格升序"))
        self.Down_sort.setText(_translate("Inquiry", "价格降序"))
        self.More_results.setText(_translate("Inquiry", "加载更多"))

