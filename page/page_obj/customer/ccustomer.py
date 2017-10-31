import sys
from time import sleep

import os

sys.path.append('..')

from page.page import Page
from util.browser import Chrome


class CCustomer(Page):

    def search_phone(self):
        self.element('search_phone').send_keys('18010181267')
        self.element('search_btn').click()


if __name__ == '__main__':

    d = Chrome.normal()
    p = CCustomer(d)
    p.login()
    p.load()
    p.search_phone()
    sleep(10)
    d.quit()
    # p.login()
    # sleep(1)
    # p.load()
    # p.search_phone()
