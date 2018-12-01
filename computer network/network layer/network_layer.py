# Filename: network_layer.py
# Coding: utf8

import time

# 使用字典表示网络拓扑并打印
network_topo = {"Route_1": {"Subnet_1": ["Node_1", "Node_2", "Node_3"]},
                "Route_2": {"Subnet_2": ["Node_4", "Node_5", "Node_6"]},
                "Route_3": {"Subnet_3": ["Node_7", "Node_8", "Node_9"]}}
print("网络拓扑结构为：")
flag = 0
for i in network_topo:
    if flag == 0:
        flag = 1
    else:
        print("\n  |  ", end="")
    print("\n" + i + "----", end="")
    for j in network_topo[i]:
        print(j + "----", end="")
        for k in network_topo[i][j]:
            print(k + "  ", end="")
print("\n")

# 初始化
## 分配 IP 地址
### IP 地址格式为 202.1.[子网号].[主机号]
### 为了简便 路由器只赋值子网号 节点只赋值主机号
IP_address = {}
IP_address["Route_1"] = 1;
IP_address["Node_1"] = 11;
IP_address["Node_2"] = 12;
IP_address["Node_3"] = 13;
IP_address["Route_2"] = 2;
IP_address["Node_4"] = 21;
IP_address["Node_5"] = 22;
IP_address["Node_6"] = 23;
IP_address["Route_3"] = 3;
IP_address["Node_7"] = 31;
IP_address["Node_8"] = 32;
IP_address["Node_9"] = 33;

## 分配路由表
### 格式为 目标地址 下一跳地址 端口
### 直接转发为"-" 转发网络号简单表示
route_table = {"Route_1": [[1, "-", "R1"], [2, "2", "D1"], [3, "2", "D1"]],
               "Route_2": [[1, "1", "U2"], [2, "-", "R2"], [3, "3", "D2"]],
               "Route_3": [[1, "2", "U1"], [2, "2", "U1"], [3, "-", "R1"]]}

## IP 分组
### 格式为 目标节点地址 跳数 传输数据
Ob_address = ""
hop = 0
data = ""

# 传输数据
## 输入
quit = ""
while(quit != "q"):
    flag = 0
    hop = 0
    while flag == 0:
        send = input("请输入发送的节点：")
        data = input("请输入发送的数据：")
        recv = input("请输入目标节点：")
        print()

        # 检测发送节点与目标节点是否合法
        if send not in IP_address:
            flag_send = 0
            print("发送节点不存在！")
        else:
            flag_send = 1
        if recv not in IP_address:
            flag_recv = 0
            print("接收节点不存在！")
        else:
            flag_recv = 1
        if flag_send == 0 or flag_recv == 0:
            print("重新输入！\n")
        else:
            flag = 1
    ## 计算相应网络号和 IP 地址
    send_subnet = int(IP_address[send] / 10)
    send_host = IP_address[send] % 10
    send_address = "202.1." + str(send_subnet) + "." + str(send_host)
    recv_subnet = int(IP_address[recv] / 10)
    recv_host = IP_address[recv] % 10
    recv_address = "202.1." + str(recv_subnet) + "." + str(recv_host)
    print("源节点 IP 地址为: " + send_address)
    print()

    ##　转发分组
    # 第一个路由器 IP 地址
    flag = 0
    tran_address = send_address + " -> "
    route_subnet = send_subnet
    route_address = "202.1."+ str(route_subnet) + ".0"
    route = "Route_" + str(route_subnet)
    print("转发过程：\n")
    print("转发开始...")
    time.sleep(3)
    print("交付至路由器——Route_" + str(route_subnet),end="")
    hop = hop + 1
    print("， 路由器存储 IP 分组为：{0} - {1} - {2}...".format(recv_address, hop, data))
    time.sleep(3)
    tran_address = tran_address + route_address + " -> "
    while route_subnet != recv_subnet:
        # 查询路由表
        for i in route_table[route]:
            if i[0] == recv_subnet:
                route_subnet = int(i[1])
                route_address = "202.1." + str(route_subnet) + ".0"
                route = "Route_" + str(route_subnet)
        print("交付至路由器——Route_" + str(route_subnet), end="")
        hop = hop + 1
        print("， 路由器存储 IP 分组为：{0} - {1} - {2}...".format(recv_address, hop, data))
        time.sleep(3)
        tran_address = tran_address + route_address + " -> "
        # 防止循环转发
        if hop >= 10:
            print("转发次数过多，数据传送失败！")
            flag = 1
            break
    if flag == 0:
        print("可直接交付至——" + recv)
        tran_address = tran_address + recv_address
        print("传输完毕！\n")
        print("转发路径为：")
        print(tran_address)

    # 一次传输完毕
    quit = input("\n输入q退出，输入任意键继续发送：")
    if quit == "q":
        print("感谢使用，程序已退出！")


