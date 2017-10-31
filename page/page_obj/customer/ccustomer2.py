import sys
from time import sleep

import os
from selenium import webdriver

sys.path.append('..')

from page.page import Page
from util.browser import Chrome


class CCustomer(Page):

    filename = os.path.basename(__file__)

    def search_phone(self):
        pass
        # elm(self.filename, 'search_phone').send_keys('18010181267')
        # elm(self.filename, 'search_btn').click()


if __name__ == '__main__':
    # d = Chrome.headless()
    # print os.path.dirname(__file__)
    d = webdriver.Chrome('../../../driver/chromedriver')
    p=CCustomer(d)
    d.quit()
    # p.login()
    # sleep(1)
    # p.load()
    # p.search_phone()
