# -*- coding: utf-8 -*-
# author: 华测-长风老师
from WebAuto.POM.create_pom import create_data
from WebAuto.Browser.browser.browser import BrowserOperate


@create_data("/Volumes/huace/Web自动化测试课程/class12/课程代码/pythonProject/data/pom_data/FrontDesk/OrderPage.json")
class OrderPage:
    url = "http://shop-xo.hctestedu.com/index.php?s=/index/order/index.html"

    class Button:
        # order_numbers = ("css selector", ".am-icon-bookmark-o")  # 订单管理按钮
        # confirm_goods = ("css selector", ".submit-ajax.submit-confirm")  # 收货按钮
        # confirm = ("css selector", "[data-am-modal-confirm]")  # 确定按钮
        # search = ("css selector", ".btn-loading-example.am-icon-search")  # 搜索按钮
        # comments = ("xpath", '//span[text()="评论"]')  # 评论按钮
        pass

    class Input:
        # search = ("name", "f0p")  # 搜索输入框
        pass

    def __init__(self, driver):
        self.driver = BrowserOperate(driver)

    def open(self):
        self.driver.open(self.url)
        return self

    def get_order_numbers(self):
        """获取订单"""
        text = self.driver.find_element(*self.Button.order_numbers).text.lstrip()
        return text

    def search(self, text):
        """搜索"""
        self.driver.find_element(*self.Input.search).send_keys(text)
        self.driver.find_element(*self.Button.search).click()
        return self

    def confirm_goods(self):
        """收货"""
        self.driver.find_element(*self.Button.confirm_goods).click()
        self.driver.find_element(*self.Button.confirm).click()
        return self

    def click_comments(self):
        """点击评论"""
        self.driver.find_element(*self.Button.comments).click()
        return self
