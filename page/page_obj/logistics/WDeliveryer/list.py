# !/usr/bin/env python
# -*- coding=utf-8 -*-
from time import sleep

from selenium.webdriver.support.select import Select

from page.base_page import BasePage
from util.browser import Chrome


class ListPage(BasePage):
    page = __file__
    
    def search_name(self, name):
        self.find_element('name').send_keys(name)
        self.find_element('search_btn').click()
        self.find_element('modify_link').click()
        Select(self.find_element('select_station')).select_by_visible_text("青年路")
        self.find_element('update_btn').click()


if __name__ == '__main__':
    d = Chrome.normal()
    # d = Chrome.headless()
    p = ListPage(d)
    p.load()
    p.search_name('韩志超')
    sleep(5)
    d.quit()
