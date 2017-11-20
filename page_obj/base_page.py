# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep as _sleep

import os

from util.data_file_parser import ConfFile
from util.log import logger
from util.config import Config
from selenium.webdriver.common.by import By
from util.browser import Chrome
from util.decorator import exec_time
from util.selenium_easy import WebPage
from util.db import DB


class BasePage(WebPage):
    property_file = None
    
    def __init__(self, driver, base_url=Config.option('env', 'base_url')):
        self.driver = driver
        self.base_url = base_url
        if self.property_file:
            self.get_property()

    @staticmethod
    def sleep(time=float(Config.option('runtime', 'sleep'))):
        _sleep(time)
    
    def get_property(self):
        property_file = os.path.basename(self.property_file).replace('.py', '.property')
        _property = ConfFile.load(property_file)
        _property['page']['menu'] = tuple(_property['page']['menu'].split(','))
        self.menu = _property['page']['menu']
        
        self.subject = _property['page']['subject']
        
        for element in _property['element']:
            _property['element'][element] = tuple(_property['element'][element].split(','))
        self.elements = _property['element']
        
        for element_name in _property['db_map']:
            _property['db_map'][element_name] = tuple(_property['db_map'][element_name].split(','))
        self.db_map = _property['db_map']
        
    # -----------------------page_obj methods----------------------------------
    @exec_time
    def open(self, url):
        self.driver.get(url)

    def on_page(self, subject):
        actual_subject = self.find_element(By.XPATH, '//*[@id="iframe"]/div/h1').text
        logger.debug("page_obj subject：%s" % actual_subject + "---config subject：%s" % subject)
        return subject in actual_subject

    def _load(self, menu, subject):
        self.clicks(menu)
        self.sleep()
        assert self.on_page(subject), "Not on page_obj!"
    
    @exec_time
    def load(self):
        self._load(self.menu, self.subject)
        
    @exec_time
    def turn_to(self, page):  # maybe bugs exists when turn_to other page_obj
        self.driver.refresh()
        self._load(page)
    
    def logout(self):
        self.find_element(By.CLASS_NAME, 'btn-bg1').click()
    
    # --------------------db methods------------------------------------------
    @exec_time
    def get_db_value(self, element_name, where_condition):
        db = DB()
        db_map = self.page['db_map'](element_name)
        return db.get(key=db_map[0], table=db_map[1], where_condition=where_condition)[0]

    @exec_time
    def compare_db(self, element_name, where_condition):
        page_element_value = self.get_input_value(element_name)
        element_db_map_value = self.get_db_value(element_name, where_condition)
        return page_element_value == element_db_map_value
    
    @exec_time
    def compare_db_all(self, where_condition):
        for element_name in self.page['db_map']:
            if not self.compare_db(element_name):
                return False
        return True
            
    
if __name__ == '__main__':
    d = Chrome.headless()
    d.get('http://jd.spicespirit.com/index/index/login/')
    p = BasePage(d)
    p.type("请输入用户名", "hanzhichao")
    p.type("请输入密码", "hanzhichao")
    p.click("登录")
