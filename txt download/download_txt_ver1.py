# Coding: utf8
# ver1 相对于 ver2 更适用于继续下载，全文下载稍有不便

import requests
import os
import time 
import datetime
import sys
from progress.spinner import Spinner

print("输入小说名：")
txt_name = input() # 保存文件名
print("输入起始章节下载网址：")
txt_url = input() # 小说起始网址


# 创建文件用于存储
txt_save_dir = "txt_save" # 文件夹名
if not os.path.exists(txt_save_dir):
    os.mkdir(txt_save_dir)
txt_file_address = txt_save_dir + "/" + txt_name + ".txt"
if os.path.exists(txt_file_address):
    txt_save_file = open(txt_file_address, "a", encoding = "utf-8") # 若已存在则是继续下载模式，否则新建下载
else:
    txt_save_file = open(txt_file_address, "w", encoding = "utf-8") 

# 开始下载
start_time = datetime.datetime.now() # 起始时间
print()
spinner = Spinner('正在奋力下载中') # 进度条
while txt_url.find("html") != -1: # 判断是否到了末尾章节，即结束标志
    # 爬取小说源代码
    try:
        txt_page = requests.get(txt_url) # 这里爬取时可能出现连接失败的异常
    except:
        print("连接超时！正在进行第一次重连...")
        time.sleep(3) # 三秒后进行第一次重连
        try:
            txt_page = requests.get(txt_url)
        except:
            print("连接超时！正在进行第二次重连...")
            time.sleep(3) # 三秒后进行第二次重连
            try:
                txt_page = requests.get(txt_url)
            except:
                print("连接超时！正在进行第三次重连...")
                time.sleep(3) # 三秒后进行第二次重连
                try:
                    txt_page = requests.get(txt_url)
                except:
                    print("\n重连失败，下载中断！\n下一章网址为：\n" + txt_url)
                    txt_save_file.close()
                    # 结束时间
                    end_time = datetime.datetime.now()
                    # 用时结果
                    second = end_time.second - start_time.second
                    minute = end_time.minute - start_time.minute
                    hour = end_time.hour - start_time.hour
                    if second < 0:
                        second += 60
                        minute -= 1
                    if minute < 0:
                        minute += 60
                        hour -= 1
                    if hour < 0:
                        hour += 24
                    print("下载用时: {0}时{1}分{2}秒".format(hour, minute, second))
                    # 保存下载记录
                    if os.path.exists("log.txt"):
                        log_file = open("log.txt", "a", encoding = "utf-8")
                    else:
                        log_file = open("log.txt", "w", encoding = "utf-8")
                    # 打印日期时间
                    now_time = time.strftime("%Y.%m.%d %H:%M:%S")
                    log_file.write(now_time + ":\n")
                    log_file.write("下载小说《{0}》中断！\n下一章网址为：\n{1}\n下载用时: {2}时{3}分{4}秒\n\n".format(txt_name, txt_url, hour, minute, second))
                    log_file.close()
                    sys.exit()
                
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
    ## 抓下一章url
    txt_flag6 = '" target="_top" class="next">下一章</a>'
    txt_source = txt_source[0:txt_source.find(txt_flag6)]
    txt_flag7 = '<a href="'
    txt_url = "https://wujixiaoshuo.com" + txt_source[txt_source.rfind(txt_flag7) + len(txt_flag7):]
    spinner.next()

# 完成存储
txt_save_file.write("<全书完>")
txt_save_file.close()

# 计时
## 结束时间
end_time = datetime.datetime.now()
## 计算用时结果
second = end_time.second - start_time.second
minute = end_time.minute - start_time.minute
hour = end_time.hour - start_time.hour
if second < 0:
    second += 60
    minute -= 1
if minute < 0:
    minute += 60
    hour -= 1
if hour < 0:
    hour += 24
print("\n下载完毕！\n下载用时: {0}时{1}分{2}秒".format(hour, minute, second))

# 保存下载记录
if os.path.exists("log.txt"):
    log_file = open("log.txt", "a", encoding = "utf-8")
else:
    log_file = open("log.txt", "w", encoding = "utf-8")
# 打印日期时间
now_time = time.strftime("%Y.%m.%d %H:%M:%S")
log_file.write(now_time + ":\n")
log_file.write("下载小说《{0}》成功！\n下载用时: {1}时{2}分{3}秒\n\n".format(txt_name, hour, minute, second))
log_file.close()