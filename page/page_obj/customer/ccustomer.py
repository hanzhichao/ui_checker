# !/usr/bin/env python
# -*- coding=utf-8 -*-

<<<<<<< HEAD
"""
-------------------------------------------------------
File Name:      mark.py
Author:         Han Zhichao
Date:           2017/11/05
Description:
=======
import os
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259

-------------------------------------------------------
"""
__author__ = 'Han Zhichao'

from time import sleep
from page.page import Page
from util.browser import Chrome


class CCustomer(Page):
<<<<<<< HEAD
    page = 'customer/ccustomer'
    
    def search_phone(self, phone):
        self.find_element('customer_search_phone').send_keys(phone)
        self.find_element('customer_search_btn').click()
        sleep(1)
=======

    def search_phone(self, phone):
        self.element('search_phone').send_keys(phone)
        self.element('search_btn').click()

    def type_username(self, username):
        self.element('username').send_keys(username)
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259


if __name__ == '__main__':

<<<<<<< HEAD
    # d = Chrome.normal()
    d = Chrome.headless()
    p = CCustomer(d)
    p.load()
    p.search_phone('18010181267')
=======
    d = Chrome.normal()  # Chrome.headless()
    p = CCustomer(d)
    p.login()
    p.load()
    p.type_username('hanzhichao')

>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259
    sleep(10)
    d.quit()
