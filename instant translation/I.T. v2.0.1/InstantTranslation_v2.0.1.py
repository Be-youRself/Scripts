# Coding: utf8
# 程序主体，用于显示翻译内容及相关操作信息

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import *
from pynput import keyboard
import pyperclip
import os
import sys
import threading
import time
import tkinter as tk
from tkinter import filedialog
import re
import requests
import math

from ui.UI_translationbox import Ui_Translation_box


class Translationbox(QtWidgets.QMainWindow, Ui_Translation_box):  # 多态继承界面类来添加逻辑
    def __init__(self, parent=None):
        super(Translationbox, self).__init__(parent=parent)
        self.setupUi(self)
        # 参数声明 #
        # 窗口移动与尺寸
        self.screen_geometry = QApplication.desktop().screenGeometry()
        self.m_Position = self.pos()
        self.m_flag = False
        self.init_windowSize = self.geometry()
        self.now_window_pos = ((self.screen_geometry.width() - self.geometry().width()) / 2, 0, self.screen_geometry.width() / 2) # 第三参数为中间位置
        # 监听操作
        self.ctrl_flag = False
        self.hide_flag = False
        self.delay_time = 0.05  # 执行翻译前延时，单位秒
        self.exit_time = 300  # 计时退出，单位0.1秒
        # 查词翻译
        self.word_repository = {}
        self.words_width = 9.1  # 按照GBK编码后每个字符所占用宽度（中文占用两个字符宽度）
        self.output_length = self.init_windowSize.width() / self.words_width  # 输出字符限制
        # 文件位置
        self.newWord_file_name = "config/newWordData.txt"
        self.repository_file_name = "config/wordRepository.txt"
        self.guide_file_name = "使用说明.txt"
        # 参数声明 #
        self.window_settings()  # 窗口属性设置
        self.load_operation()  # 加载操作

    def window_settings(self):
        # 控制窗口打开位置
        self.move(self.now_window_pos[0], self.now_window_pos[1])
        # 隐藏界面头部内容以及任务栏窗口
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        # 设置窗口背景透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def load_operation(self):
        # 新建 config 文件夹
        if not os.path.exists("config"):
            os.makedirs('config')
        # 新建说明文档
        if not os.path.exists(self.guide_file_name):
            guide_file = open(self.guide_file_name, "w", encoding="utf8")
            guide_file.write('''---------------★★★★★ I.T. (Instant Translation)★★★★★---------------

_________________________________________________________________________________________________________________


使用方法：
    1、进入程序后，屏幕中央顶部会悬浮一道蓝色的展示框，可通过鼠标拖动来调整其位置；
    2、查词：遇到任何陌生的英文单词，都可以通过将其“Ctrl + C”复制到剪切板来进行查询；
    3、词组翻译/句子翻译：通过将其“Ctrl + C”复制到剪切板可翻译词组或是不是很长的句子；
    4、生成生词本：通过点击悬浮框，使用快捷键“M”，即可选择路径生成生词本（“生词本.txt”），内含所有查询过的英文单词；
    5、程序一直于后台悬浮运行，不影响计算机上其他任务（快捷键可能会被其他软件响应）；
    6、如果悬浮框遮挡了视线，可以通过快捷键“Ctrl + H”来暂时隐藏悬浮框，出于隐藏状态一段时间后（30 s），程序会自动退出；可以通过再次使用该快捷键来显示悬浮框；
    7、如果想要退出程序，点击选中白色展示框后，使用快捷键“Esc”即可退出程序。

_________________________________________________________________________________________________________________


    任何用户在使用程序中出现问题或是对程序感兴趣的话，都可以联系我，我将尽我所能给予解答。（QQ: 1090671860）    
                    ''')
            guide_file.close()
        # 下载并载入词库
        time.sleep(2) # 模拟下载词库
        # 载入词库
        try:
            wordRepository_file = open(self.repository_file_name, "r", encoding="utf8")
            self.word_repository = eval(wordRepository_file.read())
            wordRepository_file.close()
        except Exception:
            pass
        # 新建生词文件
        if not os.path.exists(self.newWord_file_name):
            newWord_File = open(self.newWord_file_name, "w", encoding="utf-8")
            newWord_File.write("{}")
            newWord_File.close()
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
        if (str(key) == "Key.ctrl_l" or str(key) == "Key.ctrl_r") and not self.ctrl_flag:  # 防止一直赋值占用 cpu
            self.ctrl_flag = True
        elif str(key) == "'c'":
            if self.ctrl_flag and not self.hide_flag:
                # 恢复窗口
                self.resize_window()
                self.Show_box.setText("翻译中...")
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
        try:
            text = self.preprocess(self.get_text())  # 预处理
        except Exception:
            self.postprocess("该内容不可翻译！")
            return
        # 判断单词还是句子
        trans_text = text.replace("-", "")  # 处理破折号用于判断
        if re.search(r"^[A-Za-z]+$", trans_text):  # 不能用 isalpha() 判断，因为中文也返回 True
            # 单词
            trans_result = self.en2chs_repository(text.lower())
            if trans_result != "":
                self.postprocess(trans_result)
            else:
                trans_result = self.en2chs_Yd_word(text)
                self.postprocess(trans_result)
                if trans_result != "未查询到该词义！" and trans_result != "无法连接网络！":
                    # 记录需要提交的库中没有的词
                    text = text.lower()
                    self.word_repository[text] = trans_result
            # 记录生词
            if trans_result != "未查询到该词义！" and trans_result != "无法连接网络！":
                text = text.lower()
                if not os.path.exists(self.newWord_file_name):  # 不存在则新建
                    newWord_file = open(self.newWord_file_name, "w", encoding="utf-8")
                    newWord_file.write("{}")
                    newWord_file.close()
                newWord_file = open(self.newWord_file_name, "r", encoding="utf8")
                word_dict = newWord_file.read()
                newWord_file.close()
                try:
                    word_dict = eval(word_dict)
                    word_dict[text] = trans_result
                    word_dict = str(word_dict)
                    newWord_file = open(self.newWord_file_name, "w", encoding="utf-8")
                    newWord_file.write(word_dict)
                    newWord_file.close()
                except Exception:
                    # 文件受损即删除重建
                    word_dict = {text: trans_result}
                    word_dict = str(word_dict)
                    newWord_file = open(self.newWord_file_name, "w", encoding="utf-8")
                    newWord_file.write(word_dict)
                    newWord_file.close()
        else:
            # 句子
            trans_result = self.en2chs_Yd_sentence(text)
            self.postprocess(trans_result)

    @staticmethod
    def preprocess(text):
        text = text.replace("\t", "")  # 消除制表符
        text = text.replace("\n", "")  # 消除回车符
        text = text.strip()  # 消除首尾空格
        return text

    @staticmethod
    def en2chs_Yd_word(text):
        # 通过爬取分析有道网页查询单词释义
        trans_result = ""
        trans_url = "http://www.youdao.com/w/" + text  # 将空格全部替换，方便网页搜索
        try:
            trans_page = requests.get(trans_url)  # 这里爬取时可能出现连接失败的异常
        except Exception as e:
            return "无法连接网络！"
        if trans_page.status_code == 500:  # 连接失败
            return "无法连接网络！"
        trans_source = str(trans_page.content, encoding="utf-8")
        trans_flag0 = '<div class="trans-container">'  # 定位释义区间
        if trans_source.find(trans_flag0) != -1:
            # 常用词
            # 普通释义
            trans_source = trans_source[trans_source.find(trans_flag0):]
            trans_flag1 = '<ul>'
            trans_flag2 = '</ul>'
            trans_source = trans_source[trans_source.find(trans_flag1): trans_source.find(trans_flag2)]
            trans_flag3 = '<li>'
            trans_flag4 = '</li>'
            trans_num = len(trans_source.split(trans_flag3)) - 1  # 获取词义数量
            trans_list = []
            for i in range(trans_num):
                trans_source = trans_source[trans_source.find(trans_flag3):]
                trans_list.append(trans_source[len(trans_flag3): trans_source.find(trans_flag4)].strip())
                trans_source = trans_source[trans_source.find(trans_flag4):]
                trans_result = "|".join(trans_list)
        else:
            # 特殊词
            trans_flag0 = '<ul id="tPETrans-all-trans" class="all-trans">'
            if trans_source.find(trans_flag0) != -1:
                # 专业释义
                trans_flag1 = '<span class="title">'
                trans_flag2 = '</span>'
                trans_num = len(trans_source.split(trans_flag1)) - 1  # 获取词义数量
                trans_list = []
                for i in range(trans_num):
                    trans_source = trans_source[trans_source.find(trans_flag1):]
                    trans_list.append(trans_source[len(trans_flag1): trans_source.find(trans_flag2)].strip())
                    trans_source = trans_source[trans_source.find(trans_flag2):]
                trans_result = "|".join(trans_list)
            else:
                # 网络释义
                trans_flag2 = '<a href="#" title="详细释义" rel="#rw1" class="sp do-detail">&nbsp;</a>'
                trans_flag3 = '<span>'
                trans_flag4 = '</span>'
                trans_num = len(trans_source.split(trans_flag2)) - 1  # 获取词义数量
                trans_list = []
                for i in range(trans_num):
                    trans_source = trans_source[trans_source.find(trans_flag2):]
                    trans_list.append(trans_source[trans_source.find(trans_flag3) + len(trans_flag3): trans_source.find(
                        trans_flag4)].strip())
                    trans_source = trans_source[trans_source.find(trans_flag4):]
                trans_result = "|".join(trans_list)
        if trans_result == "":
            return "未查询到该词义！"
        else:
            return trans_result

    @staticmethod
    def en2chs_Yd_sentence(text):
        # 通过爬取分析有道网页翻译句子
        trans_result = ""
        trans_url = "http://www.youdao.com/w/" + text.replace(" ", "%20")  # 将空格全部替换，方便网页搜索
        try:
            trans_page = requests.get(trans_url)  # 这里爬取时可能出现连接失败的异常
        except Exception as e:
            return "无法连接网络！"
        if trans_page.status_code == 500:  # 连接失败
            return "无法连接网络！"
        trans_source = str(trans_page.content, encoding="utf-8")
        # 夹杂了中文单词翻译，需要判断
        trans_flag0 = '<div class="trans-container">'  # 定位释义区间
        if trans_source.find(trans_flag0) == -1:
            return "无法翻译该内容！"
        else:
            trans_source = trans_source[trans_source.find(trans_flag0):]
            trans_flag3 = '<p class="wordGroup">'
            if trans_source.find(trans_flag3) == -1:
                # 句子翻译(英译汉、汉译英)
                trans_flag1 = "<p>"
                trans_source = trans_source[trans_source.find(trans_flag1) + 1:]  # 定位到输入，加1防止不变化
                trans_source = trans_source[trans_source.find(trans_flag1):]  # 定位到结果
                trans_flag2 = '</p>'
                trans_result = trans_source[len(trans_flag1):trans_source.find(trans_flag2)].strip()  # 结果
            else:
                # 汉译英词语翻译
                trans_source = trans_source[trans_source.find(trans_flag3):]
                trans_flag4 = "</a>"
                trans_source = trans_source[:trans_source.find(trans_flag4)]
                trans_flag5 = '">'
                trans_result = trans_source[trans_source.rfind(trans_flag5) + len(trans_flag5):].strip()
        if trans_result == "":
            return "无法翻译该内容！"
        else:
            return trans_result

    def en2chs_repository(self, text):
        # 通过访问本地仓库来查询单词释义
        trans_result = ""
        if text in self.word_repository:
            trans_result = self.word_repository[text]
        return trans_result

    def postprocess(self, trans_result):
        # 单词展示格式调整等
        output_length = len(list(trans_result.encode("GBK")))
        if output_length > self.output_length:
            window_width = int(math.ceil(output_length * self.words_width))
            if window_width > self.screen_geometry.width():
                trans_result = "输出结果太长，无法显示！"
            else:
                # 改变窗口和控件大小
                self.resize(window_width, self.init_windowSize.height())
                self.setMinimumSize(QtCore.QSize(window_width, self.init_windowSize.height()))
                self.setMaximumSize(QtCore.QSize(window_width, self.init_windowSize.height()))
                self.Show_box.setGeometry(QtCore.QRect(0, 0, window_width, self.init_windowSize.height()))
                # 移动窗口位置
                self.window_move()
        self.Show_box.setText(trans_result)

    def resize_window(self):
        # 重置窗口显示
        self.Show_box.setText("")
        # 恢复窗口和控件大小
        self.resize(self.init_windowSize.width(), self.init_windowSize.height())
        self.setMinimumSize(QtCore.QSize(self.init_windowSize.width(), self.init_windowSize.height()))
        self.setMaximumSize(QtCore.QSize(self.init_windowSize.width(), self.init_windowSize.height()))
        self.Show_box.setGeometry(QtCore.QRect(0, 0, self.init_windowSize.width(), self.init_windowSize.height()))
        # 移动窗口位置
        self.window_move()

    def window_move(self):
        # 移动窗口位置
        x = self.now_window_pos[0]
        y = self.now_window_pos[1]
        z = self.now_window_pos[2]
        x = z - self.geometry().width() / 2
        # 调整使不超出屏幕
        if x < 0:
            x = 0
        if x > self.screen_geometry.width() - self.geometry().width():
            x = self.screen_geometry.width() - self.geometry().width()
        z = x + self.geometry().width() / 2
        self.move(x, y)
        self.now_window_pos = (x, y, z)

    def timer2exit(self):
        for i in range(self.exit_time):
            if not self.hide_flag:
                self.show()
                return
            time.sleep(0.1)
        self.program_exit()

    @staticmethod
    def get_text():
        # 获取剪切板内容
        text = pyperclip.paste()
        return text

    def keyPressEvent(self, evt):
        # 程序退出按钮
        if evt.key() == Qt.Key_Escape:
            self.program_exit()
        elif evt.key() == Qt.Key_M:
            # 恢复窗口
            self.resize_window()
            self.make_newWordBook()

    def program_exit(self):
        # 保存新词库
        wordRepository_file = open(self.repository_file_name, "w", encoding="utf-8")
        wordRepository_file.write(str(self.word_repository))
        wordRepository_file.close()
        os._exit(0)

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
            if not os.path.exists(self.newWord_file_name):  # 不存在则新建
                newWord_File = open(self.newWord_file_name, "w", encoding="utf-8")
                newWord_File.write("{}")
                newWord_File.close()
            newWord_File = open(self.newWord_file_name, "r", encoding="utf8")
            word_dict = newWord_File.read()
            newWord_File.close()
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
        # 保存当前位置
        self.now_window_pos = (x, y, self.geometry().width() / 2 + x)
        # 控制位置不超出屏幕外 #
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("ui/pic_resource/IT_startupScreen.png"))
    splash.show()  # 显示启动界面
    QtWidgets.qApp.processEvents()
    window = Translationbox()
    window.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
