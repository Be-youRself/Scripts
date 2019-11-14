# 用于测试模块功能是否正确

import requests
import os
import time 
import datetime
import sys

print("输入小说首页网址：")
txt_homepage = input() # 小说起始网址

# 处理首页 获得小说名和首章url 这一段的变量会被后续程序重复使用
## 获取源代码
try:
    txt_page = requests.get(txt_homepage) # 这里爬取时可能出现连接失败的异常
except:
    print("连接超时！正在进行第一次重连...")
    time.sleep(3) # 三秒后进行第一次重连
    try:
        txt_page = requests.get(txt_homepage) # 这里爬取时可能出现连接失败的异常
    except:
        print("连接超时！正在进行第二次重连...")
        time.sleep(3) # 三秒后进行第二次重连
        try:
            txt_page = requests.get(txt_homepage)
        except:
            print("连接超时！正在进行第三次重连...")
            time.sleep(3) # 三秒后进行第三次重连
            try:
                txt_page = requests.get(txt_homepage)
            except:
                print("重连失败！脚本自动退出！")
                sys.exit()
txt_source = str(txt_page.content, encoding = "utf-8")
## 定位小说名
txt_flag1 = '<meta property="og:title" content="'
txt_flag2 = '" />'
txt_source = txt_source[txt_source.find(txt_flag1):]
txt_name = txt_source[len(txt_flag1):txt_source.find(txt_flag2)].strip() # 获取小说名
## 定位章节列表区域
txt_flag3 = '正文</dt>'
txt_source = txt_source[txt_source.find(txt_flag3):]
## 获取章节数，即任务数量
txt_flag4 = '<dd> <a style="" href="'
mission_num = len(txt_source.split(txt_flag4)) - 1 # 获取任务数
## 获取首章url
txt_flag5 = '">'
txt_source = txt_source[txt_source.find(txt_flag4):]
txt_url = "https://wujixiaoshuo.com" + txt_source[len(txt_flag4):txt_source.find(txt_flag5)].strip() # 获取首章url

print(txt_name)
print(mission_num)
print(txt_url)
