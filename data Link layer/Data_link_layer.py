# Data_link.py

import math
import re
import time

def check(data, check_mul):
    # 进行校验 返回余数
    return data % check_mul

# 协议介绍
print('''数据链路层协议说明：
      1、将传输数据按每四个字节分割成一帧
      2、采用滑动窗口协议，窗口大小为四，即一次最多传输四帧、
      3、帧分为数据帧与控制帧
      4、数据帧由序号字段、信息字段、校验字段组成
      5.采用余数校验方式 生成多项式采用 100000000
    ''')

# 获取要传输文件数据
#send_filename = input("输入想要传输文件名: ")
send_filename = "1.txt"
send_file = open("1.txt", "rb") ###########################
send_data = send_file.read()
send_file.close()

# 传输前准备
print("欲传输数据长度为{0}byte(s)，分割为{1}个数据帧。".format(len(send_data), math.ceil(len(send_data) / 4))) # math.ceil 函数向上取整&格式化输出
print("开始传输：")
send_index = 1
send_check = []
check_mul = 0b100000000 # 生成多项式
data = 0
for i in range(0, len(send_data), 4):
    # 每一个数据帧
    # 判断是不是最后一个数据帧
    if(i + 4 >= len(send_data)):
        times = len(send_data) - i
    else:
        times = 4
    for j in range(0, times):
        data = (data << 8) + send_data[i + j] # << 优先级低于 +
    send_check.apend(check(data,check_mul))
    send_str = (send_index)
    send_index = send_index + 1

# 传输

# 传输后处理
recv_data = b""
for i in send_data:
    # 这里 i 是 int 类型的单字节数据(i 等价于 send_data[index])
    recv_data = recv_data + bytes([i]) # byte([int]) 把 int 类型转换成字节型再累加成字节流



# 将接受数据存储为文件
recv_filename = time.strftime("%Y%m%d%H%M%S") + re.search(r"\..*", send_filename).group()
recv_file = open(recv_filename, "wb")
recv_file.write(recv_data)
recv_file.close()