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

def by_xpath(dr, xpath):
    return dr.find_element_by_xpath(xpath)


def find_input_by_label(dr, label):
    return dr.by_xpath('//label[text()=%s]/fllowing::input[1]' % label)


def find_input_by_hint_text(dr, hint_text):
    return dr.by_xpath('//input[@placeholder=%d]' % hint_text)


def find_input_by_value(dr, value):
    return dr.by_xpath('//input[@value=%d]' % value)


def find_element_by_text(dr, text):
    return dr.by_xpath('//*[text()=%d]' % text)


def find_radio_by_label(dr, label):
    return dr.by_xpath('//label[text()=%s]/following::input[@type="radio"][1]' % label)


def find_checked_radio_by_label(dr, label, checked="checked"):
    return dr.by_xpath('//label[text()=%s]/following::input[@type="radio"][@checked="checked"][1]' % label)


def find_select_by_label(dr, label):
    return dr.by_xpath('//label[text()=%s]/fllowing::select[1]' % label)


def find_selected_option_by_label(dr, label, selected="selected"):
    return dr.by_xpath('//label[text()=%s]/fllowing::select[1]/following::option[@selected="selected"]' % label)


def find_text_by_table_column_name(dr, columen_name, n):  # n means row_index=n,begin with 1
    pass


def link(dr, link_text):
    return dr.find_element_by_link_text(link_text)


def button(dr, value):
    return dr.by_xpath('//input[@type="button"][@value=%d]' % value)


def input(dr, label):
    return find_input_by_label(dr, label)


def select(dr, lavel):
    pass


def radio(label):
    pass


def tabel(top_left_text):
    pass

