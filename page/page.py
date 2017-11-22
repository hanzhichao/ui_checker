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

#  -*- coding=utf-8  -*-
import sys
import inspect
from time import sleep

from util.file import ConfFile
from selenium.webdriver.common.by import By
from util.browser import Chrome
from util import config
from util.decorator import exec_time
from util.root import project_root
from util.db import DB


class Page(object):
    page = ''
    
=======
from util.decorator import show_duration


class Page(object):

    def __init__(self, driver, base_url=config.get('env', 'base_url')):
        self.driver = driver
        self.base_url = base_url
        self.username = config.get('env', 'username')
        self.password = config.get('env', 'password')

        # 得到子类PageObject页面所对应的PageElm文件路径，并解析
        if __name__ != '__main__':
            # page_obj_file = inspect.stack()[1][1]  # 获取上级调用函数的文件名
            # page_elm_file = page_obj_file.replace('page_obj', 'page_elm').replace('.py', '.ini')
            page_elm_file = project_root() + "/page/page_elm/" + self.page + ".ini"
            self.page_conf = ConfFile.load(page_elm_file)
            # self.menu = tuple(page_conf['page']['menu'].split(','))  # todo try...except...
            # self.subject = page_conf['page']['subject']  # todo try...except...
            elements_conf = self.page_conf['element']  # todo try...except...
            for element_name in elements_conf:
                elements_conf[element_name] = tuple(elements_conf[element_name].split(','))
            self.elements = elements_conf
            
    def on_page(self, subject):
        actual_subject = self._find_element(By.XPATH, '//*[@id="iframe"]/div/h1').text  # todo
        print("实际文本：%s" % actual_subject, "配置文件中的文本：%s" % subject)
        # return subject == actual_subject
        return subject in actual_subject

    @exec_time
            print '---------------------------------------------------------------------'
            print inspect.stack()
            page_obj_file = inspect.stack()[1][1]  # 获取上级调用函数的文件名
            page_elm_file = page_obj_file.replace('page_obj', 'page_elm').replace('.py', '.ini')
            _page = ConfFile.load(page_elm_file)
            self.menu = tuple(_page['page']['menu'].split(','))  # todo try...except...
            self.subject = _page['page']['subject']  # todo try...except...
            self.elements = _page['element']  # todo try...except...

    def on_page(self, subject):
        actual_subject = self.driver.find_element(By.XPATH, '//*[@id="iframe"]/div/h1').text  # todo
        return subject == actual_subject

    @show_duration
    def login(self):
        login_url = self.base_url + '/index/index/login'
        self.driver.get(login_url)
        sleep(1)
        self._find_element(By.ID, 'nickname').clear()
        self._find_element(By.ID, 'nickname').send_keys(self.username)
        self._find_element(By.ID, 'password').clear()
        self._find_element(By.ID, 'password').send_keys(self.password)
        self._find_element(By.ID, 'login').click()
        sleep(1)

    def logout(self):
        self._find_element(By.CLASS_NAME, 'btn-bg1').click()

    def _load(self, page=page):
        # login required
        # self.driver.get(self.base_url+'/index/index/index')
        page_elm_file = project_root() + "/page/page_elm/" + page + ".ini"
        self.page_conf = ConfFile.load(page_elm_file)
        menu = tuple(self.page_conf['page']['menu'].split(','))  # todo try...except...
        subject = self.page_conf['page']['subject']  # todo try...except...
        
        self._find_element(By.PARTIAL_LINK_TEXT, menu[0]).click()
        self._find_element(By.LINK_TEXT, menu[1]).click()
        self._find_element(By.LINK_TEXT, menu[2]).click()
        sleep(1)
        assert self.on_page(subject), "Load Page Error."
    
    @exec_time
    def load(self):
        self.login()
        self._load(self.page)
        
    @exec_time
    def turn_to(self, page):  # maybe bugs exists when turn_to other page
        self.driver.refresh()
        self._load(page)
        
    @exec_time
    def find_element(self, element_name):
        element_loc = self.elements[element_name]  # todo try... except ...
        return self._find_element(*element_loc)
    
    def _find_element(self, *loc):
        return self.driver.find_element(*loc)
    
    @exec_time
    def get_value(self, element_name):
        return self.find_element(element_name).get_attribute('value')
    
    @exec_time
    def get_text(self, element_name):
        return self.find_element(element_name).text
    
    @exec_time
    def logout(self):
        self.find_element(By.CLASS_NAME, 'btn-bg1').click()

    @show_duration
    def load(self):
        # login required
        self.driver.get(self.base_url+'/index/index/index')
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.menu[0]).click()
        self.driver.find_element(By.LINK_TEXT, self.menu[1]).click()
        self.driver.find_element(By.LINK_TEXT, self.menu[2]).click()
        sleep(1)
        assert self.on_page(self.subject), "Load Page Error."

    def element(self, element_name):
        element_loc = tuple(self.elements[element_name].split(','))  # todo try... except ...
        return self.driver.find_element(*element_loc)

    @show_duration
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    @show_duration
    def type(self, element, *value):
        element.clear()
        element.send_keys(*value)

    @exec_time
    def open(self, url):
        self.driver.get(url)

    @exec_time
    def get_db_map(self, element_name):
        return tuple(self.page_conf['db_map'][element_name].split(','))
    
    @exec_time
    def get_db_value(self, element_name, where_condition):
        db = DB()
        db_map = self.get_db_map(element_name)
        return db.get(key=db_map[0], table=db_map[1], where_condition=where_condition)[0]
    
    @exec_time
    def compare_db(self, element_name, where_condition):
        page_element_value = self.get_value(element_name)
        element_db_map_value = self.get_db_value(element_name, where_condition)
        return page_element_value == element_db_map_value


if __name__ == '__main__':
    d = Chrome.normal()
    # d.get('https://www.baidu.com')
    p = Page(d)
    p.login()
    print(d.title)
=======
    @show_duration
    def open(self, url):
        self.driver.get(url)


if __name__ == '__main__':
    d = Chrome.headless()
    p = Page(d)
    p.login()
    print d.title
    d.quit()
