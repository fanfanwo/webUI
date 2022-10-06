# -*- coding: utf-8 -*-
# author: 华测-长风老师
from WebAuto.POM.create_pom import create_data
from WebAuto.Browser.browser.browser import BrowserOperate

"""
使用数据分离的思想：将数据变为磁盘数据进行保存
"""


@create_data("/Volumes/huace/Web自动化测试课程/class12/课程代码/pythonProject/data/pom_data/BackDesk/IndexPage.json")
class IndexPage:
    class Button:
        pass
        # order_manages = ("xpath", '//span[text()="订单管理"]')  # 订单管理按钮
        # 分析 order_manages = 定位方式+定位的值 ； 隐性的分类

    class Input:
        pass

    def __init__(self, driver):
        self.driver = BrowserOperate(driver)

    def click_level1_order_manage(self):
        """一级目录的订单管理"""
        self.driver.find_elements(*self.Button.order_manages)[0].click()
        return self

    def click_level2_order_manage(self):
        """二级目录的订单管理"""
        self.driver.find_elements(*self.Button.order_manages)[1].click()
        return self
