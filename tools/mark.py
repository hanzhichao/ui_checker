# !/usr/bin/env python
# -*- coding=utf-8 -*-
"""
-------------------------------------------------------
File Name:      mark.py   
Author:         Han Zhichao
Date:           2017/11/5
Description:

-------------------------------------------------------
"""
import time

import os
from util.root import project_root

__author__ = 'Han Zhichao'


def mark(py_file):
    """
    add doc header to the python file
    :param py_file: python file name with path
    :return: null
    """
    with open('header.txt') as f:
        header = f.read() % (os.path.basename(__file__), time.strftime("%Y/%m/%d"))
    
    with open(py_file, 'r', encoding='UTF-8') as f:
        origin = f.read()
    if '# !/usr/bin/env python' not in origin:
        with open(py_file, 'w', encoding='UTF-8') as f:
            f.write(header)
            f.write(origin)


def mark_all(path):
    
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if name[-3:] == '.py' and name != '__init__.py':
                print(os.path.join(root, name))
                mark(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))


def crlf2lf():
    pass


def lf2crlf():
    pass


if __name__ == '__main__':
    mark('cli.py')
    mark_all(project_root())
