# Coding: utf8
# ver0 用于测试，下载单章小说并储存

import requests


print("输入起始章节下载网址：")
txt_url = input() # 小说起始网址

txt_save_file = open("test.txt", "w", encoding = "utf-8")

# 爬取小说源代码
txt_page = requests.get(txt_url) # 这里爬取时可能出现连接失败的异常            
txt_source = str(txt_page.content, encoding = "utf-8")

# 处理小说源代码
## 抓标题
txt_flag1 = '&gt;'
txt_flag2 = '</div>'
txt_source = txt_source[txt_source.rfind(txt_flag1):]
txt_title = txt_source[len(txt_flag1):txt_source.find(txt_flag2)].strip() # 标题
## 抓正文
txt_flag3 = 'https://wujixiaoshuo.com/最快更新！无广告！<br/><br/>'
txt_source = txt_source[txt_source.find(txt_flag3):]
txt_flag4 = '&nbsp;&nbsp;&nbsp;&nbsp;'
txt_flag5 = '<div align="center">'
txt_body = txt_source[txt_source.find(txt_flag4):txt_source.find(txt_flag5)] + "\n"
txt_source = txt_source[txt_source.find(txt_flag5):]
## 处理正文
txt_body = txt_body.replace("&nbsp;", " ")
txt_body = txt_body.replace("<br />", "\n")
## 存储该章节
txt_save_file.write(txt_title + "\n\n" + txt_body)
txt_save_file.close()


