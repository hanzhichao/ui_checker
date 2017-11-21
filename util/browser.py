# !/usr/bin/env python
# -*- coding=utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import platform
from pyvirtualdisplay import Display
import sys
sys.path.append('..')
from util.root import project_root


class Chrome(object):
    def __init__(self):
        pass
    if platform.system() == 'Windows':
        chrome_driver = project_root() + '/driver/chromedriver.exe'
    else:
        chrome_driver = project_root() + '/driver/chromedriver'
        os.chmod(chrome_driver, 777)

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

    @classmethod
    def remote(cls):
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        return driver


if __name__ == '__main__':
    #display = Display(visible=0, size=(800,600))
    #display.start()
    # d = webdriver.Firefox()
    d = Chrome.remote()
    d.get('http://www.baidu.com')
    print(d.title)
    print(d.page_source)
    d.quit()
    #display.stop()
