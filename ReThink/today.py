from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.ui_today import Ui_Today
import menu
import sys

class Ui_Today_sub(QtWidgets.QMainWindow, Ui_Today):
    def __init__(self, parent = None):
        super(Ui_Today_sub, self).__init__(parent = parent)
        self.setupUi(self) 
        self.setWindowIcon(QIcon('ui/image/ReThink.ico')) 
        self.setStyleSheet('''border-image: url(ui/image/bg_img.jpg);''') 
        self.Back.clicked.connect(self.menu_show)    
