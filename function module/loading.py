# Coding: utf8
# 参考网址：https://www.cnblogs.com/zkqiang/p/10515134.html
# 参考网址：https://www.jianshu.com/p/0a48dbd7004d
# 参考网址：https://blog.csdn.net/dataastron/article/details/79049039


import time
import sys


'''
# 使用 progress bar 来显示进度条
from progress.bar import Bar

bar = Bar('?', max=100, fill='@', suffix='%(percent)d%%')
for i in range(200):
    time.sleep(0.1)
    bar.next()
bar.finish()
'''


'''
# 使用 progress 来显示加载中
from progress.spinner import Spinner

spinner = Spinner('正在奋力下载中')
n = 100
while n > 0:
    # Do some work
    n = n - 1
    time.sleep(0.1)
    spinner.next()
'''


'''
# 使用 tqdm 来实现进度条
# 问题：无法单行刷新
from tqdm import tqdm

try:
    with tqdm(range(1000)) as t:
        for i in t:
            time.sleep(0.01)
except KeyboardInterrupt:
    t.close()
    raise
t.close()
'''



# 自己实现进度条(原理)
# n 总任务数量
n = 24
sys.stdout.write("  0%|                                                  | {0}/{1}".format(0, n))
sys.stdout.flush()
for i in range(n):  
    time.sleep(1)
    sys.stdout.write('   \r')
    sys.stdout.flush()
    percent_num = (i + 1) * 100 // n
    if percent_num < 10:
        sys.stdout.write("  ")
    elif percent_num < 100:
        sys.stdout.write(" ")
    else:
        pass
    sys.stdout.write('{0}%|'.format(percent_num))
    for j in range(percent_num // 4):
        sys.stdout.write("█")
    for k in range(25 - percent_num // 4):
        sys.stdout.write("  ")
    sys.stdout.write("| {0}/{1}".format(i + 1, n))
    sys.stdout.flush()



'''
# 自己实现加载中(原理)
# n 总任务数量
n = 240
label = "准备中"
sys.stdout.write(label + " | ")
sys.stdout.flush()
i = 0
while i < n:  
    time.sleep(0.5)
    sys.stdout.write('   \r')
    sys.stdout.flush()
    sys.stdout.write(label)
    if i % 4 == 0:
        sys.stdout.write(" / ")
    elif i % 4 == 1:
        sys.stdout.write(" - ")
    elif i % 4 == 2:
        sys.stdout.write(" \\ ")
    else:
        sys.stdout.write(" | ")
    sys.stdout.flush()
    i += 1
'''