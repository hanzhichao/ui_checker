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

import time
import inspect

from util.log import logger


def show_duration(action):
    start = time.clock()
    
    def wrapper(*args, **kwargs):
        return action(*args, **kwargs)

    end = time.clock()
    duration = end - start
    parent_action = inspect.stack()[1][4][0].strip()
    # inspect.getargspec(action)
    # varnames = action.__code__.co_varnames
    print('{0}---{1}---{2}s'.format(parent_action, action.__name__, duration))
    return wrapper


def exec_time(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        parent_action = inspect.stack()[1][4][0].strip()
        # print("@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__))
        back = func(*args, **kwargs)
        # print("@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__))
        print("@%.3fs taken for {%s}" % (time.time() - t0, func.__name__))
        # logger.debug(parent_action, func.__name__, time.time()-t0)
        return back
    return wrapper


def level(test_case):
    """
    0: smoke case
    1:
    :param test_case:
    :return:
    """
    pass


def case_type(test_case):
    pass          # how tempest run --type=somke ?


def limit_time(func):
    pass





















if __name__ == '__main__':
    pass

