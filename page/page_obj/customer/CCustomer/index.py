# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep
from page.base_page import BasePage
from page.index.index.login import LoginPage
from util.browser import Chrome
from util.log import logger


class IndexPage(BasePage):
    page = __file__
    menu = ('客服管理系统', '综合管理', '综合信息')
    subject = '会员信息'
    
    
    def search_phone(self, phone):
        self.type('电话搜索：', phone)
        self.clickbtn('搜索')
        page_phone = self.get_value('会员电话：')
        print(page_phone)
        self.sleep()
        
    def assert_phone(self):
        page_phone = self.get_value('会员电话：')
        print(page_phone)
        return page_phone


if __name__ == '__main__':

    # d = Chrome.normal()
    d = Chrome.headless()
    l = LoginPage(d)
    l.login()
    p = IndexPage(d)
    p.load()
    p.search_phone('18010181267')
    sleep(10)
    d.quit()
