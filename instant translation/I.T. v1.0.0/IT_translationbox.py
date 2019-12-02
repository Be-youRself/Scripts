# Coding: utf8
# 程序主体，用于显示翻译内容及相关操作信息

from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import *
import win32clipboard
from pynput import keyboard
import os
import sys
import threading
import time
import enchant
import tkinter as tk
from tkinter import filedialog

from ui.UI_translationbox import Ui_Translation_box
import IT_translationModule


class Translationbox(QtWidgets.QMainWindow, Ui_Translation_box):  # 多态继承界面类来添加逻辑
    def __init__(self, parent=None):
        super(Translationbox, self).__init__(parent=parent)
        self.setupUi(self)
        # 参数声明 #
        # 窗口移动
        self.screen_geometry = QApplication.desktop().screenGeometry()
        self.m_Position = self.pos()
        self.m_flag = False
        # 监听操作
        self.ctrl_flag = False
        self.hide_flag = False
        self.delay_time = 0.05  # 执行翻译前延时，单位秒
        self.exit_time = 300  # 计时退出，单位0.2秒
        # 查词翻译
        self.clip = ""
        self.output_length = 80  # 输出字符限制
        self.input_length = 200  # 输入字符限制
        # 文件位置
        self.repository_file_name = "config/word_repository.txt"
        self.ID_and_key_file_name = "config/ID_and_key.txt"
        # 用户信息
        self.ID = ""
        self.key = ""
        # 参数声明 #
        self.stop_flag = True  # 等待另一个窗口的标记
        self.window_settings()  # 窗口属性设置
        self.load_operation()  # 加载操作

    def window_settings(self):
        # 控制窗口打开位置
        size = self.geometry()
        self.move((self.screen_geometry.width() - size.width()) / 2, 0)
        # 隐藏界面头部内容以及任务栏窗口
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        # 设置窗口背景透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def load_operation(self):
        # 加载用户信息
        ID_and_key_file = open(self.ID_and_key_file_name, "r", encoding="utf8")
        ID_and_key_list = ID_and_key_file.read().split(":")
        self.ID = ID_and_key_list[0]
        self.key = ID_and_key_list[1]
        # 启动监听按键线程
        monitor_thread = threading.Thread(target=self.monitor_keys, args=())
        monitor_thread.setDaemon(True)  # 设置为守护线程
        monitor_thread.start()

    def monitor_keys(self):
        # 检测按键并进行翻译
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        if (str(key) == "Key.ctrl_l" or str(key) == "Key.ctrl_r") and not self.ctrl_flag: # 防止一直赋值占用 cpu
            self.ctrl_flag = True
        elif str(key) == "'c'":
            if self.ctrl_flag and not self.hide_flag:
                time.sleep(self.delay_time)  # 防止剪切板未更新
                self.translation()
        elif str(key) == "'h'":
            if self.ctrl_flag and not self.hide_flag:
                # 当前是显示状态
                self.hide_flag = True
                timer2exit_thread = threading.Thread(target=self.timer2exit, args=())
                timer2exit_thread.setDaemon(True)
                timer2exit_thread.start()
                self.hide()
            elif self.ctrl_flag and self.hide_flag:
                self.hide_flag = False
            else:
                pass
        else:
            pass

    def on_release(self, key):
        if str(key) == "Key.ctrl_l" or str(key) == "Key.ctrl_r":
            self.ctrl_flag = False

    def translation(self):
        word = self.gettext().strip()
        if self.clip == word:  # 剪切板内容未变则不操作
            pass
        else:
            self.clip = word
            # 判断是单词还是句子
            if word.find(" ") == -1:  # 单词
                if enchant.Dict("en_US").check(word):
                    translation_result = IT_translationModule.en2chs(word, self.ID, self.key)
                    # 处理翻译结果
                    while len(translation_result) > self.output_length:
                        translation_result = translation_result[:translation_result.rfind("|")]
                    self.Show_box.setText(translation_result)
                else:
                    self.Show_box.setText("不是有效英文单词！")
            else:  # 句子
                self.Show_box.setText("翻译中...")
                # 处理复制的句子
                # 处理标点符号 #
                word_to_deal = word.replace("?", " ")
                word_to_deal = word_to_deal.replace(".", " ")
                word_to_deal = word_to_deal.replace(",", " ")
                word_to_deal = word_to_deal.replace("(", " ")
                word_to_deal = word_to_deal.replace(")", " ")
                word_to_deal = word_to_deal.replace("'", " ")
                word_to_deal = word_to_deal.replace('"', " ")
                # 处理标点符号 #
                word_list = word_to_deal.split()
                valid_flag = True  # 判断句子是否合法的标记
                for i in range(len(word_list)):
                    if not enchant.Dict("en_US").check(word_list[i]):
                        if word_list[i].isdigit():  # 该项全由数字组成
                            continue
                        valid_flag = False
                        break
                if valid_flag:
                    sentence = " ".join(word.split())
                    if len(sentence) > self.input_length:
                        self.Show_box.setText("输入的句子太长了！")
                    else:
                        translation_result = IT_translationModule.en2chs(sentence, self.ID, self.key)
                        # 处理翻译结果
                        if len(translation_result) > self.output_length:
                            translation_result = translation_result[:self.output_length] + "..."
                        self.Show_box.setText(translation_result)
                else:
                    self.Show_box.setText("不是有效英文句子！")

    def timer2exit(self):
        for i in range(self.exit_time):
            if not self.hide_flag:
                self.show()
                return
            time.sleep(0.1)
        os._exit(0)

    @staticmethod
    def gettext():
        # 获取剪切板内容
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return text

    def keyPressEvent(self, evt):
        # 程序退出按钮
        if evt.key() == Qt.Key_Escape:
            sys.exit()
        elif evt.key() == Qt.Key_M:
            self.make_newWordBook()

    def make_newWordBook(self):
        # 用户确定地址
        filename = "生词本.txt"
        # 打开选择对话框
        root = tk.Tk()
        root.wm_attributes('-topmost', 1)
        root.withdraw()
        # 获得选择好的文件夹
        address = filedialog.askdirectory()
        if address == "":  # 取消文件选择
            self.Show_box.setText("已取消生成生词本！")
        else:
            address += "/" + filename

            # 生成生词本
            if not os.path.exists(self.repository_file_name):  # 不存在则新建
                repository_file = open(self.repository_file_name, "w", encoding="utf-8")
                repository_file.write("{}")
                repository_file.close()
            repository_file = open(self.repository_file_name, "r", encoding="utf8")
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
                self.Show_box.setText("生词本生成成功!")
            except Exception as e:
                self.Show_box.setText("生词本生成出错！")

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
        # 控制位置不超出屏幕外 #
        x = self.x()
        y = self.y()
        if y < 0:
            y = 0
        if y > self.screen_geometry.height() - self.geometry().height():
            y = self.screen_geometry.height() - self.geometry().height()
        if x < 0:
            x = 0
        if x > self.screen_geometry.width() - self.geometry().width():
            x = self.screen_geometry.width() - self.geometry().width()
        self.move(x, y)
        # 控制位置不超出屏幕外 #
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Translationbox()
    window.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    window.show()
    sys.exit(app.exec_())
