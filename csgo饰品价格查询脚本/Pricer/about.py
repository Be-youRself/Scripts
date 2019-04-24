from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.about import Ui_About
import menu

class Ui_About_sub(QtWidgets.QMainWindow, Ui_About): # 多态继承界面类来添加逻辑
    def __init__(self, parent = None):
        super(Ui_About_sub, self).__init__(parent = parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/image/PC.ico'))
        self.setStyleSheet('''#About{border-image: url(ui/image/bg_img.jpg);}''') # 设置自适应背景
        self.Back.clicked.connect(self.op_menu)


    def op_menu(self):
        ## 返回菜单
        self.w_menu = menu.Ui_Menu_sub()
        self.w_menu.show()
        self.close()