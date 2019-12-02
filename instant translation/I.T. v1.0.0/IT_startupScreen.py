# Coding: utf8
# 程序的启动文件，负责加载启动动画，并设置了相应的特效(淡入淡出)

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QSplashScreen
import sys
import os
import time
import json

from IT_loginbox import Loginbox
from IT_translationbox import Translationbox
import IT_YdTranslation


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__(QPixmap("ui/pic_resource/IT_startupScreen.png"))  # 启动程序的图片
        self.ID_and_key_file_name = "config/ID_and_key.txt"
        self.guide_file_name = "说明文档.txt"
        self.window = Loginbox()

    # 效果 fade =1 淡入   fade= 2  淡出，  t sleep 时间 毫秒
    def effect(self):
        self.setWindowOpacity(0)
        t = 0
        while t <= 50:
            new_opacity = self.windowOpacity() + 0.02  # 设置淡入
            if new_opacity > 1:
                break

            self.setWindowOpacity(new_opacity)
            self.show()
            t -= 1
            time.sleep(0.04)

        time.sleep(1)
        t = 0
        while t <= 50:
            new_opacity = self.windowOpacity() - 0.02  # 设置淡出
            if new_opacity < 0:
                break

            self.setWindowOpacity(new_opacity)
            t += 1
            time.sleep(0.04)

    def load_operation(self):
        # 新建说明文档
        if not os.path.exists(self.guide_file_name):
            guide_file = open(self.guide_file_name, "w", encoding="utf8")
            guide_file.write('''欢迎使用 I.T. (Instant Translation)!

_________________________________________________________________________________________________________________


注册：
    首次使用本程序需要前往“有道智云”官网进行注册来获取应用ID和应用密钥，具体方法如下：
    1、登陆官网(https://ai.youdao.com/login.s)，可选择QQ、微信、微博等账号进行注册登录；
    2、按照提示，输入手机号来获取验证码进行注册，完善信息，直至注册完成；
    3、新用户账户会有50元体验金可供使用，也可以添加客服微信再领取50体验金；
    4、在首页，选择左测栏目“应用管理”->“我的应用”来按要求填写创建新应用，其中“接入方式”为“API”；
    5、继续选择左测栏目“自然语言翻译”->“翻译实例”来按要求填写创建新实例，并将实例与上一步创建应用绑定；
    6、点进新创建应用的应用名称，可进入应用详细页面，从而获得“应用ID”与应用“密钥”，将两者填入登录框即可使用本程序。

_________________________________________________________________________________________________________________


使用方法：
    1、进入程序后，屏幕上方会悬浮一道白色的展示框，可通过鼠标拖动来调整其位置；
    2、查词：遇到任何陌生的英文单词，都可以通过将其“Ctrl + C”复制到剪切板来进行查询，但是带有破折号的词语以及一些专有名词（如：GitHub）可能无法查询；
    3、词组翻译/句子翻译：通过将其“Ctrl + C”复制到剪切板可翻译词组或是较短的句子，但是一些带有专有名词（如：GitHub）、特殊的标点符号（包括但不限于破折号）的句子可能无法进行翻译；
    4、生成生词本：通过使用快捷键“Ctrl + M”，可以选择路径生成生词本（“生词本.txt”），内含所有查询过的英文单词；
    5、程序一直于后台悬浮运行，不影响计算机上其他任务；如果想要退出程序，点击选中白色展示框后，使用快捷键“Esc”即可退出程序。

_________________________________________________________________________________________________________________


    任何用户在使用程序中出现问题或是对程序感兴趣的话，都可以联系我，我将尽我所能给予解答。（QQ: 1090671860）    
                    ''')
            guide_file.close()
        # 新建 config 文件夹
        if not os.path.exists("config"):
            os.makedirs('config')
        # 填写ID和密钥
        if os.path.exists(self.ID_and_key_file_name):
            # 非第一次登陆 检验密钥正确性
            ID_and_key_file = open(self.ID_and_key_file_name, "r", encoding="utf8")
            ID_and_key_list = ID_and_key_file.read().split(":")
            ID = ID_and_key_list[0]
            key = ID_and_key_list[1]
            try:
                result_json = IT_YdTranslation.en2chs("a", ID, key)
                result_dict = json.loads(result_json)
                if result_dict["errorCode"] == "0":
                    self.window = Translationbox()
                else:
                    raise Exception
            except:
                self.window = Loginbox()
        else:
            self.window = Loginbox()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splash = SplashScreen()
    splash.effect()
    app.processEvents()  # ＃设置启动画面不影响其他效果
    splash.load_operation()
    splash.window.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    splash.window.show()
    splash.finish(splash.window)  # 启动画面完成启动
    sys.exit(app.exec_())
