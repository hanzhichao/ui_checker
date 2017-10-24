import sys
sys.path.append('..')
from page import Page
from util.config import elm
from util.browser import Chrome
from time import sleep


class CCustomer(Page):
    def search_phone(self):
        elm(self.filename, 'search_phone').send_keys('18010181267')
        elm(self.filename, 'search_btn').click()


if __name__ == '__main__':
    d = Chrome.headless()
    p=CCustomer(d)
    p.login()
    sleep(1)
    p.load()
    p.search_phone()
