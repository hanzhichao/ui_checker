# !/usr/bin/env python
# -*- coding=utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import platform
import sys
sys.path.append('..')
from util.root import project_root
from threading import Thread
import time
from util.decorator import threads
import subprocess

class Chrome(object):
    def __init__(self):
        pass
    if platform.system() == 'Windows':
        chrome_driver = project_root() + '/driver/Chrome/chromedriver.exe'
    else:
        chrome_driver = project_root() + '/driver/Chrome/chromedriver'
        #os.chmod(chrome_driver, 777)

    @classmethod
    def normal(cls):
        options = Options()
        options.add_argument('disable-infobars')  # 去掉"chrome正受到自动化测试软件的控制"的提示条
        return webdriver.Chrome(cls.chrome_driver, chrome_options=options)

    @classmethod
    def headless(cls):
        options = Options()
        options.add_argument('disable-infobars')   
        options.add_argument('--headless')  # 无界面模式
        options.add_argument('--disable-gpu')
        return webdriver.Chrome(cls.chrome_driver, chrome_options=options)

class Grid(object):
    p_list = []
    selenium_server = project_root() + '/driver/selenium-server-standalone-2.42.2.jar'
    @classmethod
    def start_hub(cls):
        cmd = "java -jar " + cls.selenium_server + " -role hub -port 4446"
        p = subprocess.Popen(cmd, shell=True)
        # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        cls.p_list.append(p)

    @classmethod
    def start_node(cls, hub):
        cmd = "java -jar " + cls.selenium_server + " -role node -hub " + hub + "/hub/register" 
        p = subprocess.Popen(cmd, shell=True)
        # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    

    @classmethod
    def __del__(cls):
        for i in cls.p_list:
            i.terminate()

class Remote(object):
    p_list = []
    selenium_server = project_root() + '/driver/selenium-server-standalone-2.42.2.jar'
    @classmethod
    def chrome(cls):
        cmd = "java -jar " + cls.selenium_server
        p = subprocess.Popen(cmd, shell=True)
        # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        cls.p_list.append(p)
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4446/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        return driver

    def __del__(cls):
        for i in cls.p_list:
            i.terminate()


class Firefox(object):

    @classmethod
    def normal(cls):
        return webdriver.Firefox()

@threads(3)
def test_baidu():
    d = Chrome.headless()
    d.get('http://www.baidu.com')
    print(d.title)
    # print(d.page_source)
    d.quit()

# threads = []
# for i in range(5):
#     t = Thread(target=test_baidu)
#     threads.append(t)


if __name__ == '__main__':
    # d = webdriver.Firefox()
    # d = webdriver.PhantomJS(executable_path=r'D:\Projects\selenium_easy\driver\PantomJs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    # d = Chrome.remote()
    # d = Chrome.headless()
    # d = Firefox.normal()
    # d.get('http://www.baidu.com')
    # print(d.title)
    # print(d.page_source)
    # d.quit()
    # print("start:%s" % time.ctime())
    # for i in range(5):
    #     threads[i].start()
    # for i in range(5):
    #     threads[i].join()
    # print("end:%s" % time.ctime())
    # test_baidu()
    # p=subprocess.Popen("dir", shell=True)  
    # p.wait()
    Grid.start_hub()
    del Grid
    # Remote.start_node('http://192.168.100.36:4446')