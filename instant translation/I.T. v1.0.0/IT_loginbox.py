# Coding: utf8
# 用户信息输入框，验证合法性并存储

from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import *
import sys
import os
import json

from ui.UI_loginbox import Ui_Loginbox
import IT_YdTranslation
import IT_translationbox


class Loginbox(QtWidgets.QMainWindow, Ui_Loginbox):  # 多态继承界面类来添加逻辑
    # 定义信号
    def __init__(self, parent=None):
        super(Loginbox, self).__init__(parent=parent)
        self.setupUi(self)
        # 参数声明 #
        self.ID_and_key_file_name = "config/ID_and_key.txt"
        self.guide_file_name = "说明文档.txt"
        # 参数声明  #
        self.window_settings()  # 窗口属性设置
        # 函数绑定 #
        self.Button_Finsh.clicked.connect(self.verify_and_save)
        self.Button_guide.clicked.connect(self.op_guideFile)
        self.Button_Exit.clicked.connect(self.sys_exit)
        # 函数绑定 #

    def window_settings(self):
        # 控制窗口打开位置居中
        screen = QApplication.desktop().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        # 隐藏界面头部内容以及任务栏窗口
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)

    def verify_and_save(self):
        ID = self.Input_ID.text()
        key = self.Input_key.text()
        try:
            result_json = IT_YdTranslation.en2chs("a", ID, key)
            result_dict = json.loads(result_json)
            if result_dict["errorCode"] == "0":
                ID_and_key_file = open(self.ID_and_key_file_name, "w", encoding="utf8")
                ID_and_key_file.write(ID + ":" + key)
                ID_and_key_file.close()
                self.op_translationbox()
            else:
                raise Exception
        except:
            # 输入 ID 和 key 不合法
            self.Input_ID.setText("")
            self.Input_key.setText("")
            self.Tips.setText("验证失败！请确认后重新输入！")

    def op_translationbox(self):
        translation_window = IT_translationbox.Translationbox()
        translation_window.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        translation_window.show()
        self.close()

    def op_guideFile(self):
        os.system(self.guide_file_name)

    def sys_exit(self):
        sys.exit()

    # 以下三个函数组合来完成鼠标移动窗口功能
    def mousePressEvent(self, q_mouse_event):
        if q_mouse_event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = q_mouse_event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            q_mouse_event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, q_mouse_event):
        if Qt.LeftButton and self.m_flag:
            self.move(q_mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            q_mouse_event.accept()

    def mouseReleaseEvent(self, q_mouse_event):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
