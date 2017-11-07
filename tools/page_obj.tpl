# !/usr/bin/env python
# -*- coding=utf-8 -*-
"""
-------------------------------------------------------
File Name:      %s.py
Author:         Han Zhichao
Date:           2017/11/5
Description:

-------------------------------------------------------
"""
__author__ = 'Han Zhichao'

from time import sleep
from page.page import BasePage
from util.browser import Chrome


class %s(BasePage):
    page = '%s'

    def do_something(self):
        pass



if __name__ == '__main__':
    d = Chrome.normal()
    # d = Chrome.headless()
    p = %s(d)
    p.load()
    p.do_somthing()
    sleep(5)
    d.quit()