# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schedule_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Schedule(object):
    def setupUi(self, Schedule):
        Schedule.setObjectName("Schedule")
        Schedule.resize(802, 634)
        Schedule.setMinimumSize(QtCore.QSize(802, 634))
        Schedule.setMaximumSize(QtCore.QSize(802, 634))
        self.centralwidget = QtWidgets.QWidget(Schedule)
        self.centralwidget.setObjectName("centralwidget")
        self.ScheduleNote = QtWidgets.QTextBrowser(self.centralwidget)
        self.ScheduleNote.setGeometry(QtCore.QRect(45, 71, 711, 411))
        self.ScheduleNote.setObjectName("ScheduleNote")
        self.Restart = QtWidgets.QPushButton(self.centralwidget)
        self.Restart.setGeometry(QtCore.QRect(600, 520, 150, 60))
        self.Restart.setObjectName("Restart")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(390, 520, 150, 60))
        self.Next.setObjectName("Next")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 111, 31))
        self.label.setObjectName("label")
        self.NowTime = QtWidgets.QLabel(self.centralwidget)
        self.NowTime.setGeometry(QtCore.QRect(150, 20, 91, 31))
        self.NowTime.setText("")
        self.NowTime.setObjectName("NowTime")
        Schedule.setCentralWidget(self.centralwidget)

        self.retranslateUi(Schedule)
        QtCore.QMetaObject.connectSlotsByName(Schedule)

    def retranslateUi(self, Schedule):
        _translate = QtCore.QCoreApplication.translate
        Schedule.setWindowTitle(_translate("Schedule", "进程调度系统"))
        self.Restart.setText(_translate("Schedule", "返回主菜单"))
        self.Next.setText(_translate("Schedule", "下一步"))
        self.label.setText(_translate("Schedule", "当前时刻："))

