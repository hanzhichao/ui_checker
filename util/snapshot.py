# -*- coding=utf-8 -*-
from util import project_root


# 截图函数
def take_snapshot(driver, file_name):
    file_path = project_root() + '/report/snapshot/' + file_name
    driver.get_screenshot_as_file(file_path)


