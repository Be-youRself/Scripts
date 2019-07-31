# Coding: utf-8
# 创建进程窗口

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.createProcess_ui import Ui_CreateProcess
import mainWindow
import inputPara
import os


class CreateProcess(QtWidgets.QMainWindow, Ui_CreateProcess):  # 多态继承界面类来添加逻辑
    def __init__(self, parent=None):
        super(CreateProcess, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/image/PC.ico'))
        self.setStyleSheet('''#CreateProcess{border-image: url(ui/image/bg_img.jpg);}''')  # 设置自适应背景
        self.configurationData = {"Resource": 5, "Ready": 2, "Ready_time": [2, 3]}  # 初始值是默认参数
        self.read_configuration()
        self.load_para()
        self.Sure.clicked.connect(self.input_create_para)
        self.Restart.clicked.connect(self.op_mainWindow)

    def read_configuration(self):
        # 读入配置文件中的参数，若出错就读入默认参数
        try:
            configuration_file = open("configuration_file.txt", "r", encoding="utf8")
            # 读取参数并进行判别
            while True:
                line = configuration_file.readline()
                if len(line) == 0:  # 即便是空行，仍然有换行符，因此可以读完整个文件。
                    break
                if line[0: 2] == "//" or line == "\n":  # 跳过配置文件中的注释和空行
                    continue
                key_value = line.split(":")  # 分割键值为一个两元素列表
                if len(key_value) == 2:
                    self.check_config_para(key_value)
            configuration_file.close()
            if len(self.configurationData["Ready_time"]) != self.configurationData["Ready"]:  # 最后再检查一下就绪队列时间片是否与数量相匹配
                # 不匹配则重置就绪队列参数
                self.configurationData["Ready"] = 2
                self.configurationData["Ready_time"] = [2, 3]

            self.ReadResult.setText("已载入给定的合法参数！")
        except Exception:  # 读取出错（参数文件有错或文件不存在）
            self.configurationData = {"Resource": 5, "Ready": 2, "Ready_time": [2, 3]}  # 重新赋值一次避免出现异常前有数据存储
            self.ReadResult.setText("读取配置文件参数失败！已使用默认参数！")

    def check_config_para(self, key_value):
        # 用来检验是否使用配置文件中的参数
        # key_value 接受一个包含 key 与 value 的两元素列表
        # 若后面要添加配置参数，直接在本函数修改，再在字典中添加键就可
        key = key_value[0].strip()
        value = key_value[1].strip()
        if key == "Resource":
            value = int(value)  # 若类型不正确就会抛出异常
            if 1 <= value <= 10:
                self.configurationData["Resource"] = value
            return 0
        if key == "Ready":
            value = int(value)  # 若类型不正确就会抛出异常
            if 1 <= value <= 5:
                self.configurationData["Ready"] = value
            return 0
        if key == "Ready_time":
            value = eval(value)
            # 当出现时间片配置参数不正确的情况时，不用立刻更改就绪队列数量参数
            # 统一留到 read_configuration 函数中所有配置参数都读完了，最后再进行检验并作相应更改
            if type(value) != list:  # 参数形式不正确(不为列表)时不进行赋值操作
                return 0
            if len(value) != self.configurationData["Ready"]:  # 输入时间片与队列数量不匹配
                return 0
            else:
                # 检验每个时间片是否都在规定范围内
                flag = 0  # 标记是否有时间片不符合规定(1: 有；0：无)
                for i in value:
                    i = int(i)  # 转换一下类型来判断是否配置文件的值是否输入错误
                    if i > 10 or i < 1:
                        flag = 1
                if flag == 0:  # 无错才赋值
                    self.configurationData["Ready_time"] = value

    def load_para(self):
        # 将设置的参数载入显示到界面中
        # 可用 PCB 资源
        resource_PCB = self.configurationData["Resource"]
        self.FreeNum.setText(str(resource_PCB))
        # 加载进程选择下拉列表
        for i in range(resource_PCB):
            self.ProcessNum.addItem(str(i + 1))

    def input_create_para(self):
        # 打开进程创建窗口，同时会关闭本窗口，进行数据交互
        nowCreate = self.ProcessNum.currentText()  # 当前已经创建的进程数
        saveData = {"nowCreate": nowCreate, "configurationData": self.configurationData}  # 字典存储的用于交互的数据
        # 将数据存入文件 data/temp.txt
        # 检查是否有该目录 否则创建目录
        if not os.path.isdir("data"):
            os.mkdir("data")
        saveDataFile = open("data/temp.txt", "w", encoding="utf8")
        saveDataFile.write(str(saveData))
        saveDataFile.close()
        # 打开输入创建进程信息窗口
        self.w_inputPara = inputPara.InputPara()
        self.w_inputPara.show()
        # 关闭当前窗口
        self.close()

    def op_mainWindow(self):
        # 打开开始窗口，重新开始程序
        self.w_mainWindow = mainWindow.MainWindow()
        self.w_mainWindow.show()
        self.close()
