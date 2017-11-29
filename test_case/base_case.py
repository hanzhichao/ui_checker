# !/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
import sys
sys.path.append('..')
from page_obj.base_page import BasePage
from page_obj.index.index.login import LoginPage
from util.browser import Chrome
from util.log import logger
from selenium import webdriver


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
    
    @classmethod
    def setUpClass(cls):
        logger.debug("setUp...")
        # self.driver = Chrome.normal()
        cls.driver = Chrome.headless()
        # cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        page = LoginPage(cls.driver)
        page.login()
    
    @classmethod
    def tearDownClass(cls):
        logger.debug("tearDown...")
        page = BasePage(cls.driver)
        page.logout()
        cls.driver.quit()

if __name__ == '__main__':  
    unittest.main(verbosity=3)