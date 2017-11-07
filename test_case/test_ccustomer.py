# !/usr/bin/env python
# -*- coding=utf-8 -*-

from page.page_obj.customer.CCustomer.index import IndexPage
from .base_case import BaseCase


class TestCcustomer(BaseCase):
    def test_locator(self):
        
        page = IndexPage(self.driver)
        page.load()
        page.search_phone('18010181267')
        page.find_input_by_label('会员姓名：')
        page.find_input_by_label('会员电话：')
        page.find_checked_radio_by_label("性别：")
        page.find_select_by_label("客户来源：")
        page.find_selected_option_by_label('客户来源：')
        page.find_input_by_hint_text("请输入会员电话")
        
    
    def test_search_exist_customer(self):
        """
        pre-condition: 18010181267 customer exists
        no cleaning need
        """
        phone = '18010181267'
        page = IndexPage(self.driver)
        page.load()
        page.search_phone(phone)
        
        # assert page value and search value
        customer_phone = page.get_value('customer_phone')
        self.assertEqual(customer_phone, phone)

        # compare page values and db values
        where_condition = "phone='%s'" % phone
        self.assertTrue(page.compare_db_all(where_condition))
        page.logout()
        
    def test_search_not_exist_customer(self):
        phone = '18010181261'
        page = IndexPage(self.driver)
        page.load()
        page.search_phone(phone)
        customer_phone = page.get_value('customer_phone')
        self.assertFalse(customer_phone)
        page.logout()
        

        


