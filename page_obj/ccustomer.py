import sys
sys.path.append('..')
from page import Page
from util.config_parser import PageElm
from util.browser import Chrome
from time import sleep


class CCustomer(Page):
    def search_phone():
        PageElm.get('search_phone').send_keys('18010181267')
        PageElem.get('search_btn').click()


if __name__ == '__main__':
    d = Chrome.normal()
    p=CCustomer(d)
    p.login()
    sleep(1)
    p.load()
    p.search_phone()
