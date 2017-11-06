<<<<<<< HEAD
# !/usr/bin/env python
# -*- coding=utf-8 -*-

"""
-------------------------------------------------------
File Name:      mark.py
Author:         Han Zhichao
Date:           2017/11/05
Description:

-------------------------------------------------------
"""
__author__ = 'Han Zhichao'

from time import sleep

from .base import Base
=======
from time import sleep

from base import Base
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259
from page.page_obj.customer.ccustomer import CCustomer


class TestCcustomer(Base):
<<<<<<< HEAD
    
    def test_search_exist_customer(self):
        phone = '18010181267'
        page = CCustomer(self.driver)
        page.load()
        page.search_phone(phone)
        
        # page values
        customer_phone = page.get_value('customer_phone')
        customer_username = page.get_value('customer_username')
        customer_id_card = page.get_value('customer_id_card')
        customer_sex = page.get_text('customer_id_card')
        customer_birthday = page.get_value('customer_birthday')
        customer_nation = page.get_value('customer_id_card')
        customer_source = page.get_text('customer_id_card')
        customer_remark = page.get_text('customer_id_card')

        # db values
        where_condition = "phone='%s'" % phone
        db_customer_username = page.get_db_value('customer_username', where_condition)
        db_customer_phone = page.get_db_value('customer_phone', where_condition)
        db_customer_id_card = page.get_db_value('customer_id_card', where_condition)
        db_customer_sex = page.get_db_value('customer_sex', where_condition)
        db_customer_birthday = page.get_db_value('customer_birthday', where_condition)
        db_customer_nation = page.get_db_value('customer_nation', where_condition)
        db_customer_source = page.get_db_value('customer_source', where_condition)
        db_customer_remark = page.get_db_value('customer_remark', where_condition)
        
        # compare search result and expect
        self.assertEqual(customer_phone, phone)
        
        # compare search result and db_map
        self.assertEqual(customer_username, db_customer_username)
        self.assertEqual(customer_phone, db_customer_phone)
        self.assertEqual(customer_id_card, db_customer_id_card)
        
        print(page.find_element('customer_sex'))
        sleep(10)
        
        print("--------------")
        print(customer_sex, db_customer_sex)
        self.assertEqual(customer_sex, db_customer_sex)
        self.assertEqual(customer_birthday, db_customer_birthday)
        self.assertEqual(customer_nation, db_customer_nation)
        self.assertEqual(customer_source, db_customer_source)
        self.assertEqual(customer_remark, db_customer_remark)

=======
    def test_search_customer(self):
        page = CCustomer(self.driver)
        page.login()
        page.load()
        page.search_phone('18010181267')
        sleep(10)
        self.driver.quit()
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259
