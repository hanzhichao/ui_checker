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

# coding=utf-8
import logging
import time
import os
from config import Config


conf = Config()
log_dir = conf.get('runtime', 'log_dir')
date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
log_file = os.path.join(log_dir, date+'.log')


# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)    # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
fh = logging.FileHandler(log_file, mode='a')
fh.setLevel(logging.DEBUG)   # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')
