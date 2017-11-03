import unittest
import sys
sys.path.append('..')
from util.browser import Chrome


class Base(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome.normal()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()