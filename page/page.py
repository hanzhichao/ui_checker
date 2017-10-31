#  -*- coding=utf-8  -*-
import sys
import inspect
from time import sleep

from util.file import ConfFile
from selenium.webdriver.common.by import By
sys.path.append('../..')
from util.browser import Chrome
from util import config


class Page(object):

    def __init__(self, driver, base_url=config.get('env', 'base_url')):
        self.driver = driver
        self.base_url = base_url
        self.username = config.get('env', 'username')
        self.password = config.get('env', 'password')

        # 得到子类PageObject页面所对应的PageElm文件路径，并解析
        if __name__ != '__main__':
            page_obj_file = inspect.stack()[1][1]  # 获取上级调用函数的文件名
            page_elm_file = page_obj_file.replace('page_obj', 'page_elm').replace('.py', '.ini')
            _page = ConfFile.load(page_elm_file)
            self.menu = tuple(_page['page']['menu'].split(','))  # todo try...except...
            self.subject = _page['page']['subject']  # todo try...except...
            self.elements = _page['element']  # todo try...except...

    def on_page(self, subject):
        actual_subject = self.find_element(By.XPATH, '//*[@id="iframe"]/div/h1').text  # todo
        return subject == actual_subject

    def login(self):
        login_url = self.base_url + '/index/index/login'
        self.driver.get(login_url)
        sleep(1)
        self.find_element(By.ID, 'nickname').clear()
        self.find_element(By.ID, 'nickname').send_keys(self.username)
        self.find_element(By.ID, 'password').clear()
        self.find_element(By.ID, 'password').send_keys(self.password)
        self.find_element(By.ID, 'login').click()
        sleep(1)

    def logout(self):
        self.find_element(By.CLASS_NAME, 'btn-bg1').click()

    def load(self):
        # login required
        self.driver.get(self.base_url+'/index/index/index')
        self.find_element(By.PARTIAL_LINK_TEXT, self.menu[0]).click()
        self.find_element(By.LINK_TEXT, self.menu[1]).click()
        self.find_element(By.LINK_TEXT, self.menu[2]).click()
        sleep(1)
        assert self.on_page(self.subject), "Load Page Error."

    def element(self, element_name):
        element_loc = tuple(self.elements[element_name].split(','))  # todo try... except ...
        return self.find_element(*element_loc)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


if __name__ == '__main__':
    d = Chrome.headless()
    p = Page(d)
    p.login()
    print d.title
    d.quit()
