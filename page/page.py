#  -*- coding=utf-8  -*-

import os
import sys
import unittest
from selenium import webdriver
from util.file import ConfFile
from selenium.webdriver.common.by import By
sys.path.append('../..')
from util.browser import Chrome


class Page(object):
    def __init__(self, driver, page_elm): # eg: 'customer/ccustomer.ini'
        self.driver = driver
        self.page_elm_file = '../../page_elm/' + page_elm
        page = ConfFile.load_section(self.page_elm_file, 'page')  # ? If in windows os is OK?
        print page
        self.menu = tuple(page['menu'].splite(','))
        self.subject = page['subject']

        print self.menu, self.subject

    def elm(self, element):
        return tuple(ConfFile.get(self.page_elm_file, 'element', element).split(','))

    # element method
    def find_element(loc):
        return self.driver.find_element(loc)
    def locate(element):
        element_loc = PageElm.get(element)
        return self.driver.find_element(element_loc)

    def type(element,str):
        element = locate(element)
        element.clear()
        element.send_keys(str)


    # page method
    def on_page(self):
        actual_subject = self.driver.find_element_by_xpath('//*[@id="iframe"]/div/h1')
        return self.subject==actual_subject

    def load(self):
        self.find_element(By.PARTIAL_LINK_TEXT,self.menu[0]).click()
        self.find_element(By.LINK_TEXT, self.menu[1]).click()
        self.find_element(By.LINK_TEXT, self.menu[2]).click()
        assert self.on_page(), "Load Page Error."


if __name__ == '__main__':
    # d = Chrome.headless()
    d = webdriver.Chrome('../driver/chromedriver')
    p = Page(d)
    d.quit()
    # p.login()
    # p.load()
    # print os.path.dirname(__file__).split(os.sep)[-1]
    # print os.path.basename(__file__).split('.')[0] + '.ini'
    # print os.path.abspath(__file__).replace('.py', '.ini')
