# !/usr/bin/env python
# -*- coding=utf-8 -*-
import sys
sys.path.append("..")
from page_obj.customer.CCustomer.index import IndexPage
from test_case.base_case import BaseCase
import unittest


class TestCcustomerIndex(BaseCase):
    
    def test_search_exist_customer(self):
        """
        pre-condition: 18010181267 customer exists
        no cleaning need
        """
        phone = '18010181267'
        page = IndexPage(self.driver)
        page.load()
        page.search_phone(phone)
        
        # assert page_obj value and search value
        customer_phone = page.get_input_value('会员电话：')
        self.assertEqual(customer_phone, phone)
    
    def test_search_not_exist_customer(self):
        """
            pre-condition: 18010181261 customer not exists
            no cleaning need
        """
        phone = '18010181261'
        page = IndexPage(self.driver)
        page.load()
        page.search_phone(phone)
        customer_phone = page.get_input_value('会员电话：')
        self.assertFalse(customer_phone)

if __name__ == '__main__':
    unittest.main()
        


