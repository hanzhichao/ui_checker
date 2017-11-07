# !/usr/bin/env python
# -*- coding=utf-8 -*-

from email.mime.text import MIMEText
from email.header import Header
import smtplib
from util.config import Config


# 发送测试报告，需要配置你的邮箱账号
def send_email():
    # f = open(file_new, 'rb')
    # mail_body = f.read()
    # f.close()

    # 读取配置文件
    conf = Config()
    subject = conf.option('email', 'subject')
    sender = conf.option('email', 'sender')
    receiver = conf.option('email', 'receiver')
    smtp_server = conf.option('email', 'smtp_server')
    smtp_user = conf.option('email', 'smtp_user')
    smtp_password = conf.option('email', 'smtp_password')

    # 组装邮件内容
    mail_body = '测试发送邮件功能'
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    # 连接服务器发送邮件
    smtp = smtplib.SMTP()
    # print smtp_server,smtp_user,smtp_password
    smtp.connect(smtp_server)
    smtp.login(smtp_user, smtp_password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('email has send out!')
    # todo logging.info()


if __name__ == '__main__':
    send_email()
