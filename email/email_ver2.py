# Filename: email_ver2.py
# 发送带附件邮件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

mailserver = "smtp.exmail.qq.com"
username_send = "robot@jsyzqxy.cn"
print("You are trying to use the account %s to send an email."%username_send)
password = input("Enter the password: ") # 第三方登录使用授权码
username_recv = ["qxy@jsyzqxy.cn"]

mailcontent = "这是个测试邮件，不用回复！"
mail = MIMEMultipart()
mail.attach(MIMEText(mailcontent))
mail["Subject"] = "一封测试邮件"
mail["From"] = username_send
mail["To"] = ",".join(username_recv)

filename = input("Enter the filename you want to send: ")
try:
    att = MIMEText(open(filename, 'rb').read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    # 处理中文文件名
    filename = '=?utf-8?b?' + base64.b64encode(filename.encode()).decode() + '?='
    att["Content-Disposition"] = "attachment; filename = %s"%filename
    mail.attach(att)
except FileNotFoundError as e:
    print("未找到该文件！附件添加失败！")
    print(e)
except Exception as e:
    print(e)
try:
    smtp = smtplib.SMTP_SSL(mailserver, port = 465)
    smtp.login(username_send, password)
    smtp.sendmail(username_send, username_recv, mail.as_string())
    smtp.quit()
except Exception as e:
    print("Fail to send this email!\n")
    print("The reason:\n")
    print(e)
else:
    print("Success to send this email!")