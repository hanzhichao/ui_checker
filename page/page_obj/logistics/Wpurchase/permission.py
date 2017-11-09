# !/usr/bin/env python
# -*- coding=utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from page.base_page import BasePage
from util.browser import Chrome


class PermissionPage(BasePage):
    page = __file__
    
    def change_station_purchaser(self, station_name):
        sleep(1)
        try:
            cur_purchaser = self.find_element('cur_purchaser').text
            print(cur_purchaser)
            if cur_purchaser != "韩志超":
                self.input('姓名：').send_keys(cur_purchaser[:2])
                sleep(1)
                self.find_element('name_list_cur_purchaser').click()
                sleep(1)
                self.find_element('station_checkbox').click()
                self.find_element('add_btn').click()

                self.input('姓名：').send_keys('韩志超')
                sleep(1)
                self.find_element('hanzhichao').click()
                sleep(1)
                self.find_element('station_checkbox').click()
                self.find_element('add_btn').click()

            else:
                print("青年路已绑定韩志超")
        except NoSuchElementException:
            print("青年路未绑定站点")
            self.input('姓名：').send_keys('韩志超')
            sleep(1)
            self.find_element('hanzhichao').click()
            sleep(1)
            self.find_element('station_checkbox').click()
            self.find_element('add_btn').click()


if __name__ == '__main__':
    d = Chrome.normal()
    # d = Chrome.headless()
    p = PermissionPage(d)
    p.load()
    p.change_station_purchaser('立水桥')
    sleep(5)
    d.quit()
