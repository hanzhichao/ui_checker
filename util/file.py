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
from configparser import ConfigParser, NoSectionError, NoOptionError
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
        conf = ConfigParser()
        try:
            with codecs.open(path, encoding='utf-8-sig') as f:
                conf.read_file(f)
                return conf
        except IOError:
            raise IOError
            # todo logging.error()

    @classmethod
    def get(cls, path, section, option):
        conf = cls._open(path)
        try:
            return conf.get(section, option)
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
        conf = cls._open(path)
        # todo try ... except NoSuchKeys
        for section in conf.sections():
            _dict[section] = {}
            for option in conf.options(section):
                _dict[section][option] = conf.get(section, option)
        
        return _dict
        
    @classmethod
    def load_section(cls, path, section):
        _dict = {}
        # conf = ConfigParser.ConfigParser()
        conf = cls._open(path)
        # todo try ... except ...
        for option in conf.options(section):
            _dict[option] = conf.get(section, option)
        return _dict


# class ExcelFile:
#     def __init__(self):
#         pass
#
#     @classmethod
#     def get(cls, path, sheet, row, col):
#         wb = xlrd.open_workbook(path)
#         if isinstance(sheet, int):
#             sh = wb.sheet_by_index(sheet)
#         else:
#             sh = wb.sheet_by_name(sheet)
#         return sh.cell_value(row, col)
#
#     @classmethod
#     def load(cls, path, sheet=0):
#         wb = xlrd.open_workbook(path)
#         if isinstance(sheet, int):
#             sh = wb.sheet_by_index(sheet)
#         else:
#             sh = wb.sheet_by_name(sheet)
#         cols = sh.ncols
#         rows = sh.nrows
#         data_list = []
#         for row in range(1, rows):
#             data = {}
#             for col in range(0, cols):
#                 data[sh.cell_value(0, col)] = sh.cell_value(row, col)
#             data_list.append(data)
#         return data_list


class XMLFile:
    def __init__(self):
        pass

    @classmethod
    def get(cls):
        pass


if __name__ == '__main__':
    pass
