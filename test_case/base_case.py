# !/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from util.browser import Chrome


class BaseCase(unittest.TestCase):
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
        # self.driver = Chrome.normal()
        self.driver = Chrome.headless()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # login()
        
    def tearDown(self):
        self.driver.quit()
        # logout()