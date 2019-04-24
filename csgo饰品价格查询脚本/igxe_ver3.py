# Filename: igxe_ver3.py
# 从want.txt文件获取想要搜索的饰品信息
# 获取最低价格
# 可以按页数进行彻底查找
# 解决了首页没有欲查找饰品导致查找失败的问题
# 若是网站没有该饰品或者输入名称出错则会返回正确报错

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
        igxe = requests.get(igxe_website)
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
        price = "￥" + igxe_source[ind_2 + len(ref_2): ind_3] + igxe_source[ind_3 + len(ref_3): ind_3 + len(ref_3) + 2]
    else:
        price = "未查找到该饰品！也可能是名称输入出错或者网站更新了！"

    # 存储价格到文件
    file_w.write(search + "       " + price + "\n")

# 打印间隔
file_w.write("\n\n\n")
file_w.close()
