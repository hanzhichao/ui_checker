<<<<<<< HEAD
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

=======
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259
from random import random

import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
<<<<<<< HEAD
from util.decorator import show_duration
from util.browser import Chrome
=======
from decorator import show_duration
from browser import Chrome
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259


@show_duration
def hello():
    time.sleep(random())
<<<<<<< HEAD
    print("hello")
=======
    print "hello"
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259


class Action(WebElement, WebDriver):

    @show_duration
    def type(self, *value):
        self.clear()
        self.send_keys(*value)

    @show_duration
    def open(self, url):
        self.get(url)
<<<<<<< HEAD
        










=======
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259


d = Chrome.headless()
d.get('http://www.baidu.com')
<<<<<<< HEAD
print(d.title)
d.find_element_by_id('kw').type('hanzhichao')
d.find_element_by_id('su').click()
print(d.title)
=======
print d.title
d.find_element_by_id('kw').type('hanzhichao')
d.find_element_by_id('su').click()
print d.title
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259
d.quit()
