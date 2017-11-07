# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep
from page.base_page import BasePage
from util.browser import Chrome
from util.log import logger


class IndexPage(BasePage):
    page = __file__
    
    def search_phone(self, phone):
        self.find_element('customer_search_phone').send_keys(phone)
        self.find_element('customer_search_btn').click()
        sleep(1)


if __name__ == '__main__':

    # d = Chrome.normal()
    d = Chrome.headless()
    p = IndexPage(d)
    p.match_property()
    # p.load()
    # p.search_phone('18010181267')
    # sleep(10)
    # d.quit()
