# Filename: Medium_access_control.py
# Coding: utf8
import sys
import threading
import random
import time

# 线程类用来模拟总线抢占情况
class Using_condition_thread(threading.Thread):
    isUsed = 0
    user = ""
    def run(self):
        while 1:
            self.isUsed = 0
            if random.random() < 0.3: # 占用概率为30%
                self.user = random.choice('BCD')
                self.isUsed = 1
            time.sleep(random.random() / 10) # 总线被一次占用时间(小于 100 ms)

print('''模拟 MAC 中 CSMA/CD 方法：
1.设置四个节点 A、B、C、D
2.节点竞争采用随机竞争，先到先得
3.使用 A 节点进行数据发送
4.发送失败等待三秒后重发
''')

# 采用字典来表示邻接表
node_graph = {"A":["B", "C", "D"],
         "B":["A", "C", "D"],
         "C":["A", "B", "D"],
         "D":["A", "B", "C"]}

print("拓扑结构如下：\n")
for node in node_graph:
    print(node + " ——", end=' ')
    for next_node in node_graph[node]:
        print(next_node, end=' ')
    print("")
print()

# 生成新线程来模拟总线占用情况
using_condition_thread = Using_condition_thread()
using_condition_thread.setDaemon(True) # 随主线程结束而结束
using_condition_thread.start()

msg_send = input("请输入想要发送的数据：")
# 随机选择节点来发送这段数据
print("A节点即将发送该数据:\n")

isUsed = 0
user = ''
while 1:
    # 发送前进行侦听
    print("侦听总线...")
    time.sleep(1)
    while 1:
        isUsed = using_condition_thread.isUsed
        user = using_condition_thread.user
        if isUsed == 0:
            print("总线空闲，开始发送数据...")
            break
        print(user + " 节点正在发送数据，总线正忙，等待中...")
        time.sleep(3)

    # 开始发送数据
    time.sleep(2)
    isUsed = using_condition_thread.isUsed
    user = using_condition_thread.user
    if isUsed == 0:
        print("发送成功！发送结果如下：")
        for next_node in node_graph["A"]:
            print(next_node + " 已接收 " + msg_send)
        break
    else:
        print("发送数据时与 {0} 节点发生冲突！发送失败！等待重新发送...".format(user))
        time.sleep(3)

sys.exit(0)


