# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputPara_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InputPara(object):
    def setupUi(self, InputPara):
        InputPara.setObjectName("InputPara")
        InputPara.resize(492, 646)
        InputPara.setMinimumSize(QtCore.QSize(492, 646))
        InputPara.setMaximumSize(QtCore.QSize(492, 646))
        self.centralwidget = QtWidgets.QWidget(InputPara)
        self.centralwidget.setObjectName("centralwidget")
        self.Warning = QtWidgets.QLabel(self.centralwidget)
        self.Warning.setGeometry(QtCore.QRect(50, 30, 711, 51))
        self.Warning.setText("")
        self.Warning.setObjectName("Warning")
        self.Restart = QtWidgets.QPushButton(self.centralwidget)
        self.Restart.setGeometry(QtCore.QRect(260, 510, 150, 60))
        self.Restart.setObjectName("Restart")
        self.L1 = QtWidgets.QLabel(self.centralwidget)
        self.L1.setGeometry(QtCore.QRect(70, 85, 211, 71))
        self.L1.setObjectName("L1")
        self.ProcessName = QtWidgets.QComboBox(self.centralwidget)
        self.ProcessName.setGeometry(QtCore.QRect(300, 100, 100, 40))
        self.ProcessName.setObjectName("ProcessName")
        self.L2 = QtWidgets.QLabel(self.centralwidget)
        self.L2.setGeometry(QtCore.QRect(70, 155, 201, 51))
        self.L2.setObjectName("L2")
        self.L3 = QtWidgets.QLabel(self.centralwidget)
        self.L3.setGeometry(QtCore.QRect(70, 200, 281, 81))
        self.L3.setObjectName("L3")
        self.L4 = QtWidgets.QLabel(self.centralwidget)
        self.L4.setGeometry(QtCore.QRect(70, 260, 221, 81))
        self.L4.setObjectName("L4")
        self.L5 = QtWidgets.QLabel(self.centralwidget)
        self.L5.setGeometry(QtCore.QRect(70, 310, 281, 101))
        self.L5.setObjectName("L5")
        self.Prior = QtWidgets.QComboBox(self.centralwidget)
        self.Prior.setGeometry(QtCore.QRect(300, 160, 100, 40))
        self.Prior.setObjectName("Prior")
        self.NeedTime = QtWidgets.QComboBox(self.centralwidget)
        self.NeedTime.setGeometry(QtCore.QRect(300, 220, 100, 40))
        self.NeedTime.setObjectName("NeedTime")
        self.IOTime = QtWidgets.QComboBox(self.centralwidget)
        self.IOTime.setGeometry(QtCore.QRect(300, 280, 100, 40))
        self.IOTime.setObjectName("IOTime")
        self.IOLast = QtWidgets.QComboBox(self.centralwidget)
        self.IOLast.setGeometry(QtCore.QRect(300, 340, 100, 40))
        self.IOLast.setObjectName("IOLast")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(260, 420, 150, 60))
        self.Save.setObjectName("Save")
        self.StartSchedule = QtWidgets.QPushButton(self.centralwidget)
        self.StartSchedule.setGeometry(QtCore.QRect(60, 510, 150, 60))
        self.StartSchedule.setObjectName("StartSchedule")
        InputPara.setCentralWidget(self.centralwidget)

        self.retranslateUi(InputPara)
        QtCore.QMetaObject.connectSlotsByName(InputPara)

    def retranslateUi(self, InputPara):
        _translate = QtCore.QCoreApplication.translate
        InputPara.setWindowTitle(_translate("InputPara", "进程调度系统"))
        self.Restart.setText(_translate("InputPara", "返回主菜单"))
        self.L1.setText(_translate("InputPara", "当前进程"))
        self.L2.setText(_translate("InputPara", "优先级"))
        self.L3.setText(_translate("InputPara", "运行时间"))
        self.L4.setText(_translate("InputPara", "IO 开始时间"))
        self.L5.setText(_translate("InputPara", "IO 持续时间"))
        self.Save.setText(_translate("InputPara", "保存"))
        self.StartSchedule.setText(_translate("InputPara", "开始调度"))

