# -*- coding: utf-8 -*-
# author: 华测-长风老师
from random import choice

from WebAuto.POM.create_pom import create_data
from WebAuto.Browser.browser.browser import BrowserOperate


@create_data("/Volumes/huace/Web自动化测试课程/class12/课程代码/pythonProject/data/pom_data/FrontDesk/HomePage.json")
class HomePage:
    # url = "http://shop-xo.hctestedu.com/"

    class Button:
        # login = ("link text", "登录")  # 登录按钮
        # goods_images = ("class name", "goods-images")  # 商品的图片
        pass

    class Input:
        pass

    def __init__(self, driver):
        self.driver = BrowserOperate(driver)

    def open_url(self):
        """打开首页网址"""
        self.driver.open(self.url)
        return self

    def click_login(self):
        """点击首页的登录"""
        self.driver.find_element(*self.Button.login).click()
        return self

    def random_choice_goods(self):
        """随机选择商品"""
        choice(self.driver.find_elements(*self.Button.goods_images)).click()
        return self
