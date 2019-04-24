# Filename: igxe_ver3.py
# 从want.txt文件获取想要搜索的饰品信息
# 获取最低价格
# 可以按页数进行彻底查找
# 解决了首页没有欲查找饰品导致查找失败的问题
# 若是网站没有该饰品或者输入名称出错则会返回正确报错
# 正确处理无want.txt文件或者want.txt文件为空的情况
# 处理饰品名称首尾空格、制表符、回车以解决名称格式不当的卡死问题
# 添加低价提醒功能
# 统一了输出格式 使得结果更清晰
# 统一字符格式通过将字符串转换成“GBK”格式的字节来计算其宽度
# 即len(bytes(a, encoding="GBK"))
# 或len(list(a.encode("GBK")))
# 进行无网络连接时候卡死的异常处理

import requests
import time
import os
import sys

# 从文件读取饰品信息并存入列表
searchList = []

file_r = open("want.txt", "a") # 若没有则相当于创建文件
file_r.close()

file_r = open("want.txt")
# 打开文件的字符编码要与文件记录相同 否则出现乱码不能正确读取
# 默认参数打开ANSI的txt文件
# 若读取UTF-8 文件中首行开头会有特殊转义字符 需要另外处理
while True:
    line = file_r.readline()
    if len(line) == 0:
        break
    searchList.append(line)
file_r.close()

# 消除饰品名称末尾换行符
for i in range(0, len(searchList)):
    # range 包括 begin 不包括 end
    searchList[i].replace("\t","") # 处理制表符
    searchList[i].replace("\n","") # 处理句末回车
    searchList[i] = searchList[i].strip() # 处理首尾空格

j = 0
for i in range(0, len(searchList)):
    if searchList[j] == "":
        del searchList[j] # 删除空元素
        j = j - 1
    j = j + 1

file_w = open("igxe.txt", "a", encoding="utf-8")
# 对于文件无内容进行处理
if len(searchList) == 0:
    file_r = open("want.txt", "w")
    file_r.write("蝴蝶刀（★）")
    file_r.close()
    searchList = ["蝴蝶刀（★）"]
    file_w.write("提示：未检索到欲搜索饰品名称，已写入默认值，可于want.txt文件进行更改！\n")

# 打印日期时间
now_time = time.strftime("%Y.%m.%d %H:%M:%S")
file_w.write(now_time + ":\n")

priceAlert = 0
wantPrice = 0
# 获取价格并打印
for i in range(0, len(searchList)):
    if searchList[i].find("￥") != -1: # 判断是否使用了价格提醒
        search = searchList[i].split("￥")[0].strip()
        try:
            wantPrice = float(searchList[i].split("￥")[1].strip())
        except ValueError:
            file_w.write(search)
            # 输出空格保证格式统一
            for j in range(0, 40 - len(list(search.encode('gbk')))):
                file_w.write(" ")
            file_w.write("输入格式有误，低价提醒功能出错！\n")
            continue
    else:
        search = searchList[i]
    page = 1
    # 设置循环判断状态码 endPage
    # 0表示循环中
    # 1表示出错
    # 2表示正常获取价格
    endPage = 0
    while endPage != 1 and endPage != 2:
        # 从网页源代码获取信息
        # 获取网页源代码
        igxe_website = "https://www.igxe.cn/csgo/730?is_buying=0&is_stattrak%5B%5D=0&is_stattrak%5B%5D=0&keyword=" + search + "&sort=0&ctg_id=0&type_id=0&page_no=" + str(page) + "&page_size=20&rarity_id=0&exterior_id=0&quality_id=0&capsule_id=0"
        # 对于网络未连接进行异常处理
        try:
            igxe = requests.get(igxe_website)
        except Exception:
            file_w.write("网络出现错误，连接失败！脚本已退出！\n\n\n\n")
            sys.exit()
        igxe_source = str(igxe.content, encoding = "utf-8") 

        # 处理所得字符串
        # 定位到商品区域
        ref_1 = 'title="' + search + '"'
        ind_1 = igxe_source.find(ref_1) 

        # 判断该页有没有这个商品
        if ind_1 == -1:
            # 到达最后一页
            if igxe_source.find("<!--没有数据-->") != -1:
                endPage = 1
            page = page + 1   
            continue    

        # 定位到价格区域
        ref_2 = '''<div class="price fl"><sup>￥</sup>
                                                    <span>'''
        ind_2 = igxe_source.find(ref_2, ind_1)  
        if ind_2 == -1:
            # 未能正确查找关键字 网站发生变化
            endPage = 1
            continue

        ref_3 = '''</span>
                                                    <sub>'''
        ind_3 = igxe_source.find(ref_3, ind_2, ind_2 + 300)
        if ind_3 == -1:
            # 未能正确查找关键字 网站发生变化
            endPage = 1
            continue
        endPage = 2

    # 获取价格
    if endPage == 2:
        try:
            price = igxe_source[ind_2 + len(ref_2): ind_3] + igxe_source[ind_3 + len(ref_3): ind_3 + len(ref_3) + 2]
            priceFloat = float(price)
        except ValueError:
            file_w.write(search)
            # 输出空格保证格式统一
            for j in range(0, 40 - len(list(search.encode('gbk')))):
                file_w.write(" ")
            file_w.write("查询失败！(网站更新)\n")
            continue
        if wantPrice >= priceFloat: # 判断是否低价
        	priceAlert = i + 1
        result = "￥" + price
    else:
        result = "未查找到该饰品！(名称输入出错/网站更新)"

    # 存储价格到文件
    file_w.write(search)
    # 输出空格保证格式统一
    for j in range(0, 40 - len(list(search.encode('gbk')))):
        file_w.write(" ")
    file_w.write(result)
    # 低价标记
    if priceAlert == i + 1:
    	file_w.write("       " + "★★★低价★★★")
    file_w.write("\n")

# 打印间隔
file_w.write("\n\n\n")
file_w.close()

# 低价自动打开igxe.txt
if priceAlert > 0:
	os.system("igxe.txt")
