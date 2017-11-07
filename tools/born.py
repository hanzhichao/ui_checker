# !/usr/bin/env python
# -*- coding=utf-8 -*-
"""
-------------------------------------------------------
File Name:      born.py   
Author:         Han Zhichao
Date:           2017/11/5
Description:

-------------------------------------------------------
"""
__author__ = 'Han Zhichao'
import os
from util.root import project_root


def create_page(path_dict):
    path = project_root() + '/page'
    page_obj_path = path + '/page_obj/'
    page_elm_path = path + '/page_elm/'
    
    with open('page_obj.tpl') as f:
        page_obj_tpl = f.read()
    
    with open('page_elm.tpl') as f:
        page_elm_tpl = f.read()
    
    for page_dir in path_dict:
        page_obj_dir = page_obj_path + page_dir
        page_elm_dir = page_elm_path + page_dir
        
        if not os.path.exists(page_obj_dir):
            os.makedirs(page_obj_dir)
            print("make dir %s done" % page_obj_dir)
            with open(page_obj_dir + '/' + '__init__.py', 'w') as f:
                f.write('')
            print("make file %s done" % (page_obj_dir + '/' + '__init__.py'))
        if not os.path.exists(page_elm_dir):
            os.makedirs(page_elm_dir)
            print("make dir %s done" % page_elm_dir)
        for page in path_dict[page_dir]:
            page_obj = page_obj_dir + '/' + page + '.py'
            page_elm = page_elm_dir + '/' + page + '.ini'
        
            if not os.path.exists(page_obj):
                file_name = page
                first = page[:1].upper()
                class_name = first + page[1:].capitalize()
                path = page_dir + '/' + page
                with open(page_obj, 'w') as f:
                    f.write(page_obj_tpl % (file_name, class_name, path, class_name))
                print("make dir %s done" % page_obj)
        
            if not os.path.exists(page_elm):
                with open(page_elm, 'w') as f:
                    f.write(page_elm_tpl)
                print("make dir %s done" % page_elm)
            

if __name__ == '__main__':
    test_dict = {'system1': ['page1', 'page2', 'page3'], 'system2': ['page4', 'page5']}
    create_page(test_dict)