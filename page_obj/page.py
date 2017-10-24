import os
import sys
sys.path.append('..')
from util.browser import Chrome
import unittest
from selenium import webdriver
from util.config_parser import Config, PageElm
from selenium.webdriver.common.by import By


class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Config.base_url
        filename = os.path.basename(__file__).split('.')[0]
        print filename
        if filename != 'page':
            self._page = PageElm('../../../'+filename)[0]
            self.menu = PageElm(path).menu
            self.subject = PageElm(path).subject
    
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


    def login(self):
        login_url = self.base_url + '/index/index/login'
        self.driver.get(login_url)
        self.driver.find_element_by_id('nickname').clear()
        self.driver.find_element_by_id('nickname').send_keys(Config.password)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(Config.password)
        self.driver.find_element_by_id('login').click()

    def logout(self):
        self.driver.find_element_by_class_name('btn-bg1').click()
    
    def load(self):
        self.find_element(By.PARTIAL_LINK_TEXT,PageElm.menu[0]).click()
        self.find_element(By.LINK_TEXT, PageElm[1]).click()
        self.find_element(By.LINK_TEXT, PageElm[2]).click()
        assert self.on_page(), "Load Page Error."


if __name__ == '__main__':
    d = Chrome.normal()
    p=Page(d)
    p.login()
