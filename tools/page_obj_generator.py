# !/usr/bin/env python
# -*- coding=utf-8 -*-

import os
from util.root import PROJECT_ROOT
from util.browser import Chrome
from page.page_obj.customer.CCustomer.index import IndexPage


def fetch_links():
    driver = Chrome.headless()
    page = IndexPage(driver)
    page.login()
    links = []
    link_elements = driver.find_elements_by_xpath('//a[not(contains(@href,"javascript"))]')
    for element in link_elements:
        link = element.get_attribute("href")
        if link:
            link = link.split('/')[-3:]
            link = {os.path.join(link[0], link[1]): link[2]}
            links.append(link)
    return links


def create_page(path_dict):
    page_obj_path = os.path.join(PROJECT_ROOT,'page/page_obj/')
    page_elm_path = os.path.join(PROJECT_ROOT,'page/page_elm/')
    
    with open('page_obj.tpl') as f:
        obj_tpl = f.read()
    
    with open('page_elm.tpl') as f:
        elm_tpl = f.read()
    
    for page_dir in fetch_links():
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
            page_obj = os.path.join(page_obj_dir, page + '.py')
            page_elm = os.path.join(page_elm_dir, page + '.property')
        
            if not os.path.exists(page_obj):
                first = page[:1].upper()
                class_name = first + page[1:].capitalize()
                path = page_dir + '/' + page
                with open(page_obj, 'w') as f:
                    f.write(obj_tpl % (class_name, path, class_name))
                print("make dir %s done" % page_obj)
        
            if not os.path.exists(page_elm):
                with open(page_elm, 'w') as f:
                    f.write(elm_tpl)
                print("make dir %s done" % page_elm)
            

if __name__ == '__main__':
    link = fetch_links()
    for i in link:
        print(i)

