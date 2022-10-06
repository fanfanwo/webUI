# -*- coding: utf-8 -*-
# author: 华测-长风老师
from WebAuto.POM.create_pom import create_data

from WebAuto.Browser.browser.browser import BrowserOperate
@create_data("/Volumes/huace/Web自动化测试课程/class12/课程代码/pythonProject/data/pom_data/FrontDesk/LoginPage.json")
class LoginPage:
    # url = "http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html"

    class Button:
        # login = ("xpath", '//button[text()="登录"]')  # 登录按钮
        pass

    class Input:
        # username = ("name", "accounts")  # 用户名输入框
        # password = ("name", "pwd")  # 密码输入框
        pass

    def __init__(self, driver):
        self.driver = BrowserOperate(driver)

    def login(self, username, password):
        self.driver.find_element(*self.Input.username).send_keys(username)
        self.driver.find_element(*self.Input.password).send_keys(password)
        self.driver.find_element(*self.Button.login).click()
        return self
