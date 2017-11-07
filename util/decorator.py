# !/usr/bin/env python
# -*- coding=utf-8 -*-

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
        back = func(*args, **kwargs)
        logger.debug(parent_action + '---' + func.__name__ + '---' + str("%.3fs" % (time.time()-t0)))
        return back
    return wrapper


def level(test_case):
    pass


def case_type(test_case):
    pass          # how tempest run --type=somke ?


def limit_time(func):
    pass


if __name__ == '__main__':
    l = logger
    l.debug("hello")




















if __name__ == '__main__':
    pass

