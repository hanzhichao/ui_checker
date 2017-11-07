# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep
from util.log import logger
from util.config import Config, Property
from selenium.webdriver.common.by import By
from util.browser import Chrome
from util.decorator import exec_time
from util.db import DB


class BasePage(object):
    page = __file__
    SLEEP_TIME = float(Config.option('runtime', 'sleep'))
    
    def __init__(self, driver, base_url=Config.option('env', 'base_url')):
        self.driver = driver
        self.base_url = base_url
        
        if __name__ != '__main__':
            self.property = Property(self.page).property

    # -----------------------page methods----------------------------------
    @exec_time
    def open(self, url):
        self.driver.get(url)
    
    def _login(self, driver, base_url, username, password):
        login_url = base_url + '/index/index/login'
        driver.get(login_url)
        sleep(self.SLEEP_TIME)
        driver.find_element(By.ID, 'nickname').clear()
        driver.find_element(By.ID, 'nickname').send_keys(username)
        driver.find_element(By.ID, 'password').clear()
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.ID, 'login').click()
        sleep(self.SLEEP_TIME)

    @exec_time
    def login(self):
        username = Config.option('env', 'username')
        password = Config.option('env', 'password')
        self._login(self.driver, self.base_url, username, password)

    def logout(self):
        self._find_element(By.CLASS_NAME, 'btn-bg1').click()

    def on_page(self, subject):
        actual_subject = self._find_element(By.XPATH, '//*[@id="iframe"]/div/h1').text
        logger.debug("page subject：%s" % actual_subject + "---config subject：%s" % subject)
        return subject in actual_subject

    def _load(self, menu, subject):
        self._find_element(By.PARTIAL_LINK_TEXT, menu[0]).click()
        self._find_element(By.LINK_TEXT, menu[1]).click()
        self._find_element(By.LINK_TEXT, menu[2]).click()
        sleep(self.SLEEP_TIME)
        assert self.on_page(subject), "Not on page!"
    
    @exec_time
    def load(self):
        self.login()
        menu = self.property['page']['menu']
        subject = self.property['page']['subject']
        self._load(menu, subject)
        
    @exec_time
    def turn_to(self, page):  # maybe bugs exists when turn_to other page
        self.driver.refresh()
        self._load(page)
     
    # -----------------------element methods-------------------------------
    
    def _find_element(self, *loc):
        return self.driver.find_element(*loc)
      
    @exec_time
    def find_element(self, element_name):
        elements = self.property['element']
        element_loc = elements[element_name]
        return self._find_element(*element_loc)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_input_by_label(self, label):
        return self.by_xpath('//label[text()="%s"]/following::input[1]' % label)

    def find_input_by_hint_text(self, hint_text):
        return self.by_xpath('//input[@placeholder="%s"]' % hint_text)

    def find_input_by_value(self, value):
        return self.by_xpath('//input[@value="%s"]' % value)

    def find_element_by_text(self, text):
        return self.by_xpath('//*[text()="%s"]' % text)

    def find_radios_by_label(self, label):
        return self.by_xpath('//label[text()="%s"]/following::input[@type="radio"][1]' % label)

    def find_checked_radio_by_label(self, label):
        return self.by_xpath('//label[text()="%s"]/following::input[@type="radio"][@checked="checked"][1]' % label)

    def find_select_by_label(self, label):
        return self.by_xpath('//label[text()="%s"]/following::select[1]' % label)

    def find_selected_option_by_label(self, label):
        return self.by_xpath('//label[text()="%s"]/following::select[1]/option[@selected="selected"]' % label)

    def find_text_by_table_column_name(self, column_name, n):  # n means row_index=n,begin with 1
        pass
    
    def find_button_by_value(self, value):
        return self.by_xpath('//input[@type="button"][@value="%s"]' % value)
    
    def link(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def button(self, value):
        return self.find_button_by_value(value)

    def input(self, label):
        return self.find_input_by_label(label)

    def select(self, label):
        return self.find_select_by_label(label)

    def radios(self, label):
        return self.find_radios_by_label(label)
    
    def checked_radio(self, label):
        return self.find_checked_radio_by_label(label)

    def table(self, top_left_text):
        pass
    
    def selected_option(self, label):
        return self.find_selected_option_by_label(label)
    
    @exec_time
    def get_value(self, element_name):
        return self.find_element(element_name).get_attribute('value')
    
    @exec_time
    def get_text(self, element_name):
        return self.find_element(element_name).text

    # -----------------------db methods-------------------------------------
    @exec_time
    def get_db_value(self, element_name, where_condition):
        db = DB()
        db_map = self.property['db_map'][element_name]
        value = db.get(key=db_map[0], table=db_map[1], where_condition=where_condition)[0]
        return str(value)
    
    def compare_db(self, element_name, where_condition):
        element_page_value = self.get_value(element_name)
        if not element_page_value:
            element_page_value = self.get_text(element_name)
        element_db_value = self.get_db_value(element_name, where_condition)
        logger.debug("%s---%s---%s", element_name, element_page_value, element_db_value)
        return element_page_value == element_db_value
    
    def compare_db_all(self, where_condition):
        result = 1
        for element_name in self.property['db_map']:
            result = result and self.compare_db(element_name, where_condition)
        return result
        
        
if __name__ == '__main__':
    d = Chrome.headless()
    # d.get('https://www.baidu.com')
    p = BasePage(d)
    # p.login()
    # print(d.title)
    d.quit()
