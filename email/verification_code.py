# Filename: verification_code.py
# 一个简单的验证码校验系统来应用 qemail.py

import qemail
import random
import sys

username_recv = input("请输入获取验证码的邮箱：")
print("正在发送验证码...")
title = "您的验证信息"
veri_code = ""
for i in range(0, 6):
    veri_code = str(random.randint(0,9)) + veri_code
content = "您正在进行验证，如果不是本人操作，请勿理睬！\n\n\
您的验证码是： %s (请不要告诉任何人)"%veri_code
mail = qemail.SendMail(username_recv = username_recv, 
    mailtitle = title, mailcontent = content)
mail.send_mail()
print("验证码已发送至 %s"%username_recv)
if veri_code == input("请输入验证码："):
    print("验证成功！")
else:
    print("验证失败！")
while(input("输入q退出：") != "q"):
    pass
sys.exit()