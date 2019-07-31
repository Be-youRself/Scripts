# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createProcess_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateProcess(object):
    def setupUi(self, CreateProcess):
        CreateProcess.setObjectName("CreateProcess")
        CreateProcess.resize(415, 387)
        CreateProcess.setMinimumSize(QtCore.QSize(415, 387))
        CreateProcess.setMaximumSize(QtCore.QSize(415, 387))
        self.centralwidget = QtWidgets.QWidget(CreateProcess)
        self.centralwidget.setObjectName("centralwidget")
        self.Restart = QtWidgets.QPushButton(self.centralwidget)
        self.Restart.setGeometry(QtCore.QRect(220, 260, 150, 60))
        self.Restart.setObjectName("Restart")
        self.ReadResult = QtWidgets.QLabel(self.centralwidget)
        self.ReadResult.setGeometry(QtCore.QRect(50, 40, 391, 41))
        self.ReadResult.setText("")
        self.ReadResult.setObjectName("ReadResult")
        self.L1 = QtWidgets.QLabel(self.centralwidget)
        self.L1.setGeometry(QtCore.QRect(50, 105, 181, 41))
        self.L1.setObjectName("L1")
        self.FreeNum = QtWidgets.QLabel(self.centralwidget)
        self.FreeNum.setGeometry(QtCore.QRect(230, 105, 181, 41))
        self.FreeNum.setText("")
        self.FreeNum.setObjectName("FreeNum")
        self.L2 = QtWidgets.QLabel(self.centralwidget)
        self.L2.setGeometry(QtCore.QRect(50, 170, 181, 41))
        self.L2.setObjectName("L2")
        self.ProcessNum = QtWidgets.QComboBox(self.centralwidget)
        self.ProcessNum.setGeometry(QtCore.QRect(230, 170, 100, 40))
        self.ProcessNum.setObjectName("ProcessNum")
        self.Sure = QtWidgets.QPushButton(self.centralwidget)
        self.Sure.setGeometry(QtCore.QRect(40, 260, 150, 60))
        self.Sure.setObjectName("Sure")
        CreateProcess.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateProcess)
        QtCore.QMetaObject.connectSlotsByName(CreateProcess)

    def retranslateUi(self, CreateProcess):
        _translate = QtCore.QCoreApplication.translate
        CreateProcess.setWindowTitle(_translate("CreateProcess", "进程调度系统"))
        self.Restart.setText(_translate("CreateProcess", "返回主菜单"))
        self.L1.setText(_translate("CreateProcess", "空闲队列资源个数："))
        self.L2.setText(_translate("CreateProcess", "创建进程个数"))
        self.Sure.setText(_translate("CreateProcess", "确认"))

