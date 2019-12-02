# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_translationbox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Translation_box(object):
    def setupUi(self, Translation_box):
        Translation_box.setObjectName("Translation_box")
        Translation_box.resize(1200, 45)
        Translation_box.setMinimumSize(QtCore.QSize(1200, 45))
        Translation_box.setMaximumSize(QtCore.QSize(1200, 45))
        self.centralwidget = QtWidgets.QWidget(Translation_box)
        self.centralwidget.setObjectName("centralwidget")
        self.Show_box = QtWidgets.QLabel(self.centralwidget)
        self.Show_box.setGeometry(QtCore.QRect(0, 0, 1200, 45))
        self.Show_box.setStyleSheet("border-radius:10px 15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:repeat, x1:0.505682, y1:0, x2:0.505682, y2:1, stop:0.335227 rgba(21, 0, 142, 255), stop:1 rgba(63, 81, 255, 255));")
        self.Show_box.setText("")
        self.Show_box.setAlignment(QtCore.Qt.AlignCenter)
        self.Show_box.setObjectName("Show_box")
        Translation_box.setCentralWidget(self.centralwidget)

        self.retranslateUi(Translation_box)
        QtCore.QMetaObject.connectSlotsByName(Translation_box)

    def retranslateUi(self, Translation_box):
        _translate = QtCore.QCoreApplication.translate
        Translation_box.setWindowTitle(_translate("Translation_box", "I.T."))

