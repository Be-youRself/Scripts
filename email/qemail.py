# Filename: SendMail.py
# 封装发送邮件的类
# 添加密码参数 若调用函数前未设置密码则需要进行登录操作
# 将变量输入类型都统一字符型输入(适当list型也允许) 函数中进行处理
# 返回邮件发送结果(-3:输入参数出错 -2:添加附件出错 -1:发送邮件失败(网络、邮箱&密码不匹配等原因) 0:发送成功)(-3、-2、-1均不会发送出去邮件)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

class SendMail(object):
    '''This is a class to send an email to someone.

Parameter list:
    (username_recv, mailtitle, mailcontent, file = [], username_send = "robot@jsyzqxy.cn", 
    password_send = "", mailserver = "stmp.exmail.qq.com", port = 465)
Type of all the paremeters port is string.
You can use list as the type of username_recv and file when you have more than one.
The default username_send is the author's account.
You can change it to your account and at the same time, you need remember to change mailserver and port.
You will get four different status codes after calling this function:
    0:Success to send the email.
    -1:Fail to send the email(bad Internet、wrong password and so on).
    -2:Fail to add the files.
    -3:Errors of the parameter inputed
    (-1、-2、-3 will not send an email out)'''

    def __init__(self, username_recv, mailtitle, mailcontent, file = [], 
                username_send = "robot@jsyzqxy.cn", password_send = "",
                 mailserver = "smtp.exmail.qq.com", port = 465):
        # 对于数据类型进行字符型统一
        # 判断单个还是多个收件人
        if not isinstance(username_recv, list):
            self.username_recv = [str(username_recv)]
        else:
            for i in range(len(username_recv)):
                username_recv[i] = str(username_recv[i])
            self.username_recv = username_recv
        self.mailtitle = str(mailtitle)
        self.mailcontent = str(mailcontent)
        # 判断单个还是多个附件
        if not isinstance(file, list):
            self.file = [str(file)]
        else:
            for i in range(len(file)):
                file[i] = str(file[i])
            self.file = file
        self.username_send = str(username_send)
        self.password_send = str(password_send)
        self.mailserver = str(mailserver)
        self.port = str(port)

    def send_mail(self):
        # 如果没有提前输入密码 执行登录
        if self.password_send == "":
            print("You are trying to use account %s to send an email."%self.username_send)
            self.password_send = input("Please enter the password:")
        # 对于port是否合法进行验证以及处理
        # 可在此处使用 regex 进行名称格式验证
        try:
            self.port = int(self.port)
        except Exception:
            return -3
        # 建立邮件对象
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
            except Exception:
                return -2
        # 发送邮件
        try:
            self.smtp = smtplib.SMTP_SSL(self.mailserver, port = self.port)
            self.smtp.login(self.username_send, self.password_send) #登录密码末尾空格会被忽视
            self.smtp.sendmail(self.username_send, self.username_recv, mail.as_string())
            self.smtp.quit()
        except Exception as e:
            return -1
        else:
            return 0

if __name__ == "__main__":
    email = SendMail(["qxy@jsyzqxy.cn"], "一封邮件示例", "这是一封来自SendMail主类的邮件示例，不用回复！")
    email.send_mail()