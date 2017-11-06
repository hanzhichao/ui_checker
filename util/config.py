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

from util.file import ConfFile
from util.root import project_root
=======
from file import ConfFile
from util import project_root
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259


def get_all():
    path = project_root() + '/conf/default.conf'
    return ConfFile.load(path)


def get_section(section):
    path = project_root() + '/conf/default.conf'
    return ConfFile.load_section(path, section)


def get(section, option):
    path = project_root() + '/conf/default.conf'
    return ConfFile.get(path, section, option)


class Config(object):
    def __init__(self, path='../conf/default.conf'):
        self.path = path
        self._dict = ConfFile.load(path)

    def config(self):
        return self._dict

    def section(self, section):
        try:
            return self._dict[section]
        except KeyError:
            raise KeyError

    def get(self, section, option):
        section_dict = self.section(section)
        try:
            return section_dict[option]
        except KeyError:
            raise KeyError


if __name__ == '__main__':
    conf = Config()
<<<<<<< HEAD
    print(conf.get('email', 'smtp_server'))
=======
    print conf.get('email', 'smtp_server')
>>>>>>> c981237763b50a6ecfb387b2b7de98b5aa55d259
