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

import unittest
=======
import unittest
import sys
sys.path.append('..')
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259
from util.browser import Chrome


class Base(unittest.TestCase):
<<<<<<< HEAD
    type = 'normal'  # normal, smoke, snacirors
    level = 1  # 1-5
    times = 1
    concurrency = 1
    timeout = 0
    skip = False
    
    def prepare(self):
        pass
    
    def clean(self):
        pass
    
    def setUp(self):
        self.driver = Chrome.normal()
        # self.driver = Chrome.headless()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # login()
        
    def tearDown(self):
        self.driver.quit()
        # logout()
=======
    def setUp(self):
        self.driver = Chrome.normal()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259
