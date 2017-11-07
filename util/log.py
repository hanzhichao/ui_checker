# !/usr/bin/env python
# -*- coding=utf-8 -*-

import logging
import time
from util.config import Config
from util.root import project_root


# def log():
conf = Config()
log_dir = conf.get('runtime', 'log_dir')
date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
log_file = project_root() + log_dir + date + '.log'


# 第一步，创建一个logger
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)    # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
fh = logging.FileHandler(log_file, mode='a')
fh.setLevel(logging.DEBUG)   # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)   # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

# return logger
