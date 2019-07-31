# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 630)
        MainWindow.setMinimumSize(QtCore.QSize(622, 630))
        MainWindow.setMaximumSize(QtCore.QSize(622, 630))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(130, 270, 581, 101))
        self.Title.setStyleSheet("font: 30pt \"华文楷体\";")
        self.Title.setObjectName("Title")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(120, 420, 150, 60))
        self.Start.setObjectName("Start")
        self.Change = QtWidgets.QPushButton(self.centralwidget)
        self.Change.setGeometry(QtCore.QRect(120, 500, 150, 60))
        self.Change.setObjectName("Change")
        self.About = QtWidgets.QPushButton(self.centralwidget)
        self.About.setGeometry(QtCore.QRect(350, 500, 150, 60))
        self.About.setObjectName("About")
        self.Recreate = QtWidgets.QPushButton(self.centralwidget)
        self.Recreate.setGeometry(QtCore.QRect(350, 420, 150, 60))
        self.Recreate.setObjectName("Recreate")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(200, 70, 211, 181))
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "进程调度系统"))
        self.Title.setText(_translate("MainWindow", "进程调度系统"))
        self.Start.setText(_translate("MainWindow", "开始进程调度"))
        self.Change.setText(_translate("MainWindow", "修改配置文件"))
        self.About.setText(_translate("MainWindow", "关于"))
        self.Recreate.setText(_translate("MainWindow", "重置配置文件"))

