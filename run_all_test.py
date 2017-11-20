# -*- coding: utf-8 -*-
import unittest
import time
from util.HTMLTestRunnerCN import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os


# 发送测试报告，需要配置你的邮箱账号
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = 'test_results@sina.com'
    msg['To'] = 'hanzhichao@spicespirit.com'
    smtp = smtplib.SMTP()
    smtp.connect("smtp.sina.com")
    smtp.login("test_results@sina.com", "hanzhichao123")
    smtp.sendmail("test_results@sina.com", "hanzhichao@spicespirit.com", msg.as_string())
    smtp.quit()
    print('email has send out!')
    
    
# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new


# 指定测试用例为当前文件夹下的test_case目录
test_dir = './test_case'
test_report = './report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


if __name__ == "__main__":                                                                        
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '/' + now + '_result.html'
    fp = open(filename, 'wb')
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=fp, title='测试报告', description="运行环境：windows 10, Chrome")
    runner.run(discover)
    fp.close()                                                                                       
    new_report = new_report(test_report)
    send_mail(new_report)


