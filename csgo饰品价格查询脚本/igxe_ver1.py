# Filename: igxe_per1.py
# 获取爪子刀（★）（search）的最低价格

import requests
import time

# 从网页源代码获取信息
# 获取网页源代码
search = "爪子刀（★）"
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

#存储到文件
file_w = open("igxe.txt", "a", encoding="utf-8")
now_time = time.strftime("%Y.%m.%d %H:%M:%S")
file_w.write(now_time + ":\n")
file_w.write(search + "       " + price + "\n\n")
file_w.close()
