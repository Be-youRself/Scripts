# Coding: utf8

import datetime
import time

start_time = datetime.datetime.now()

# 运行程序
time.sleep(300)

end_time = datetime.datetime.now()
# 给出结果
second = end_time.second - start_time.second
minute = end_time.minute - start_time.minute
hour = end_time.hour - start_time.hour
if second < 0:
    second += 60
    minute -= 1
if minute < 0:
    minute += 60
    hour -= 1
print("用时:{0}时{1}分{2}秒".format(hour, minute, second))