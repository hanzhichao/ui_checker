# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep as _sleep

from util.log import logger
from util.config import Config, Property
from selenium.webdriver.common.by import By
from util.browser import Chrome
from util.decorator import exec_time
from util.db import DB


class BasePage(object):
    page = __file__
    menu = ()
    subject = ''
    
    def __init__(self, driver, base_url=Config.option('env', 'base_url')):
        self.driver = driver
        self.base_url = base_url
        
        # if __name__ != '__main__':
        #     self.property = Property(self.page).property

    @staticmethod
    def sleep(time=float(Config.option('runtime', 'sleep'))):
        _sleep(time)
    # -----------------------page methods----------------------------------
    
    @exec_time
    def open(self, url):
        self.driver.get(url)

    def on_page(self, subject):
        actual_subject = self.find_element(By.XPATH, '//*[@id="iframe"]/div/h1').text
        logger.debug("page subject：%s" % actual_subject + "---config subject：%s" % subject)
        return subject in actual_subject

    def _load(self, menu, subject):
        self.find_element(By.PARTIAL_LINK_TEXT, menu[0]).click()
        self.find_element(By.LINK_TEXT, menu[1]).click()
        self.find_element(By.LINK_TEXT, menu[2]).click()
        self.sleep()
        assert self.on_page(subject), "Not on page!"
    
    @exec_time
    def load(self):
        self._load(self.menu, self.subject)
        
    @exec_time
    def turn_to(self, page):  # maybe bugs exists when turn_to other page
        self.driver.refresh()
        self._load(page)
    
    def logout(self):
        self.find_element(By.CLASS_NAME, 'btn-bg1').click()
    # -----------------------element methods-------------------------------
    
    
    # -----------------------db methods-------------------------------------
    @exec_time
    def get_db_value(self, element_name, where_condition):
        db = DB()
        db_map = self.property['db_map'][element_name]
        value = db.get(key=db_map[0], table=db_map[1], where_condition=where_condition)[0]
        return str(value)
    
    def compare_db(self, element_name, where_condition):
        element_page_value = self.get_value(element_name)
        if not element_page_value:
            element_page_value = self.get_text(element_name)
        element_db_value = self.get_db_value(element_name, where_condition)
        logger.debug("%s---%s---%s", element_name, element_page_value, element_db_value)
        return element_page_value == element_db_value
    
    def compare_db_all(self, where_condition):
        result = 1
        for element_name in self.property['db_map']:
            result = result and self.compare_db(element_name, where_condition)
        return result
        
        
if __name__ == '__main__':
    d = Chrome.headless()
    # d.get('https://www.baidu.com')
    p = BasePage(d)
    # p.login()
    # print(d.title)
    d.quit()
