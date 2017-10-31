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

from random import random

import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from util.decorator import show_duration
from util.browser import Chrome


@show_duration
def hello():
    time.sleep(random())
    print("hello")


class Action(WebElement, WebDriver):

    @show_duration
    def type(self, *value):
        self.clear()
        self.send_keys(*value)

    @show_duration
    def open(self, url):
        self.get(url)
        












d = Chrome.headless()
d.get('http://www.baidu.com')
print(d.title)
d.find_element_by_id('kw').type('hanzhichao')
d.find_element_by_id('su').click()
print(d.title)
d.quit()
