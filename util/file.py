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
import json
from configparser import ConfigParser, NoSectionError, NoOptionError, RawConfigParser
# try:
#     import xlrd
# except Exception:
#     xlrd_not_installed = True

import codecs


class JsonFile:
    def __init__(self):
        pass

    @classmethod
    def get(cls, path, key):
        with open(path, encoding='utf-8') as f:
            return json.load(f)[key]

    @classmethod
    def load(cls, path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)


class ConfFile:
    def __init__(self):
        pass

    @classmethod
    def _open(cls, path):
        # cf1 = ConfigParser()
        cf1 = RawConfigParser()
        try:
            # python 2
            with codecs.open(path, encoding='utf-8-sig') as f:
                cf1.readfp(f)
                print(cf1['runtime'])
                return cf1
            
        except IOError:
            raise IOError
            # todo logging.error()

    @classmethod
    def get(cls, path, section, option):
        cf2 = cls._open(path)
        try:
            return cf2.get(section, option)
        except NoOptionError:
            raise NoOptionError
            # todo logging.error()
            # print '文件：%s，[%s]中找不到%s项' % (path, section, option)

        except NoSectionError:
            raise NoSectionError
            # todo logging.error()
            # print '文件：%s，[%s]中找不到%s项' % (path, section, option)

    @classmethod
    def load(cls, path):
        _dict = {}
        cf3 = cls._open(path)
        # todo try ... except NoSuchKeys
        for section in cf3.sections():
            _dict[section] = {}
            for option in cf3.options(section):
                _dict[section][option] = cf3.get(section, option)
        
        return _dict
        
    @classmethod
    def load_section(cls, path, section):
        _dict = {}
        # conf = ConfigParser.ConfigParser()
        cf4 = cls._open(path)
        # todo try ... except ...
        for option in cf4.options(section):
            _dict[option] = cf4.get(section, option)
        return _dict

'''
class ExcelFile:
    def __init__(self):
        pass

    @classmethod
    def get(cls, path, sheet, row, col):
        wb = xlrd.open_workbook(path)
        if isinstance(sheet, int):
            sh = wb.sheet_by_index(sheet)
        else:
            sh = wb.sheet_by_name(sheet)
        return sh.cell_value(row, col)

    @classmethod
    def load(cls, path, sheet=0):
        wb = xlrd.open_workbook(path)
        if isinstance(sheet, int):
            sh = wb.sheet_by_index(sheet)
        else:
            sh = wb.sheet_by_name(sheet)
        cols = sh.ncols
        rows = sh.nrows
        data_list = []
        for row in range(1, rows):
            data = {}
            for col in range(0, cols):
                data[sh.cell_value(0, col)] = sh.cell_value(row, col)
            data_list.append(data)
        return data_list
'''


class XMLFile:
    def __init__(self):
        pass

    @classmethod
    def get(cls):
        pass


if __name__ == '__main__':
    conf = ConfFile()
    sleep = ConfFile.load('../conf/default.conf')
    print(sleep)

