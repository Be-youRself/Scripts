# Data_link_layer.py

import math
import random
import re
import time

def generate_check(data, check_mul):
    # 进行校验 返回校验码
    return data % check_mul

# 协议介绍
print('''简单数据链路层协议说明：
      1、将传输数据按每四个字节分割成一帧
      2、采用滑动窗口协议 窗口大小为四 即一次最多传输四帧
      3、帧分为数据帧与控制帧
      4、数据帧由序号字段-信息字段-校验字段组成
      5.采用余数校验方式 生成多项式采用 100000000
      6.传输过程 帧用十六进制显示
      7.出现错误帧采用SR方式重发
      8.出现错误帧的概率为 5%''')

# 获取要传输文件数据
send_filename = input("输入想要传输文件名: ")
send_file = open(send_filename, "rb") 
send_data = send_file.read()
send_file.close()

# 传输前准备
print("欲传输数据长度为{0}byte(s)，分割为{1}个数据帧。".format(len(send_data), math.ceil(len(send_data) / 4))) # math.ceil 函数向上取整&格式化输出
print("开始传输：\n")
send_index = 0
send_check = []
send_message = []
check_mul = 0b100000000 # 生成多项式
for i in range(0, len(send_data), 4):
    # 每一个数据帧
    data = 0
    send_index = send_index + 1
    # 判断是不是最后一个数据帧
    if (i + 4) >= len(send_data):
        times_byte = len(send_data) - i
    else:
        times_byte = 4
    for j in range(0, times_byte):
        data = (data << 8) + send_data[i + j] # << 优先级低于 +
    send_message.append(data)
    send_check.append(generate_check(data,check_mul))

# 建立链路
show_indent = "                                 "
print("Send                             Recv")
print("-------------------------------------------------------------")
print("U, SNRM")
print(show_indent + "U, UA")

# 传输数据
recv_data = b""
for i in range(0, send_index, 4):
    # 发送
    # 判断是不是最后一组数据帧
    if (i + 4) >= send_index:
        times_frame = send_index - i
    else:
        times_frame = 4
    for j in range(0, times_frame):
        send_str = "{0} {1} {2}".format(hex(i + j + 1), hex(send_message[i + j]), hex(send_check[i + j]))
        print(send_str)
    # 接收
    buff_bytes = [-1, -1, -1, -1] # 设置缓存
    resend_list = []
    for j in range(0, times_frame):
        if random.random() < 0.05: # 出错概率为 5%
            data = send_message[i + j] + 1
        else:
            data = send_message[i + j]
        if generate_check(data, check_mul) == send_check[i + j]:
            # 存入缓存
            buff_bytes[j] = i + j
            print(show_indent + "ACK {}".format(hex(i + j + 1)))
        else:
            resend_list.append(i + j)
            print(show_indent + "NAK {}".format(hex(i + j + 1)))
    # 出错采用SR重发
    while resend_list != [] :
        for k in resend_list:
            send_str = "{0} {1} {2}".format(hex(k + 1), hex(send_message[k]), hex(send_check[k]))
            print(send_str)
            if random.random() < 0.05: # 出错概率为 5%
                data = send_message[k] + 1
            else:
                data = send_message[k]
            if generate_check(data, check_mul) == send_check[k]:
                buff_bytes[k - i] = k
                resend_list.remove(k)
                print(show_indent + "ACK {}".format(hex(k + 1)))
            else:
                print(show_indent + "NAK {}".format(hex(k + 1)))
    # 存储缓存中的数据
    for frame_index in buff_bytes:
        if frame_index != -1:
            byte_index = 4 * frame_index
            if (byte_index + 4) >= len(send_data):
                times_byte = len(send_data) - byte_index
            else:
                times_byte = 4
            for g in range(times_byte):
                recv_data = recv_data + bytes([send_data[g + byte_index]]) # 整型转换成字节型

# 拆除链路
print("U, DISC")
print(show_indent + "U, UA")

# 将接受数据存储为文件
recv_filename = time.strftime("%Y%m%d%H%M%S") + re.search(r"\..*", send_filename).group()
recv_file = open(recv_filename, "wb")
recv_file.write(recv_data)
recv_file.close()
print("\n接收数据已保存为{0}文件\n数据传输完成!".format(recv_filename))