# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep as _sleep
from util.log import logger
from util.config import Config
from selenium.webdriver.common.by import By
from util.browser import Chrome
from util.decorator import exec_time
from util.selenium_easy import WebPage


class BasePage(WebPage):
    menu = ()
    subject = ''
    
    def __init__(self, driver, base_url=Config.option('env', 'base_url')):
        self.driver = driver
        self.base_url = base_url

    @staticmethod
    def sleep(time=float(Config.option('runtime', 'sleep'))):
        _sleep(time)
    # -----------------------page_obj methods----------------------------------
    
    @exec_time
    def open(self, url):
        self.driver.get(url)

    def on_page(self, subject):
        actual_subject = self.find_element(By.XPATH, '//*[@id="iframe"]/div/h1').text
        logger.debug("page_obj subject：%s" % actual_subject + "---config subject：%s" % subject)
        return subject in actual_subject

    def _load(self, menu, subject):
        self.click(menu)
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
    
    
if __name__ == '__main__':
    d = Chrome.headless()
    d.get('http://jd.spicespirit.com/index/index/login/')
    p = BasePage(d)
    p.type("请输入用户名", "hanzhichao")
    p.type("请输入密码", "hanzhichao")
    p.click("登录")
