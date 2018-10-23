from PyQt5 import QtWidgets
from ui_menu import Ui_Menu
from today import Ui_Today_sub
import sys

class Ui_Menu_sub(QtWidgets.QMainWindow, Ui_Menu): #多态继承
    def __init__(self, parent = None):
        super(Ui_Menu_sub, self).__init__(parent = parent)
        self.setupUi(self)
        self.Today.clicked.connect(self.op_today)

    def op_today(self):
        w_today = Ui_Today_sub()
        w_today.show()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Menu_sub()
    window.show()
    sys.exit(app.exec_())