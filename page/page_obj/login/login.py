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

from util.browser import Chrome
from selenium import webdriver
import sys
sys.path.append('../..')
from util.config import Config
from page.page import Page


class Login(Page):

    def login(self):

        login_url = self.base_url + '/index/index/login'
        self.driver.get(login_url)
        self.driver.find_element_by_id('nickname').clear()
        self.driver.find_element_by_id('nickname').send_keys(self.username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_id('login').click()

