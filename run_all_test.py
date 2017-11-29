# -*- coding: utf-8 -*-
import unittest
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
import platform
from threading import Thread
if (platform.python_version()) < '3':
    from util.HTMLTestRunner import HTMLTestRunner
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    from util.HTMLTestRunnerCN import HTMLTestRunner

from util.root import project_root
import sys
sys.path.append('..')

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

# 截图函数
def take_snapshot(driver, file_name):
    file_path = project_root() + '/report/snapshot/' + file_name
    driver.get_screenshot_as_file(file_path)

# 指定测试用例为当前文件夹下的test_case目录
# test_dir =  os.path.join(project_root(),'test_case')
test_dir = "./test_case"
test_report = './report'
module_list = []
ignore_list = ['__pycache__']
for path in os.listdir(test_dir):
    if path not in ignore_list:
        path = os.path.join(test_dir, path)
        if os.path.isdir(path):
            module_list.append(path)

test_suite_list = []
for module in module_list:
    unittest.defaultTestLoader._top_level_dir = None
    try:
        discover = unittest.defaultTestLoader.discover(module, pattern='test*.py')
        test_suite_list.append(discover)
    except ImportError:
        print("module '%s' cann't be imported" % module)
        continue

# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '/' + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new


def run(module, test_suite):
    now = time.strftime("%Y-%m-%d_%H%M%S")
    module = module.split("\\")[1]
    filename = test_report + '/' + module + '_' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description="运行环境：windows 10, Chrome")
    # runner = unittest.TextTestRunner()
    runner.run(test_suite)
    fp.close()

if __name__ == "__main__":                                                                        
    
    threads = []
    suite_num = len(test_suite_list)
    for i in range(suite_num):
        t = Thread(target=run, args=(module_list[i], test_suite_list[i],))
        threads.append(t)
    for i in range(suite_num):
        threads[i].start()
    for i in range(suite_num):
        threads[i].join()
                                                                                         
    # new_report = new_report(test_report)
    # send_mail(new_report)


