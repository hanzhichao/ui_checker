# !/usr/bin/env python
# -*- coding=utf-8 -*-

import time
import inspect
from functools import wraps
import unittest
from threading import Thread
from threading import Timer

import sys
sys.path.append("..")
from util.log import logger

def exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        parent_action = inspect.stack()[1][4][0].strip()
        back = func(*args, **kwargs)
        _exec_time = time.time()-t0
        logger.debug(parent_action + '---' + func.__name__ + '---' + str("%.3fs" % _exec_time))
        return back
    return wrapper

def limit_time(seconds):
    def _limit_time(func): 
        def time_out():
            raise TimeoutError()
            
        @wraps(func)
        def wrapper(*args, **kwargs):
            timer = Timer(seconds, time_out)
            timer.start()
            back = func(*args, **kwargs)
            return back
        return wrapper
    return _limit_time


def level(level):
    if level==1:
        return lambda func: func
    return unittest.skip("skip this level cases")


def threads(n):
    def _threads(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("start:%s" % time.ctime())
            threads = []
            for i in range(n):
                if not args or kwargs:
                    t = Thread(target=func)
                elif args:
                    t = Thread(target=func, args=args)
                elif kwargs:
                    t = Thread(target=func, args=kwargs)
                threads.append(t)
            for i in range(n):
                threads[i].start()
            for i in range(n):
                threads[i].join()
            print("end:%s" % time.ctime())
            return func
        return wrapper
    return _threads


def case_type(test_case):
    pass          # how tempest run --type=somke ?

class Test(unittest.TestCase):
    
    @limit_time(1)
    def test_limit_time(self):
        time.sleep(3)
        print("hello")

if __name__ == '__main__':
    unittest.main()