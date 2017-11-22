from selenium.webdriver.common.by import By
from page_obj.base_page import BasePage
from util.config import Config
from util.browser import Chrome


class LoginPage(BasePage):
    uri = 'index/index/login'
    
    # element location
    input_username_loc = (By.ID, 'nickname')
    input_password_loc = (By.ID, 'password')
    btnLogin_loc = (By.ID, 'login')
    
    # data
    username = Config.option('env', 'username')
    password = Config.option('env', 'password')
    
    def login_as(self, username, password):
        login_url = self.base_url + self.uri
        self.open(login_url)
        self.sleep()
        self.type(self.input_username_loc, username)
        self.type(self.input_password_loc, password)
        self.click(self.btnLogin_loc)
        self.sleep()
    
    def login(self):
        self.login_as(self.username, self.password)
        

if __name__ == '__main__':
    d = Chrome.normal()
    # d = Chrome.headless()
    p = LoginPage(d)
    p.login()
    p.sleep()
    d.quit()