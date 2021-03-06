# Filename: igxe_ver2.py
# 从want.txt文件获取想要搜索的饰品信息
# 获取最低价格

import requests
import time

# 从文件读取饰品信息并存入列表
searchList = []
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
    if(searchList[i].rfind("\n") != -1):
        searchList[i] = searchList[i][0: searchList[i].rfind("\n")]

# 打印日期时间
file_w = open("igxe.txt", "a", encoding="utf-8")
now_time = time.strftime("%Y.%m.%d %H:%M:%S")
file_w.write(now_time + ":\n")

# 获取价格并打印
for i in range(0, len(searchList)):
    search = searchList[i]
    # 从网页源代码获取信息
    # 获取网页源代码
    igxe_website = "https://www.igxe.cn/csgo/730?keyword=" + search
    igxe = requests.get(igxe_website)
    igxe_source = str(igxe.content, encoding = "utf-8")

    # 处理所得字符串
    # 定位到商品区域
    ref_1 = 'title="' + search + '"'
    ind_1 = igxe_source.find(ref_1)

    # 定位到价格区域
    ref_2 = '''<div class="price fl"><sup>￥</sup>
                                                    <span>'''
    ind_2 = igxe_source.find(ref_2, ind_1)

    ref_3 = '''</span>
                                                    <sub>'''
    ind_3 = igxe_source.find(ref_3, ind_2, ind_2 + 300)

    # 获取价格
    price = "￥" + igxe_source[ind_2 + len(ref_2): ind_3] + igxe_source[ind_3 + len(ref_3): ind_3 + len(ref_3) + 2]

    # 存储价格到文件
    file_w.write(search + "       " + price + "\n")

# 打印间隔
file_w.write("\n\n\n")
file_w.close()
