# Coding: utf-8
# 简介信息窗口

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.about_ui import Ui_About


class About(QtWidgets.QMainWindow, Ui_About):  # 多态继承界面类来添加逻辑
    def __init__(self, parent=None):
        super(About, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/image/PC.ico'))
        self.setStyleSheet('''#About{border-image: url(ui/image/bg_img.jpg);}''')  # 设置自适应背景
