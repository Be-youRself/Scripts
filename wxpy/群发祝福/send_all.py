# Filename: send_all.py
# Coding: utf8
# 对于列表所有好友发送指定祝福 以对方备注名开头

from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot()
# 创建列表所有好友的对象列表
friends = bot.friends().search("张欣")

# 读入指定祝福内容
message = ""
file_r = open("message.txt","r",encoding = "utf-8")
while True:
    line = file_r.readline()
    message = message + line
    if len(line) == 0:
        break
file_r.close()

count = 0 # 用于统计人数
# 发送祝福
for i in friends[1:]: # 第一个是自己 所以从下标1开始 不除去自己会导致异常
	try:
		i.send('亲爱的{0}：\n        {1}'.format(i.name, message)) # 四个空格等于一个汉字
	except Exception: # 防止出现异常中断脚本 尤其图片发送会导致异常！
		print(i.name)
		continue
	count = count + 1
	time.sleep(2) # 微信有消息发送速度限制

print("成功发送祝福给了{0}个好友！".format(count))
