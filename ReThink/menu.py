from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.ui_menu import Ui_Menu
from today import Ui_Today_sub
import sys

class Ui_Menu_sub(QtWidgets.QMainWindow, Ui_Menu): # 多态继承界面类来添加逻辑
    def __init__(self, parent = None):
        super(Ui_Menu_sub, self).__init__(parent = parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('image/ReThink.ico')) 
        self.setStyleSheet('''border-image: url(image/bg_img.jpg);''') # 设置自适应背景
        self.Today.clicked.connect(self.op_today)

    def op_today(self):
        self.w_today = Ui_Today_sub()
        self.w_today.show()
        self.close()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Menu_sub()
    window.show()
    sys.exit(app.exec_())