# !/usr/bin/env python
# -*- coding=utf-8 -*-

import os
import sys
sys.path.append('..')
from page_obj.index.index.login import LoginPage
from util.browser import Chrome
from util.root import PROJECT_ROOT


def fetch_links():
    driver = Chrome.headless()
    page = LoginPage(driver)
    page.login()
    links = []
    link_elements = driver.find_elements_by_xpath('//a[not(contains(@href,"javascript"))]')
    for element in link_elements:
        link = element.get_attribute("href")
        if link:
            link = link.split('/')[-3:]
            link = [os.path.join(link[0], link[1]), link[2]]
            links.append(link)
    return links


def create_page_obj_elm(path_list):
    page_obj_path = os.path.join(PROJECT_ROOT, 'page_obj/')
    # page_elm_path = os.path.join(PROJECT_ROOT, 'page_obj/')
    
    with open('page_obj.tpl') as f:
        obj_tpl = f.read()
    
    # with open('page_elm.tpl') as f:
    #     elm_tpl = f.read()
    
    for item in path_list:
        obj_dir = page_obj_path + item[0]
        # elm_dir = page_elm_path + item[0]
        
        # 在page_obj建立模块目录
        if not os.path.exists(obj_dir):
            os.makedirs(obj_dir)
            print("make dir %s done" % obj_dir)
            with open(os.path.join(obj_dir, '__init__.py'), 'w') as f:
                f.write('')
            print("make file %s done" % (obj_dir + '/' + '__init__.py'))
        # if not os.path.exists(elm_dir):
        #     os.makedirs(elm_dir)
        #     print("make dir %s done" % elm_dir)
            
        page_obj = os.path.join(obj_dir, item[1] + '.py')
        # page_elm = os.path.join(elm_dir, item[1] + '.property')
        
        if not os.path.exists(page_obj):
            class_name = item[1].capitalize()+'Page'
            with open(page_obj, 'w') as f:
                f.write(obj_tpl % (class_name, class_name))
            print("make dir %s done" % page_obj)
    
        # if not os.path.exists(page_elm):
        #     with open(page_elm, 'w') as f:
        #         f.write(elm_tpl)
        #     print("make dir %s done" % page_elm)
            

if __name__ == '__main__':
    l = fetch_links()
    create_page_obj_elm(l)

