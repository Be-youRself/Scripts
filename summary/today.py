from PyQt5 import QtWidgets
from ui_today import Ui_Today
import sys

class Ui_Today_sub(QtWidgets.QWidget, Ui_Today): #多态继承
    def __init__(self, parent = None):
        super(Ui_Today_sub, self).__init__(parent = parent)
        self.setupUi(self)       
