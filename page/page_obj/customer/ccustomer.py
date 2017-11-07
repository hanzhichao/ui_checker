# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep
from page.page import Page
from util.browser import Chrome


class CCustomer(Page):
    page = 'customer/ccustomer'
    
    def search_phone(self, phone):
        self.find_element('customer_search_phone').send_keys(phone)
        self.find_element('customer_search_btn').click()
        sleep(1)


if __name__ == '__main__':

    # d = Chrome.normal()
    d = Chrome.headless()
    p = CCustomer(d)
    p.load()
    p.search_phone('18010181267')
    sleep(10)
    d.quit()
