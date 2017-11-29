[TOC]
# ui_checker

>麻辣诱惑后台管理系统UI自动化测试项目，基于python + selenium + unittest


## 主要特性
1. 采用PageObject模式封装每个操作页面，支持页面与元素分离
2. 支持selenium_easy模式，按人类习惯，通过链接/按钮文字，Form前置标签识别/操作控件，支持多个相同标签控件的识别
3. 支持Json/XML/CSV/Excel/Config类型的数据文件解析，支持将数据文件完整解析成dict格式，或从中获取某个值
4. 支持数据连接及对比数据库的值
5. 支持Chrome Headless无界面模式运行，支持Grid分布式运行或Remote模式
6. 支持按模块并发执行用例，每个模块生成各自的报告
7. 支持邮件/截图/log
8. 支持显示webdriver各项操作消耗时间，支持time_out设置，支持多线程重复某一操作， 支持制定test case level
9. 支持 Windows/Linux + python2.*/python3.* 

## 使用方法
### 运行环境
>推荐 Windows 7/10 + Python 3.* + selenium3.5 + Chrome 62以上
> 或 CentOS 7.* + Python2.7 + selenium3.5 + google-chrome-stable最新版

以Windows为例：

1. 下载安装Chrome最新版
2. 下载安装Git Windows客户端
3. 下载安装python3.6.3（自动安装pip和配置好环境变量）
4. 安装python第三方库，打开cmd
```
pip install selenium
pip install pymysql
pip install xlrd
```

### 使用项目
1. 克隆项目，打开cmd
```
git@192.168.100.240:hanzhichao/ui_checker.git
cd ui_checker
```
2. 配置项目
```
打开conf/default.conf
修改[env]下base_url及登录用户名和密码,保存
```
3. 执行所有用例
```
python run_all_test.py
```

### 编写用例
1. 完善page_obj对象
```
1.1 根据页面菜单url确定所在模块，如"综合管理系统>部门管理>新增部门" 页面链接为.../admin/ADepartment/create
1.2 打开page_obj/目录下对应的模块下对应的py文件，如page_obj/admin/ADepartment/create.py
1.3 完善menu和subject：
    如menu='综合管理系统','部门管理','新增部门'（用于加载页面，注意：中间为英文逗号），
    subject='部门信息'（页面主体，第一个头部主题，用于判断页面是否加载成功）
1.4 封装页面操作，3种方式，参考page_obj/customer/CCustumer/下的：
    index.py(selenium_easy模式)
    index2.py(标准PageObj模式)
    index3.py+index3.property(元素分离模式)
```
2. 编写测试用例
```
进入test_case/相应模块下，如test_case/admin
新建test_adepartment_create.py文件
编写该页面相关的用例，参考test_case/customer/test_ccustomer_index.py
```
3. page_obj示例
```
# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep

from page_obj.base_page import BasePage
from page_obj.index.index.login import LoginPage
from util.browser import Chrome
from util.db import DB
from util.selenium_easy import Element, Input


class IndexPage(BasePage):
    menu = ('客服管理系统', '综合管理', '综合信息')
    subject = '会员信息'
 
    def search_phone(self, phone):
        self.type('电话搜索：', phone)
        self.click_btn('搜索')
        self.sleep()
        
    def save_work_bill(self):
        self.click("显示更多内容")
        
        self.select("来电原由", "订单")
        self.select("来电原由", "创建订单", 2)
        self.type_area("备注", "自动化测试", 2)
        self.click_btn("保存", 2)
        
    def create_order(self, phone, station, code):
        self.search_phone(phone)
        self.save_work_bill()
        self.click("显示更多内容", 4)
        self.select("配送站点", station)
        self.type("请输入要查询商品的简码", code)
        sleep(1)
        self.click_text("麻酱烧饼")
        self.select("订单渠道：", "电话")
        self.select("订单区域", "北京")
        self.click_input("是否预定送餐时间", 4)
        self.click_btn("当前")
        self.click_btn("确认")
        self.check("支付方式", 1)
        self.select("支付方式", "支付宝")
        self.type_area("备注", "自动化测试下单", 3)
        self.click_btn("保存", 3)
        
        
if __name__ == '__main__':
    d = Chrome.normal()
    # d = Chrome.headless()
    d.maximize_window()
    l = LoginPage(d)
    l.login()
    p = IndexPage(d)
    p.load()
    p.create_order('18010181267', '花家地', 'M')
    sleep(10)
    d.quit()

```
4. 测试用例示例
test_case/customer/test_ccustomer_index.py
```
# !/usr/bin/env python
# -*- coding=utf-8 -*-
import sys
sys.path.append("..")
from page_obj.customer.CCustomer.index import IndexPage
from test_case.base_case import BaseCase
import unittest
from util.decorator import level


class TestCcustomerIndex(BaseCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestCcustomerIndex, cls).setUpClass()
        cls.page = IndexPage(cls.driver)
        cls.page.load()
    
    def test_search_exist_customer(self):
        """
        pre-condition: 18010181267 customer exists
        no cleaning need
        """
        phone = '18010181267'
        self.page.search_phone(phone)
        # assert page_obj value and search value
        customer_phone = self.page.get_input_value('会员电话：')
        self.assertEqual(customer_phone, phone)

    @level(2)
    def test_search_not_exist_customer(self):
        """
            pre-condition: 18010181261 customer not exists
            no cleaning need
        """
        phone = '18010181261'
        self.page.search_phone(phone)
        customer_phone = self.page.get_input_value('会员电话：')
        self.assertFalse(customer_phone)

if __name__ == '__main__':  
    unittest.main(verbosity=2)

```
## 项目结构
* conf--配置文件目录
* driver---浏览器驱动目录
* page_obj---页面对象目录，包含各个模块
* report---报告目录，包含log/snapshot
* support---环境及项目需要的软件
* test_case---测试用例，分模块
* tools---一些工具，包含自动生成所有页面对象
* util---公共方法库
    browser.py---封装浏览器驱动
    config.py---解析conf/default.conf项目配置文件
    data_file_parser.py---解析各种数据文件，支持Json/Config/XML/Excel/CSV
    db.py---连接数据，查询数据
    decorator.py---装饰器，包含显示执行时间，超时，多线程等装饰器
    HTMLTestRunner.py---python2.*英文版报告生成包
    HTMLTestRunnerCN.py---python3.*中文版报告生成包
    log.py---log控制
    root.py---项目一些常量，包含解析项目绝对目录
    selenium_easy.py---基于xpath封装了许多页面元素定位及操作方法
