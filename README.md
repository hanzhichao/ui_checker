1.安装chrome
```
sudo apt-get install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
```
如果上面运行 
sudo dpkg -i google-chrome*.deb命令之后报错，使用如下命令修复一下： 
sudo apt-get install -f,之后再次运行sudo dpkg -i google-chrome*.deb命令就可以了

安装后确认/usr/bin目录下是否有google-chrome文件

2.安装python、安装Selenium、安装requests(可选)

sudo apt-get install python-pip
sudo pip install selenium
#requests模块，可选安装
sudo pip install requests

3.安装chromedriver

建议安装最新版本的chromedriver，下载页面： 
http://chromedriver.storage.googleapis.com/index.html

在这个页面里列出了chromedriver的各个版本，我们选择目前最新的版本（2.29），使用命令行安装：

wget -N http://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

安装后确认/usr/bin目录下是否有chromedriver文件

由于时效性，在安装时应当先去网站查看最新版本，然后替换命令行中的2.29版本信息
4.简单示例

这时候就可以在图形界面的终端运行python自动化测试脚本了。 
示例脚本，打开网址并截图：

#coding:utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://zhaoyabei.github.io/")
driver.save_screenshot(driver.title+".png")

可以看到chrome启动并加载了网址，桌面生成了截图。 
这里写图片描述


5.字符界面运行

如果想要在字符界面使用Chrome进行测试，需要使用工具Xvfb.

X Virtual Framebuffer（Xvfb）虚拟帧缓冲器,简单来说它可以直接处理 Window的图形化功能，并且不会输出到屏幕上，这就摆脱了对可视窗口的依赖
sudo apt-get -y install xvfb gtk2-engines-pixbuf
sudo apt-get -y install xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable
# 截图功能，可选
sudo apt-get -y install imagemagick x11-apps
Xvfb -ac :99 -screen 0 1280x1024x16 & export DISPLAY=:99

运行测试脚本，输出网页标题：

#coding:utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://github.com/")
print driver.title

# 分层
1. 驱动层： 文件的读取解析，db链接的建立，ssh链接的建立，smtp链接的建立，浏览器驱动
2. 逻辑层： 配置文件的读取，db ORM, client对象，webdriver补充定位方法，及操作方法，邮件功能，报告功能
3. 页面层:  page 原型，page object 和 page element，页面基本操作，登陆，登出
5. 业务层： 基本业务，如下单，申购，开具发票等
6. 用例层： 基于页面层的单测用例和基于业务层的场景用例，包括prepare和clean
7. 控制层： 用例执行控制，并发，多次，多种执行策略
8. web层：  网站Dashboard

其他： 批量生产page object 和 page elment   自动获取 元素 定位方式