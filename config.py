# !/usr/bin/env python
# -*- coding=utf-8 -*-

from util.data_file_parser import ConfFile
from util.root import CONFIG_FILE


class Config(object):
    conf = ConfFile.load(CONFIG_FILE)
    
    def __init__(self, config_file=CONFIG_FILE):
        self.conf = ConfFile.load(config_file)

    @classmethod
    def section(cls, section):
        return cls.conf[section]
    
    @classmethod
    def option(cls, section, option):
        section_dict = cls.section(section)
        return section_dict[option]


class Property(object):
    
    @staticmethod
    def _match_property(page):
        page_elm_file = page.replace('page_obj', 'page_elm').replace('.py', '.property')
        return page_elm_file
    
    @staticmethod
    def load(_property):
        _property['page_obj']['menu'] = tuple(_property['page_obj']['menu'].split(','))
    
        _elements = _property['element']
        for element in _elements:
            _elements[element] = tuple(_elements[element].split(','))
    
        _db_map = _property['db_map']
        for element in _db_map:
            _db_map[element] = tuple(_db_map[element].split(','))
    
        _property['element'] = _elements
        _property['db_map'] = _db_map
        return _property

    def __init__(self, page):
        _property = ConfFile.load(self._match_property(page))
        self.property = self.load(_property)
    
   
if __name__ == '__main__':
    print(Config.conf)
