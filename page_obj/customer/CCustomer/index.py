# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep

from page_obj.base_page import BasePage
from page_obj.index.index.login import LoginPage
from util.browser import Chrome
from util.db import DB


class IndexPage(BasePage):
    menu = '客服管理系统', '综合管理', '综合信息'
    subject = '会员信息'
    db_map = {'会员姓名': ('username', 'u_user'),
              }
    
    def search_phone(self, phone):
        self.type('电话搜索：', phone)
        self.click('搜索')
        self.sleep()
        print(self.get_input_value('会员姓名'))
        print(self.get_input_value('会员电话'))
        print(self.get_input_value('身份证号码'))
        print(self.get_input_value('生日'))
        print(self.get_radio_value('性别'))
        print(self.get_select_value('民族'))
        print(self.get_select_value('客户来源'))
        print(self.get_textarea_text('备注'))
        db = DB()
        where_condition = 'phone="18010181267"'
        print(db.get(key='username', table='u_user', where_condition=where_condition)[0])


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
