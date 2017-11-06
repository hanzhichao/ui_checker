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

# -*- coding=utf-8 -*-
from util.root import project_root
=======
# -*- coding=utf-8 -*-
from util import project_root
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259


# 截图函数
def take_snapshot(driver, file_name):
    file_path = project_root() + '/report/snapshot/' + file_name
    driver.get_screenshot_as_file(file_path)


