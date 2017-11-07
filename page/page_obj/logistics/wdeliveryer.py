# !/usr/bin/env python
# -*- coding=utf-8 -*-
"""
-------------------------------------------------------
File Name:      wdeliveryer.py   
Author:         Han Zhichao
Date:           2017/11/5
Description:

-------------------------------------------------------
"""
__author__ = 'Han Zhichao'

from time import sleep
from page.base_page import BasePage
from util.browser import Chrome


class WDeliveryer(BasePage):
    page = 'logistics/wdeliveryer'
    
    def search_name(self, name):
        self.find_element('name').send_keys(name)
        self.find_element('search_btn').click()
        sleep(1)
        self.find_element('modify_link').click()
        sleep(1)
        self.find_element('select_station').click()
        sleep(1)
        self.find_element('station').click()
        sleep(3)
        self.find_element('update_btn').click()


if __name__ == '__main__':
    d = Chrome.normal()
    # d = Chrome.headless()
    p = WDeliveryer(d)
    p.load()
    p.search_name('韩志超')
    sleep(5)
    d.quit()
