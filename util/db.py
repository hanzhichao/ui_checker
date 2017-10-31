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

import pymysql
from util.config import get_section
from util.decorator import exec_time


class DB(object):
    def __init__(self, *args, **kwargs):
        db_conf = get_section('db')
        self.conn = pymysql.connect(host=db_conf['host'],
                                    port=int(db_conf['port']),
                                    user=db_conf['user'],
                                    passwd=db_conf['passwd'],
                                    db=db_conf['db'],
                                    charset='utf8')
        self.cursor = self.conn.cursor()
    
    # def __del__(self):
    #     self.cursor.close()
    #     self.conn.close()
    
    @exec_time
    def exec_sql(self, sql):
        print(sql)
        effect_row = self.cursor.execute(sql)
        return self.cursor.fetchall()

    @exec_time
    def get(self, key, table, where_condition):
        sql = "SELECT %s FROM %s WHERE %s" % (key, table, where_condition)
        effect_row = self.cursor.execute(sql)
        return self.cursor.fetchone()


if __name__ == '__main__':
    db = DB()
    result = db.exec_sql("SELECT username FROM u_user WHERE phone='18010181267'")
    print(result)
    result = db.get('username', 'u_user', "phone='18010181267'")
    print(result)

