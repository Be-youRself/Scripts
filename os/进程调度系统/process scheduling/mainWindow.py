# Coding: utf-8
# 程序的开始窗口

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.mainWindow_ui import Ui_MainWindow
import createProcess
import about
import os
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):  # 多态继承界面类来添加逻辑
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/image/PC.ico'))
        self.setStyleSheet('''#MainWindow{border-image: url(ui/image/bg_img.jpg);}''')  # 设置自适应背景
        self.Logo.setStyleSheet('''border-image: url(ui/image/PC_Logo.png);''')
        # 如果配置文件不存在则自动创建一个默认参数的配置文件
        if not os.path.exists("configuration_file.txt"):
            self.create_configuration()
        self.Start.clicked.connect(self.op_creat)
        self.Change.clicked.connect(self.op_configuration)
        self.Recreate.clicked.connect(self.create_configuration)
        self.About.clicked.connect(self.op_about)

    @staticmethod
    def create_configuration():
        # 按照默认参数创建配置文件文件
        configuration_file = open("configuration_file.txt", "w", encoding="utf8")
        content = '''// Coding: utf-8
// 提示：若没有成功读取配置参数，可能是输入有误，如中英文分号等。
    
// 空闲资源队列数，范围为[1, 10]，默认为 5。
Resource: 5
             
// 就绪队列的个数，范围为[1, 5], 默认为 2。
Ready: 2

// 就绪队列对应时间片，用一个列表表示，每个时间片范围为[1, 10], 默认为[2, 3]
Ready_time: [2, 3]

'''
        configuration_file.write(content)
        configuration_file.close()

    def op_creat(self):
        # 打开创建进程窗口，开始创建进程
        self.w_createProcess = createProcess.CreateProcess()
        self.w_createProcess.show()
        self.close()

    @staticmethod
    def op_configuration():
        # 打开配置文件用于修改
        os.system("configuration_file.txt")

    def op_about(self):
        # 打开简介界面
        self.w_about = about.About()
        self.w_about.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
