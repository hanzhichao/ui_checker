# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from file import ConfFile
from util import project_root


class Chrome(object):
    def __init__(self):
        pass

    chrome_driver = project_root() + '/driver/chromedriver'

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
