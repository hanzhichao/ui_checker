# !/usr/bin/env python
# -*- coding=utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from util.log import logger

class WebPage(object):
    
    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
    
    def by_xpath(self, xpath, multi=False, index=None):
        if not multi:
            return self.driver.find_element_by_xpath(xpath)
        elif index is not None:
            logger.debug(index, type(index))
            logger.debug(self.driver.find_elements_by_xpath(xpath))
            return self.driver.find_elements_by_xpath(xpath)[index-1]
        else:
            return self.driver.find_elements_by_xpath(xpath)
    
    def find_input_by_label(self, label, multi=False, index=None):
        return self.by_xpath('//*[contains(text(),"%s")]/following::input[1]|textarea[1]' % label, multi, index)
    
    def find_textarea_by_label(self, label, multi=False, index=None):
        return self.by_xpath('//*[contains(text(),%s)]/following::textarea[1]' % label, multi, index)
    
    def find_input_by_hint_text(self, hint_text, multi=False, index=None):
        return self.by_xpath('//input[@placeholder="%s"]' % hint_text, multi, index)
    
    def find_textarea_by_hint_text(self, hint_text, multi=False, index=None):
        return self.by_xpath('//textarea[@placeholder="%s"]' % hint_text, multi, index)
    
    def find_element_by_text(self, text, multi=False, index=None):
        try:
            return self.by_xpath("//*[(text()='%s']" % text, multi, index)
        except NoSuchElementException:
            try:
                return self.by_xpath("//*[contains(text(),%s]" % text, multi, index)
            except NoSuchElementException:
                logger.debug("页面上找不到该文本")

    def find_radio_by_group_label(self, label, n, multi=False, index=None):
        return self.by_xpath('//*[contains(text(),"%s")]/following::'
                             'input[@type="radio"][%d]' % (label, n), multi, index)

    def find_radio_by_label(self, label, multi=False, index=None):
        return self.by_xpath("//*[text()='%s']/preceding::input[@type='radio'][1]" % label, multi, index)
       
    def find_select_by_label(self, label, multi=False, index=None):
        return self.by_xpath('//*[contains(text(),"%s")]/following::select[1]' % label, multi, index)

    def find_text_by_table_column_name(self, column_name, n, multi=False, index=None):  # n means row_index=n,begin with 1
        pass
    
    def find_button_by_value(self, value, multi=False, index=None):
        try:
            return self.by_xpath('//input[@type="button"][@value="%s"]' % value, multi, index)
        except NoSuchElementException:
            logger.debug("找不到按钮'%s',尝试寻找该文本链接..." % value)
            return self.find_link_by_text(value)
        except IndexError:
            logger.debug("找不到按钮'%s',尝试寻找该文本链接..." % value)
            return self.find_link_by_text(value)
        
    def find_link_by_text(self, text, multi=False, index=None):
        try:
            return self.driver.find_element_by_link_text(text)
        except NoSuchElementException:
            try:
                logger.debug("找不到与文本'%s'完全一致的链接，尝试寻找包含该文本的链接..." % text)
                return self.driver.find_element_by_partial_link_text(text)
            except NoSuchElementException:
                logger.debug("找不到文本包含'%s'的链接，尝试去掉空格完全匹配..." % text)
            try:
                return self.by_xpath('//a[normalize-space(contains(text(),"%s"))]' % text, multi, index)
            except NoSuchElementException:
                logger.debug("找不到文本为%s的链接或按钮")
                
    # --------------element action---------------------
    def type(self, label, text, multi=False, index=None):
        try:
            input_elm = self.find_input_by_label(label, multi, index)
            input_elm.clear()
            input_elm.send_keys(text)
        except NoSuchElementException:
            try:
                input_elm = self.find_input_by_hint_text(label, multi, index)
                input_elm.clear()
                input_elm.send_keys(text)
            except NoSuchElementException:
                logger.debug("标签或提示文字为%s的输入框定位失败！" % label)
        # finally:
        #     self.click()
    
    def type_date(self, label, date):
        self.type(label, date)
        self.click()
        
    def type_area(self, label, text, multi=False, index=None):
            try:
                textarea_elm = self.find_textarea_by_label(label, multi, index)
                textarea_elm.send_keys(text)
            except NoSuchElementException:
                try:
                    textarea_elm = self.find_textarea_by_hint_text(label, multi, index)
                    textarea_elm.send_keys(text)
                except NoSuchElementException:
                    logger.debug("标签或提示文字为%s的文本框定位失败！" % label)
                
    def click(self, text, multi=False, index=None):
        if isinstance(text, str):
            self.find_button_by_value(text, multi, index).click()
        elif isinstance(text, tuple or list):
            self.clicks(text)
    
    def clicks(self, *args):
        if len(args) == 1:
            for text in args[0]:
                self.find_link_by_text(text).click()
        if len(args) > 1:
            for text in args:
                self.find_link_by_text(text).click()
        elif not args:
            self.by_xpath("//body").click()
   
    def click_element(self, *loc):
        self.find_element(*loc).click()
        
    def check(self, *args):
        if len(args) == 1:
            self.find_radio_by_label(args).click()
        elif len(args) == 2:
            if isinstance(args[1], int):
                self.find_radio_by_group_label(args[0], args[1]).click()
            elif isinstance(args[1], str):
                self.find_radio_by_label(args[1]).click()
    
    def select(self, label, option):
        select_elm = Select(self.find_select_by_label(label))
        if isinstance(option, str):
            select_elm.select_by_visible_text(option)
        elif isinstance(option, int):
            select_elm.select_by_index(option-1)
       
    # -----------------------get value------------------------
    def get_input_value(self, label):
        return self.find_input_by_label(label).get_attribute('value')
    
    def get_textarea_text(self, label):
        return self.find_textarea_by_label(label).text
    
    def get_radio_value(self, label):
        return self.by_xpath('//*[contains(text(),"%s")]/following::input[@type="radio"]'
                             '[@checked="checked"][1]' % label).get_attribute("value")
    
    def get_select_value(self, label):
        return Select(self.find_select_by_label(label)).first_selected_option.text
