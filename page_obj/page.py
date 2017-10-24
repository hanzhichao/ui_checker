import os
import sys
sys.path.append('..')
from util.browser import Chrome
import unittest
from selenium import webdriver
from util.config import conf, page, elm
from selenium.webdriver.common.by import By


class Page(object):
    def __init__(self, driver, filename=os.path.basename(__file__).split('.')[0]):
        self.driver = driver
        self.base_url = conf('env','base_url')
        self.filename = os.path.basename(__file__).split('.')[0]

        # if self.filename != 'page':
        _page = page(self.filename)
        print _page
        self.menu = _page['menu']
        self.subject = _page['subject']
    
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
        self.driver.find_element_by_id('nickname').send_keys(conf('login','username'))
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(conf('login','password'))
        self.driver.find_element_by_id('login').click()

    def logout(self):
        self.driver.find_element_by_class_name('btn-bg1').click()
    
    def load(self):
        self.find_element(By.PARTIAL_LINK_TEXT,self.menu[0]).click()
        self.find_element(By.LINK_TEXT, self.menu[1]).click()
        self.find_element(By.LINK_TEXT, self.menu[2]).click()
        assert self.on_page(), "Load Page Error."


if __name__ == '__main__':
    d = Chrome.headless()
    p=Page(d)
    p.login()
    p.load()
