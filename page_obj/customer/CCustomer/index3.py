# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select
from page_obj.index.index.login import LoginPage
from page_obj.base_page import BasePage
from util.browser import Chrome


# 页面对象（PO）登录页面
class IndexPage(BasePage):
    property_file = __file__
    
    def search_customer(self, phone):
        self.find_element(*self.elements['customer_search_phone']).send_keys(phone)
        self.find_element(*self.elements['customer_search_btn']).click()
        sleep(1)

    def save_work_bill(self):
        self.find_element(*self.elements['call_show_more']).click()
        Select(self.find_element(*self.elements['call_reason1'])).select_by_visible_text('订单')
        Select(self.find_element(*self.elements['call_reason2'])).select_by_visible_text('创建订单')
        self.find_element(*self.elements['call_remark']).send_keys("自动化测试")
        self.find_element(*self.elements['call_save_btn']).click()
        sleep(1)
        
    def create_order(self):
        self.search_customer('18010181267')
        self.save_work_bill()
        
        self.find_element(*self.elements['create_order_show_more']).click()
        Select(self.find_element(*self.elements['create_order_station'])).select_by_visible_text("花家地")
        self.find_element(*self.elements['create_order_search']).send_keys("M")
        sleep(1)
        self.find_element(*self.elements['create_order_search_option']).click()
        Select(self.find_element(*self.elements['create_order_channel'])).select_by_visible_text("其他")
        Select(self.find_element(*self.elements['create_order_area'])).select_by_visible_text("北京")
        self.find_element(*self.elements['create_order_start']).click()
        self.find_element(*self.elements['create_order_start_time_now']).click()
        self.find_element(*self.elements['create_order_start_time_sure']).click()
        self.find_element(*self.elements['create_order_pay_online']).click()
        Select(self.find_element(*self.elements['create_order_pay_way'])).select_by_visible_text("支付宝")
        self.find_element(*self.elements['create_order_remark']).send_keys("自动化测试下单")
        self.find_element(*self.elements['create_order_save_btn']).click()


if __name__ == '__main__':
    d = Chrome.normal()
    # d = Chrome.headless()
    d.maximize_window()
    l = LoginPage(d)
    l.login()
    p = IndexPage(d)
    p.load()
    p.create_order()
    sleep(10)
    d.quit()