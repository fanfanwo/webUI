# -*- coding: utf-8 -*-
# author: 华测-长风老师
from WebAuto.POM.create_pom import create_data
from WebAuto.Browser.browser.browser import BrowserOperate


@create_data("/Volumes/huace/Web自动化测试课程/class12/课程代码/pythonProject/data/pom_data/FrontDesk/BuyPage.json")
class BuyPage:
    class Button:
        # buying_patterns = ("css selector", '.payment-list>li')  # 付款方式
        # submit_orders = ("css selector", ".btn-go.btn-loading-example")  # 提交订单按钮
        # my_orders = ("css selector", ".am-btn.am-btn-primary.am-radius")  # 我的订单按钮
        pass

    class Input:
        pass

    def __init__(self, driver):
        self.driver = BrowserOperate(driver)

    def choice_buying_patterns(self, value):
        """
        选择付款方式
        :param value: 0---》支付宝；1---》微信；2--->货到付款
        :return:
        """
        # 有N种方式确定我们使用什么付款方式

        # 方式一
        self.driver.find_elements(*self.Button.buying_patterns)[value].click()

        # # 方式二：
        # ele_s = self.driver.find_elements(*self.Button.buying_patterns)
        # for i in ele_s:
        #     if i.find_element("tag name", "span").text == value:
        #         i.click()

        return self

    def cash_on_delivery(self):
        """选择付款方式为货到付款"""
        return self.choice_buying_patterns(2)

    def click_submit_orders(self):
        """点击提交订单"""
        self.driver.find_element(*self.Button.submit_orders).click()
        return self

    def click_my_orders(self):
        """点击我的订单按钮"""
        self.driver.find_element(*self.Button.my_orders).click()
        return self
