# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep

from page_obj.base_page import BasePage
from page_obj.index.index.login import LoginPage
from util.browser import Chrome
from util.db import DB
from util.selenium_easy import Element, Input


class IndexPage(BasePage):
    menu = ('客服管理系统', '综合管理', '综合信息')
    subject = '会员信息'
 
    def search_phone(self, phone):
        self.type('电话搜索：', phone)
        self.click_btn('搜索')
        self.sleep()
        
    def save_work_bill(self):
        self.click("显示更多内容")
        
        self.select("来电原由", "订单")
        self.select("来电原由", "创建订单", 2)
        self.type_area("备注", "自动化测试", 2)
        self.click_btn("保存", 2)
        
    def create_order(self, phone, station, code):
        self.search_phone(phone)
        self.save_work_bill()
        self.click("显示更多内容", 4)
        self.select("配送站点", station)
        self.type("请输入要查询商品的简码", code)
        sleep(1)
        self.click_text("麻酱烧饼")
        self.select("订单渠道：", "电话")
        self.select("订单区域", "北京")
        self.click_input("是否预定送餐时间", 4)
        self.click_btn("当前")
        self.click_btn("确认")
        self.check("支付方式", 1)
        self.select("支付方式", "支付宝")
        self.type_area("备注", "自动化测试下单", 3)
        self.click_btn("保存", 3)
        
        
if __name__ == '__main__':
    d = Chrome.normal()
    # d = Chrome.headless()
    d.maximize_window()
    l = LoginPage(d)
    l.login()
    p = IndexPage(d)
    p.load()
    p.create_order('18010181267', '花家地', 'M')
    sleep(10)
    d.quit()
