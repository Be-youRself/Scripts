# Coding: utf8
# 参考网址：https://www.cnblogs.com/zkqiang/p/10515134.html

'''
import time
from progress.bar import Bar

bar = Bar('?', max=100, fill='@', suffix='%(percent)d%%')
for i in range(200):
    time.sleep(0.1)
    bar.next()
bar.finish()
'''



from progress.spinner import Spinner
import time

spinner = Spinner('正在奋力下载中')
n = 100
while n > 0:
    # Do some work
    n = n - 1
    time.sleep(0.1)
    spinner.next()
