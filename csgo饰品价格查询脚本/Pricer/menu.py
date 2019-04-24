from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.mainwindow import Ui_Menu
import inquiry
import about
import sys

class Ui_Menu_sub(QtWidgets.QMainWindow, Ui_Menu): # 多态继承界面类来添加逻辑
    def __init__(self, parent = None):
        super(Ui_Menu_sub, self).__init__(parent = parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/image/PC.ico'))
        self.setStyleSheet('''#Menu{border-image: url(ui/image/bg_img.jpg);}''') # 设置自适应背景
        self.Logo.setStyleSheet('''border-image: url(ui/image/PC_Logo.png);''')
        self.Inquiry.clicked.connect(self.op_inquiry)
        self.About.clicked.connect(self.op_about)

    def op_inquiry(self):
        self.w_inquiry = inquiry.Ui_Inquiry_sub()
        self.w_inquiry.show()
        self.close()

    def op_about(self):
        self.w_about = about.Ui_About_sub()
        self.w_about.show()
        self.close()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Menu_sub()
    window.show()
    sys.exit(app.exec_())