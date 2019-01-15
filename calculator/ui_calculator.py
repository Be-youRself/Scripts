# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 539)
        MainWindow.setMinimumSize(QtCore.QSize(372, 539))
        MainWindow.setMaximumSize(QtCore.QSize(372, 539))
        MainWindow.setStyleSheet("background-color: rgb(229, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 20, 421, 581))
        self.widget.setObjectName("widget")
        self.butt1 = QtWidgets.QPushButton(self.widget)
        self.butt1.setGeometry(QtCore.QRect(30, 190, 70, 70))
        self.butt1.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt1.setObjectName("butt1")
        self.butt2 = QtWidgets.QPushButton(self.widget)
        self.butt2.setGeometry(QtCore.QRect(110, 190, 70, 70))
        self.butt2.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt2.setObjectName("butt2")
        self.butt3 = QtWidgets.QPushButton(self.widget)
        self.butt3.setGeometry(QtCore.QRect(190, 190, 70, 70))
        self.butt3.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt3.setObjectName("butt3")
        self.butt4 = QtWidgets.QPushButton(self.widget)
        self.butt4.setGeometry(QtCore.QRect(30, 270, 70, 70))
        self.butt4.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt4.setObjectName("butt4")
        self.butt5 = QtWidgets.QPushButton(self.widget)
        self.butt5.setGeometry(QtCore.QRect(110, 270, 70, 70))
        self.butt5.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt5.setObjectName("butt5")
        self.butt6 = QtWidgets.QPushButton(self.widget)
        self.butt6.setGeometry(QtCore.QRect(190, 270, 70, 70))
        self.butt6.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt6.setObjectName("butt6")
        self.butt7 = QtWidgets.QPushButton(self.widget)
        self.butt7.setGeometry(QtCore.QRect(30, 350, 70, 70))
        self.butt7.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt7.setObjectName("butt7")
        self.butt_minus = QtWidgets.QPushButton(self.widget)
        self.butt_minus.setGeometry(QtCore.QRect(270, 190, 70, 70))
        self.butt_minus.setStyleSheet("\n"
"font: 18pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt_minus.setObjectName("butt_minus")
        self.butt8 = QtWidgets.QPushButton(self.widget)
        self.butt8.setGeometry(QtCore.QRect(110, 350, 70, 70))
        self.butt8.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt8.setObjectName("butt8")
        self.butt9 = QtWidgets.QPushButton(self.widget)
        self.butt9.setGeometry(QtCore.QRect(190, 350, 70, 70))
        self.butt9.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt9.setObjectName("butt9")
        self.butt_multiple = QtWidgets.QPushButton(self.widget)
        self.butt_multiple.setGeometry(QtCore.QRect(270, 270, 70, 70))
        self.butt_multiple.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt_multiple.setObjectName("butt_multiple")
        self.butt_division = QtWidgets.QPushButton(self.widget)
        self.butt_division.setGeometry(QtCore.QRect(270, 350, 70, 70))
        self.butt_division.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt_division.setObjectName("butt_division")
        self.butt0 = QtWidgets.QPushButton(self.widget)
        self.butt0.setGeometry(QtCore.QRect(110, 430, 70, 70))
        self.butt0.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt0.setObjectName("butt0")
        self.butt_plus = QtWidgets.QPushButton(self.widget)
        self.butt_plus.setGeometry(QtCore.QRect(270, 110, 70, 70))
        self.butt_plus.setStyleSheet("\n"
"font: 18pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt_plus.setObjectName("butt_plus")
        self.butt_dot = QtWidgets.QPushButton(self.widget)
        self.butt_dot.setGeometry(QtCore.QRect(190, 430, 70, 70))
        self.butt_dot.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt_dot.setObjectName("butt_dot")
        self.butt_per = QtWidgets.QPushButton(self.widget)
        self.butt_per.setGeometry(QtCore.QRect(190, 110, 70, 70))
        self.butt_per.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt_per.setObjectName("butt_per")
        self.butt_restart = QtWidgets.QPushButton(self.widget)
        self.butt_restart.setGeometry(QtCore.QRect(30, 110, 70, 70))
        self.butt_restart.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: rgb(221, 253, 255);\n"
"color: rgb(255, 85, 0);")
        self.butt_restart.setObjectName("butt_restart")
        self.butt_back = QtWidgets.QPushButton(self.widget)
        self.butt_back.setGeometry(QtCore.QRect(110, 110, 70, 70))
        self.butt_back.setStyleSheet("image: url(:/pic/image/back.png);\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt_back.setText("")
        self.butt_back.setObjectName("butt_back")
        self.butt_equal = QtWidgets.QPushButton(self.widget)
        self.butt_equal.setGeometry(QtCore.QRect(270, 430, 70, 70))
        self.butt_equal.setStyleSheet("\n"
"font: 12pt \"宋体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(255, 170, 127);")
        self.butt_equal.setObjectName("butt_equal")
        self.butt_logo = QtWidgets.QPushButton(self.widget)
        self.butt_logo.setGeometry(QtCore.QRect(30, 430, 70, 70))
        self.butt_logo.setStyleSheet("image: url(:/pic/image/logo.png);\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(221, 253, 255);")
        self.butt_logo.setText("")
        self.butt_logo.setObjectName("butt_logo")
        self.output = QtWidgets.QTextBrowser(self.widget)
        self.output.setGeometry(QtCore.QRect(30, 0, 310, 90))
        self.output.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"宋体\";\n"
"text-align:right;")
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.butt1.setText(_translate("MainWindow", "1"))
        self.butt2.setText(_translate("MainWindow", "2"))
        self.butt3.setText(_translate("MainWindow", "3"))
        self.butt4.setText(_translate("MainWindow", "4"))
        self.butt5.setText(_translate("MainWindow", "5"))
        self.butt6.setText(_translate("MainWindow", "6"))
        self.butt7.setText(_translate("MainWindow", "7"))
        self.butt_minus.setText(_translate("MainWindow", "-"))
        self.butt8.setText(_translate("MainWindow", "8"))
        self.butt9.setText(_translate("MainWindow", "9"))
        self.butt_multiple.setText(_translate("MainWindow", "×"))
        self.butt_division.setText(_translate("MainWindow", "÷"))
        self.butt0.setText(_translate("MainWindow", "0"))
        self.butt_plus.setText(_translate("MainWindow", "+"))
        self.butt_dot.setText(_translate("MainWindow", "."))
        self.butt_per.setText(_translate("MainWindow", "%"))
        self.butt_restart.setText(_translate("MainWindow", "C"))
        self.butt_equal.setText(_translate("MainWindow", "="))
        self.output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

import rs_calculator_rc
