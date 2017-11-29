# !/usr/bin/env python
# -*- coding=utf-8 -*-
import sys
sys.path.append("..")
from page_obj.customer.CCustomer.index import IndexPage
from test_case.base_case import BaseCase
import unittest
from util.decorator import level


class TestCcustomerIndex(BaseCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestCcustomerIndex, cls).setUpClass()
        cls.page = IndexPage(cls.driver)
        cls.page.load()
    
    def test_search_exist_customer(self):
        """
        pre-condition: 18010181267 customer exists
        no cleaning need
        """
        phone = '18010181267'
        self.page.search_phone(phone)
        # assert page_obj value and search value
        customer_phone = self.page.get_input_value('会员电话：')
        self.assertEqual(customer_phone, phone)

    @level(2)
    def test_search_not_exist_customer(self):
        """
            pre-condition: 18010181261 customer not exists
            no cleaning need
        """
        phone = '18010181261'
        self.page.search_phone(phone)
        customer_phone = self.page.get_input_value('会员电话：')
        self.assertFalse(customer_phone)

if __name__ == '__main__':  
    unittest.main(verbosity=2)
        


