# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from base.data_file_parser import ConfFile

class Chrome():
    def __init__(self):
        pass

    @classmethod
    def normal(cls):
        options = Options()
        options.add_argument('disable-infobars') # 去掉"chrome正受到自动化测试软件的控制"的提示条
        return webdriver.Chrome(chrome_options=options)

    @classmethod
    def headless(cls):
        options = Options()
        options.add_argument('disable-infobars')   
        options.add_argument('--headless')  # 无界面模式
        options.add_argument('--disable-gpu')

        # options.binary_location =r'C:\Users\hldh214\AppData\Local\Google\Chrome\Application\chrome.exe'  # Windows 下 chrome安装位置
        # options.binary_location = '/opt/google/chrome/chrome' # Linux 下chrome安装位置
        return webdriver.Chrome(chrome_options=options)
