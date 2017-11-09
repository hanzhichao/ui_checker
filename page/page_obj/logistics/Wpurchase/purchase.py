# !/usr/bin/env python
# -*- coding=utf-8 -*-
from time import sleep

from selenium.webdriver.support.select import Select

from page.base_page import BasePage
from util.browser import Chrome


class PurchasePage(BasePage):
    page = __file__
    
    def create_new_purchase(self, station_name):
        self.find_element('create_new_purchase').click()
        sleep(1)
        Select(self.find_element('need_select_time')).select_by_visible_text("下午")
        self.find_element('purchase_num').send_keys("10000")
        self.find_element('save_btn').click()
        sleep(1)
        self.find_element('confirm_btn').click()
        sleep(5)
        

if __name__ == '__main__':
    d = Chrome.normal()
    # d = Chrome.headless()
    p = PurchasePage(d)
    p.load()
    p.create_new_purchase('青年路')
    sleep(5)
    d.quit()
