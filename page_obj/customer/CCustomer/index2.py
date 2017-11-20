# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from time import sleep
from page_obj.index.index.login import LoginPage
from selenium.webdriver.support.select import Select
from util.browser import Chrome
from page_obj.base_page import BasePage


# 页面对象（PO）登录页面
class IndexPage(BasePage):
    menu = ('客服管理系统', '综合管理', '综合信息')
    subject = '会员信息'
    
    customer_search_phone_text_loc = (By.ID, 'order_user_phone')  # 电话搜索
    customer_search_btn_loc = (By.ID, 'order_search_user')  # 搜索按钮
    
    customer_username_text_loc = (By.ID, 'username')
    customer_phone_text_loc = (By.ID, 'phone')
    customer_id_card_text_loc = (By.ID, 'id_card')
    customer_birthday_date_picker_loc = (By.ID, 'birthday')
    customer_sex_radio_male_loc = (By.XPATH, '//input[@type="radio" and @name="sex" and @value="1"]')
    customer_sex_radio_female_loc = (By.XPATH, '//input[@type="radio" and @name="sex" and @value="2"]')
    customer_sex_radio_checked_loc = (By.XPATH, '//input[@type="radio" and @name="sex" and @checked="checked"]')
    customer_nation_select_loc = (By.ID, 'nation')
    customer_source_select_loc = (By.ID, 'source')
    customer_remark_textarea_loc = (By.ID, 'remark')
    customer_save_btn_loc = (By.ID, 'member_save')
    
    # order_info_*_loc
    
    call_show_more_link_loc = (By.XPATH, '//*[text()="接线人员："]/following::a[text()="显示更多内容"]')
    call_reason_select1_loc = (By.ID, 'desk_type')
    call_reason_select2_loc = (By.ID, 'desk_reason')
    call_remark_textarea_loc = (By.ID, 'order_desc_remark')
    call_save_btn_loc = (By.ID, 'desk_save')

    create_order_show_more_link_loc = (By.XPATH, '//*[text()="新建订单"]/following::a[text()="显示更多内容"][2]')
    create_order_search_text_loc = (By.ID, 'order_code_match')
    create_order_station_select_loc = (By.ID, 'customer_stations')
    create_order_search_option_loc = (By.XPATH, '//li[@class="order_radio"]')
    create_order_channel_select_loc = (By.ID, 'order_source')
    create_order_area_select_loc = (By.ID, 'order_area')
    create_order_start_time_picker_loc = (By.ID, 'order_delivery_start_time')
    create_order_start_time_picker_now_loc = (By.XPATH, '//button[text()="当前"]')
    create_order_start_time_picker_sure_loc = (By.XPATH, '//button[text()="确认"]')
    create_order_pay_online_radio_loc = (By.XPATH, '//input[@type="radio" and @name="pay_way" and @value="2"]')
    create_order_pay_way_select_loc = (By.ID, 'pay_channel')
    create_order_remark_textarea_loc = (By.ID, 'order_remark')
    create_order_save_btn_loc = (By.ID, 'save_order')
    
    def search_customer(self, phone):
        self.find_element(*self.customer_search_phone_text_loc).send_keys(phone)
        self.find_element(*self.customer_search_btn_loc).click()
        sleep(1)

    def save_work_bill(self):
        
        self.find_element(*self.call_show_more_link_loc).click()
        Select(self.find_element(*self.call_reason_select1_loc)).select_by_visible_text('订单')
        Select(self.find_element(*self.call_reason_select2_loc)).select_by_visible_text('创建订单')
        self.find_element(*self.call_remark_textarea_loc).send_keys("自动化测试")
        self.find_element(*self.call_save_btn_loc).click()
        sleep(1)
        
    def create_order(self):
        
        self.search_customer('18010181267')
        self.save_work_bill()
        
        self.find_element(*self.create_order_show_more_link_loc).click()
        Select(self.find_element(*self.create_order_station_select_loc)).select_by_visible_text("花家地")
        self.find_element(*self.create_order_search_text_loc).send_keys("M")
        sleep(1)
        self.find_element(*self.create_order_search_option_loc).click()
        Select(self.find_element(*self.create_order_channel_select_loc)).select_by_visible_text("其他")
        Select(self.find_element(*self.create_order_area_select_loc)).select_by_visible_text("北京")
        self.find_element(*self.create_order_start_time_picker_loc).click()
        self.find_element(*self.create_order_start_time_picker_now_loc).click()
        self.find_element(*self.create_order_start_time_picker_sure_loc).click()
        self.find_element(*self.create_order_pay_online_radio_loc).click()
        Select(self.find_element(*self.create_order_pay_way_select_loc)).select_by_visible_text("支付宝")
        self.find_element(*self.create_order_remark_textarea_loc).send_keys("自动化测试下单")
        self.find_element(*self.create_order_save_btn_loc).click()


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