# Filename: SendMail.py
# 封装发送邮件的类
# 未对输入实参进行变量类型的分析 输入类型有误即会出现异常

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

class SendMail(object):
    '''This is a class to send an email to someone.

Parameter list:(username_recv, mailtitle, mailcontent, file = [], username_send = "robot@jsyzqxy.cn", mailserver = "stmp.exmail.qq.com", port = 465)
Type of all the paremeters except port is string.(port is int)
You can use list as the type of username_recv and file when you have more than one.
The default username_send is the author's account.
You can change it to your account and at the same time, you need remember to change mailserver and port.'''

    def __init__(self, username_recv, mailtitle, mailcontent, 
                file = [], username_send = "robot@jsyzqxy.cn",
                 mailserver = "smtp.exmail.qq.com", port = 465):
        # 判断单个还是多个收件人
        if not isinstance(username_recv, list):
            self.username_recv = [username_recv]
        else:
            self.username_recv = username_recv
        self.mailtitle = mailtitle
        self.mailcontent = mailcontent
        # 判断单个还是多个附件
        if not isinstance(file, list):
            self.file = [file]
        else:
            self.file = file
        self.username_send = username_send
        self.mailserver = mailserver
        self.port = port

    def send_mail(self):
        # 登陆
        print("You are trying to use account %s to send an email."%self.username_send)
        self.password = input("Please enter the password:")
        mail = MIMEMultipart()
        mail.attach(MIMEText(self.mailcontent, "plain"))
        mail["Subject"] = self.mailtitle
        mail["From"] = self.username_send
        mail["To"] = ",".join(self.username_recv)
        # 处理附件
        for i in range(0, len(self.file)):
            try:
                att = MIMEText(open(self.file[i], "rb").read(), "base64", "utf-8")
                att["Content-Type"] = "application/octet-stream"
                # 处理中文文件名
                self.file[i] ='=?utf-8?b?' + base64.b64encode(self.file[i].encode()).decode() + '?='
                att["Content-Disposition"] = "attachment; filename = %s"%self.file[i]
                mail.attach(att)
            except Exception as e:
                print("Fail to attach the attachment:", self.file[i])
                print("The details:")
                print(e)
        # 发送邮件
        try:
            self.smtp = smtplib.SMTP_SSL(self.mailserver, port = self.port)
            self.smtp.login(self.username_send, self.password)
            self.smtp.sendmail(self.username_send, self.username_recv, mail.as_string())
            self.smtp.quit()
        except Exception as e:
            print("Fail to send this email!")
            print("The details:")
            print(e)
        else:
            print("Success to send this email!")

if __name__ == "__main__":
    email = SendMail(["qxy@jsyzqxy.cn"], "一封邮件示例", "这是一封来自SendMail主类的邮件示例，不用回复！")
    email.send_mail()