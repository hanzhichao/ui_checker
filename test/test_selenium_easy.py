from argparse import Action

from util.browser import Chrome
from util.selenium_easy import WebPage
import unittest
from time import sleep


class WebPageTest(unittest.TestCase):
    
    def find_input_by_hint_text(self):
        username = self.p.find_input_by_hint_text("请输入用户名")
        password = self.p.find_input_by_hint_text("请输入密码")
        self.assertEqual(username.get_attribute("placeholder"), "请输入用户名")
        self.assertEqual(password.get_attribute("placeholder"), "请输入密码")
    
    def test_find(self):
        d = Chrome.normal()
        d.get('http://jd.spicespirit.com/index/index/login/')
        p = WebPage(d)
        p.type("请输入用户名", "hanzhichao")
        p.type("请输入密码", "hanzhichao")
        p.click("登录")
        sleep(1)
        p.clicks("客服管理系统", "综合管理", "综合信息")
        sleep(1)
        p.check("性别：", 2)
        
        p.type("生日", "2019-02-03")

        # textarea_elm = p.find_textarea_by_label("备注")
        # textarea_elm.send_keys("这是一段备注")
        p.click("显示更多内容", True, 1)
        p.type_area("备注", "这是一段备注", True, 2)
        p.select("客户来源", 4)
        sleep(10)
        d.quit()
