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

# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from util.root import project_root
import platform


class Chrome(object):
    def __init__(self):
        pass
    if platform.system() == 'Windows':
        chrome_driver = project_root() + '/driver/chromedriver.exe'
    else:
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
