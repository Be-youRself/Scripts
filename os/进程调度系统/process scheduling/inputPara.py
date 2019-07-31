# Coding: utf-8
# 输入进程创建信息窗口
##### 这里一定要注意保存的临时文件数据有没有被篡改

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.inputPara_ui import Ui_InputPara
import mainWindow
import schedule
import time
import os


class InputPara(QtWidgets.QMainWindow, Ui_InputPara):  # 多态继承界面类来添加逻辑
    def __init__(self, parent=None):
        super(InputPara, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/image/PC.ico'))
        self.setStyleSheet('''#InputPara{border-image: url(ui/image/bg_img.jpg);}''')  # 设置自适应背景
        self.saveData = {}
        self.get_save_data()
        self.PCB = {}
        self.ready = {}
        self.init_resource()
        self.NeedTime.activated.connect(self.change_IO_time)
        self.IOTime.activated.connect(self.change_IO_last)
        self.Save.clicked.connect(self.save_PCB_data)
        self.StartSchedule.clicked.connect(self.start_schedule)
        self.Restart.clicked.connect(self.op_mainWindow)

    def get_save_data(self):
        # 读取交互数据
        try:
            readFile = open("data/temp.txt", "r", encoding="utf8")
            saveData = eval(readFile.read())
            if type(saveData) != dict:
                raise Exception("临时文件被篡改！")
            self.saveData = saveData
        except Exception:
            # 读取文件不正常
            self.abnormal_exit()
        finally:
            readFile.close()
            os.remove("data/temp.txt") # 读完了以后立刻删除，避免数据泄露

    def abnormal_exit(self):
        # 需要的临时文件不存在，程序异常退出
        # 删除临时文件
        ##### 写一个临时窗口来替代这个标签
        if os.path.exists("data/temp.txt"):
            os.remove("data/temp.txt")
        self.Warning.setText("临时文件被破坏！三秒后重启程序！")
        time.sleep(30)
        self.op_mainWindow()

    def init_resource(self):
        # 根据相应参数初始化 PCB 资源
        num_PCB = int(self.saveData["nowCreate"])
        for i in range(num_PCB):
            temp_name = "P" + str(i)
            # 用一个列表来表示 PCB，对应属性为：进程名、优先级、运行需要总时间、IO占用开始时刻、IO占用持续时间、已经运行时间、被调度次数、是否占用IO资源
            self.PCB[temp_name] = {"name": temp_name, "prior": "1", "need_time": "5", "IO_time": "None",
                                   "IO_last": "None",
                                   "run_time": "0", "schedule": "0", "occupy": "0"}

        # 根据相应参数初始化就绪队列
        num_ready = self.saveData["configurationData"]["Ready"]
        for i in range(num_ready):
            temp_name = "Ready_" + str(i + 1)
            self.ready[temp_name] = []
            if i == 0:
                for i in self.PCB:
                    self.ready[temp_name].append(i)

        # 初始化下拉菜单
        ##### 这里的运行总时间范围限制可以写入参数文件中！！！
        # 进程名
        for i in self.PCB:
            self.ProcessName.addItem(i)
        # 优先级
        for i in range(num_ready):
            self.Prior.addItem(str(i + 1))
        # 运行需要时间
        for i in range(15):  ##### 这个参数可以写入参数文件中！！！
            self.NeedTime.addItem(str(i + 1))
        # IO 起始时间
        self.IOTime.addItem("None")
        # IO 起始时间当前进程运行时间有关
        for i in range(int(self.NeedTime.currentText())):
            self.IOTime.addItem(str(i + 1))
        # IO 持续时间
        self.IOLast.addItem("None")

    def change_IO_time(self):
        # 实时改变 IO 起始时间下拉菜单
        self.IOTime.clear()
        self.IOTime.addItem("None")
        # IO 起始时间当前进程运行时间有关
        for i in range(int(self.NeedTime.currentText())):
            self.IOTime.addItem(str(i + 1))
        # 同时也要清除 IO 持续时间下拉菜单
        self.IOLast.clear()
        self.IOLast.addItem("None")

    def change_IO_last(self):
        # 实时改变 IO 持续时间下拉菜单
        self.IOLast.clear()
        if self.IOTime.currentText() == "None":
            self.IOLast.addItem("None")
        else:
            start_time = int(self.IOTime.currentText())
            need_time = int(self.NeedTime.currentText())
            for i in range(need_time - start_time + 1):
                self.IOLast.addItem(str(i + 1))

    def save_PCB_data(self):
        # 保存每个 PCB 的参数信息
        temp_name = self.ProcessName.currentText()
        temp_PCB = self.PCB[temp_name]
        # 从前一个就绪队列中删除这个PCB
        self.ready["Ready_" + temp_PCB["prior"]].remove(temp_name)
        # 修改优先级
        temp_PCB["prior"] = self.Prior.currentText()
        # 在新的队列中添加这个PCB
        self.ready["Ready_" + self.Prior.currentText()].append(temp_name)
        # 修改运行总时间
        temp_PCB["need_time"] = self.NeedTime.currentText()
        # 修改 IO 起始与终止时间
        temp_PCB["IO_time"] = self.IOTime.currentText()
        temp_PCB["IO_last"] = self.IOLast.currentText()

    def start_schedule(self):
        # 开始进行调度
        # 对于就绪队列进行排序
        for i in self.ready:
            self.ready[i].sort()
        # 保存当前所有信息
        self.saveData["PCB"] = self.PCB
        self.saveData["ready"] = self.ready
        # 将数据存入文件 data/temp.txt
        # 检查是否有该目录 否则创建目录
        if not os.path.isdir("data"):
            os.mkdir("data")
        saveDataFile = open("data/temp.txt", "w", encoding="utf8")
        saveDataFile.write(str(self.saveData))
        saveDataFile.close()
        # 打开输入创建进程信息窗口
        self.w_schedule = schedule.Schedule()
        self.w_schedule.show()
        # 关闭当前窗口
        self.close()

    def op_mainWindow(self):
        # 打开开始窗口，重新开始程序
        self.w_mainWindow = mainWindow.MainWindow()
        self.w_mainWindow.show()
        self.close()
