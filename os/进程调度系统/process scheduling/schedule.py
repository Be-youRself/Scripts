# Coding: utf-8
# 进程调度窗口

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.schedule_ui import Ui_Schedule
import mainWindow
import os
import time


class Schedule(QtWidgets.QMainWindow, Ui_Schedule):  # 多态继承界面类来添加逻辑
    def __init__(self, parent=None):
        super(Schedule, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/image/PC.ico'))
        self.setStyleSheet('''#Schedule{border-image: url(ui/image/bg_img.jpg);}''')  # 设置自适应背景
        self.saveData = {}
        self.PCB = {}
        self.ready = {}
        self.ready_time = []
        self.running = {"now_process": {}, "need_time": 0, "run_time": 0}  # 用于判断就绪队列绑定的时间片是否运行完毕
        self.IO_resource = ""  # 默认只有一个 IO 资源，为空则资源未被占用，被占用时值等于被占用进程名
        self.blocked = []  # 用于放置阻塞进程的队列
        self.finished = []  # 用于放置运行完毕的队列
        self.init_information = ""
        self.get_save_data()
        self.init_resource()
        self.Next.clicked.connect(self.schedule_process)
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
        # 完成界面资源初始化工作
        self.load_data()
        self.print_init_information()
        # 载入第一个资源
        self.get_process_from_ready()
        # 打印状态
        self.print_schedule_information()
        # 存储到日志文件
        self.init_information = time.strftime("%Y.%m.%d %H:%M:%S") + " 记录：\n" + self.init_information  # 打印当前时间
        self.save_to_file(self.init_information)
        self.init_information = ""  # 重置信息

    def load_data(self):
        # 读入相应数据
        self.NowTime.setText("0")
        self.PCB = self.saveData["PCB"]
        self.ready = self.saveData["ready"]
        self.ready_time = self.saveData["configurationData"]["Ready_time"]

    def print_init_information(self):
        # 打印创建信息
        self.init_information = "创建进程成功，资源已成功分配!\n"
        self.init_information += "创建了 " + self.saveData["nowCreate"] + " 个进程，具体信息如下：\n"
        for i in self.PCB:
            self.init_information += "    " + i + "——优先级：" + self.PCB[i]["prior"] + "；运行时间：" + self.PCB[i][
                "need_time"] + \
                                     "；IO开始时刻：" + self.PCB[i]["IO_time"] + "；IO持续时间：" + self.PCB[i]["IO_last"] + "\n"
        self.init_information += "就绪队列具体信息如下：\n"
        for i in self.ready:
            self.init_information += "    " + i + ": "
            for j in range(len(self.ready[i])):
                if j != 0:
                    self.init_information += "、"
                self.init_information += self.ready[i][j]
            self.init_information += "\n"
        self.init_information += "\n"

    def save_to_file(self, log_information: str):
        # 将输出的日志保存到文件中
        # 将数据存入文件 data/log.txt
        # 检查是否有该目录 否则创建目录
        if not os.path.isdir("data"):
            os.mkdir("data")
        saveDataFile = open("data/log.txt", "a", encoding="utf8")
        saveDataFile.write(log_information)
        saveDataFile.close()

    def get_process_from_ready(self):
        # 从就绪队列中获取进程
        process_name = ""
        for i in self.ready:
            if len(self.ready[i]) != 0:
                process_name = self.ready[i][0]
                del self.ready[i][0]
                break
        if process_name == "":
            self.schedule_over()
        else:
            for i in self.PCB:
                if i == process_name:
                    temp_process = self.PCB[i]  # 加入运行队列
            self.running["now_process"] = temp_process
            ready_index = int(temp_process["prior"]) - 1
            self.running["need_time"] = int(self.ready_time[ready_index])
            self.running["run_time"] = 0
            temp_process["schedule"] = str(int(temp_process["schedule"]) + 1)  # 进程中被调度次数属性加一
            # 输出调度信息
            self.init_information += "进程 " + temp_process["name"] + " 从 " + temp_process["prior"] + " 号就绪队列中第 " + \
                                     temp_process["schedule"] + " 次被调度！进程具体信息如下：\n"
            self.init_information += "    " + temp_process["name"] + "——已经运行时间：" + temp_process["run_time"] + "；运行总时间：" \
                                     + temp_process["need_time"] + "；是否占用IO资源：" + str(
                bool(int(temp_process["occupy"]))) + "\n\n"

    def add_process_to_ready(self, temp_process: dict):
        # 将进程加入到就绪队列中
        # 判断优先级，若已经是最后的优先级了就再插到队尾
        prior = int(temp_process["prior"])
        if prior + 1 >= len(self.ready):
            prior = str(len(self.ready))
            ready_name = "Ready_" + prior
            temp_process["prior"] = str(len(self.ready))
        else:
            prior = str(prior + 1)
            ready_name = "Ready_" + prior
            temp_process["prior"] = str(int(temp_process["prior"]) + 1)
        self.ready[ready_name].append(temp_process["name"])
        self.init_information += "进程 " + temp_process["name"] + " 加入到 " + prior +" 号就绪队列中！\n\n"

    def schedule_process(self):
        # 主要的调度过程
        temp_process = self.running["now_process"]
        # 是否需要分配资源
        if temp_process["IO_time"] != "None" and temp_process["IO_time"] == str(int(temp_process["run_time"]) + 1) \
                and temp_process["occupy"] == "0":  # 放置从阻塞队列出来的进程情况
            if self.IO_resource == "":
                self.IO_resource = temp_process["name"]
                temp_process["occupy"] = "1"
            else:
                self.blocked.append(temp_process["name"])  # 加入阻塞队列
                self.init_information += "进程 " + temp_process["name"] + " 被阻塞！\n\n"
                # 重新调度一个
                self.get_process_from_ready()
                self.print_schedule_information()
                self.save_to_file(self.init_information)
                self.init_information = ""
                return 0
        # 运行一个时间片
        self.NowTime.setText(str(int(self.NowTime.text()) + 1))  # 主时间加一
        temp_process["run_time"] = str(int(temp_process["run_time"]) + 1)
        self.running["run_time"] += 1  # 执行时间加一
        if temp_process["occupy"] == "1":
            temp_process["IO_last"] = str(int(temp_process["IO_last"]) - 1)
        # 是否释放资源
        if temp_process["IO_time"] != "None" and temp_process["IO_last"] == "0":
            # 当前进程释放资源
            self.IO_resource = ""
            temp_process["occupy"] = "0"
            # 观察阻塞队列是否需要出队
            if len(self.blocked) != 0:
                get_resource_process_name = self.blocked[0]
                del self.blocked[0]
                self.init_information += "进程 " + get_resource_process_name + " 移除阻塞队列！\n\n"
                for i in self.PCB:
                    if i == get_resource_process_name:
                        get_resource_process = self.PCB[i]  # 加入运行队列
                self.IO_resource == get_resource_process_name
                get_resource_process["occupy"] = "1"
                self.add_process_to_ready(get_resource_process)
        # 当前进程是否运行完毕
        if temp_process["run_time"] == temp_process["need_time"]:
            self.finished.append(temp_process["name"])
            self.init_information += "进程 " + temp_process["name"] + " 运行完毕！\n\n"
            self.print_schedule_information()
            self.save_to_file(self.init_information)
            self.init_information = ""
            self.get_process_from_ready()
            return 0
        # 进行时间片是否运行完毕
        if self.running["run_time"] == self.running["need_time"]:
            self.print_schedule_information()
            self.save_to_file(self.init_information)
            self.init_information = ""
            self.add_process_to_ready(temp_process)
            self.get_process_from_ready()
            return 0
        self.print_schedule_information()
        self.save_to_file(self.init_information)
        self.init_information = ""  # 重置信息

    def print_schedule_information(self):
        # 用来打印每次调度的结果
        temp_process = self.running["now_process"]
        self.init_information += "第 " + self.NowTime.text() + " 个时间片:\n"
        self.init_information += "运行队列：\n"
        self.init_information += "    " + temp_process["name"] + "——已经运行时间：" + temp_process["run_time"] + "；运行总时间：" \
                                 + temp_process["need_time"] + "；是否占用IO资源：" + str(
            bool(int(temp_process["occupy"]))) + "\n"
        self.init_information += "就绪队列：\n"
        for i in self.ready:
            self.init_information += "    " + i + ": "
            for j in range(len(self.ready[i])):
                if j != 0:
                    self.init_information += "、"
                self.init_information += self.ready[i][j]
            self.init_information += "\n"
        self.init_information += "阻塞队列："
        for i in range(len(self.blocked)):
            if i != 0:
                self.init_information += "、"
            self.init_information += self.blocked[i]
        self.init_information += "\n完成队列："
        for i in range(len(self.finished)):
            if i != 0:
                self.init_information += "、"
            self.init_information += self.finished[i]
        self.init_information += "\n\n"
        # 输出到命令框
        self.ScheduleNote.setText(self.init_information)

    def schedule_over(self):
        # 所有进程调度完毕
        self.Next.setText("调度完毕")
        self.Next.clicked.connect(self.op_mainWindow)

    def op_mainWindow(self):
        # 打开开始窗口，重新开始程序
        self.w_mainWindow = mainWindow.MainWindow()
        self.w_mainWindow.show()
        self.close()
