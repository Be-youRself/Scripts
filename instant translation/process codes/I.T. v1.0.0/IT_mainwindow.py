from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QApplication, QMenu, QAction, qApp

from ui.UI_instant_translation import Ui_MainWindow
import IT_translationbox
import sys
import os
import tkinter as tk
from tkinter import filedialog

import threading

repository_file_name = "word_repository.txt"

class IT_mainwindow(QtWidgets.QMainWindow, Ui_MainWindow): # 多态继承界面类来添加逻辑
    def __init__(self, parent = None):
        super(IT_mainwindow, self).__init__(parent = parent)
        self.setupUi(self)
        # 绑定函数
        self.Make_newWordBook.clicked.connect(self.make_newWordBook)
        self.Translation_mode.clicked.connect(self.op_trans)

    def TrayEvent(self):
        pass

    def op_trans(self):
        self.w_t_box = IT_translationbox.Translation_box()
        # 置于最上层
        self.w_t_box.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.w_t_box.show()
        self.close()

    def make_newWordBook(self):
        # 清空提示框
        self.Tips.setText("")

        # 用户确定地址
        filename = "生词本.txt"
        ## 打开选择对话框
        root = tk.Tk()
        root.withdraw()
        ## 确定地址
        # 获得选择好的文件夹
        address = filedialog.askdirectory() + "/" + filename

        # 生成生词本
        if not os.path.exists(repository_file_name):  # 不存在则新建
            repository_file = open(repository_file_name, "w", encoding="utf-8")
            repository_file.write("{}")
            repository_file.close()
        else:
            repository_file = open(repository_file_name, "r", encoding="utf8")
            word_dict = repository_file.read()
            repository_file.close()
        newWordBook = ""
        try:
            word_dict = eval(word_dict)
            for i in word_dict:
                newWordBook += i
                for j in range(30 - len(i)):
                    newWordBook += " "
                newWordBook += word_dict[i] + "\n"
            newWordBook_file = open(address, "w", encoding="utf8")
            newWordBook_file.write(newWordBook)
            newWordBook_file.close()
            self.Tips.setText('生成成功!(' + filename + ")")
        except Exception as e:
            self.Tips.setText("文件生成出错！")
            print(e)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = IT_mainwindow()
    window.show()
    sys.exit(app.exec_())