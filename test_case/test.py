# !/usr/bin/env python
# -*- coding=utf-8 -*-

"""
-------------------------------------------------------
File Name:      mark.py
Author:         Han Zhichao
Date:           2017/11/05
Description:

-------------------------------------------------------
"""
__author__ = 'Han Zhichao'

 -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('disable-infobars')   # 去掉"chrome正受到自动化测试软件的控制"的提示条
# options.add_argument('--headless')  # 无界面模式
# options.add_argument('--disable-gpu')

#options.binary_location =r'C:\Users\hldh214\AppData\Local\Google\Chrome\Application\chrome.exe'  # Windows 下 chrome安装位置
# options.binary_location = '/opt/google/chrome/chrome' # Linux 下chrome安装位置

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.baidu.com')
print driver.title
driver.quit()