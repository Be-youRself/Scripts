# Filename: email_ver1.py
# 尝试用机器账号向指定邮箱发送邮件
# 仅发送文本信息

import smtplib
from email.mime.text import MIMEText

##准备阶段
mailserver = "smtp.exmail.qq.com" # 服务器地址
# 发送方
username_send = "robot@jsyzqxy.cn"
password = "euxNgCrNvswVPSTz" # 第三方登录使用授权码
# 接收方
username_recv = ["qxy@jsyzqxy.cn"]
# 邮件
mailcontents = "This is just a test email."
mail = MIMEText(mailcontents, "plain") # 内容、格式(可以省去)
# 固定写法 必须要有
mail["Subject"] = "A test"
mail["From"] = username_send
mail["To"] = ",".join(username_recv)

##开始发送
try:
    smtp = smtplib.SMTP_SSL(mailserver, port = 465) # 连接邮箱服务器
    smtp.login(username_send, password) # 登录邮箱
    smtp.sendmail(username_send, username_recv, mail.as_string()) #发送邮件
    smtp.quit() # 断开连接 退出服务    
except Exception as e:
    print("Fail to send this email!")
    print("The reason:\n")
    print(e)
else:
    print("Success to send this email!")




















