import sys
from time import sleep

import os

sys.path.append('..')

from page.page import Page
from util.browser import Chrome


class CCustomer(Page):

    def search_phone(self, phone):
        self.element('search_phone').send_keys(phone)
        self.element('search_btn').click()

    def type_username(self, username):
        self.element('username').send_keys(username)


if __name__ == '__main__':

    d = Chrome.normal()  # Chrome.headless()
    p = CCustomer(d)
    p.login()
    p.load()
    p.type_username('hanzhichao')

    sleep(10)
    d.quit()
    # p.login()
    # sleep(1)
    # p.load()
    # p.search_phone()
