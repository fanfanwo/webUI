# -*- coding: utf-8 -*-
# author: 华测-长风老师
from random import choice

from WebAuto.POM.create_pom import create_data
from WebAuto.Browser.browser.browser import BrowserOperate


@create_data("/Volumes/huace/Web自动化测试课程/class12/课程代码/pythonProject/data/pom_data/FrontDesk/GoodsInfoPage.json")
class GoodsInfoPage:
    class Button:
        # format_ul = ("css selector", ".sku-items>ul")  # 规格的ul元素
        # buy = ("css selector", ".buy-btn.buy-submit.buy-event.login-event")  # 购买按钮
        pass

    class Input:
        pass

    def __init__(self, driver):
        self.driver = BrowserOperate(driver)

    def random_choice_format(self):
        """选择商品规格"""
        ele_uls = self.driver.find_elements(*self.Button.format_ul)
        if ele_uls:
            for i in ele_uls:
                ele_lis = i.find_elements("tag name", "li")
                while True:
                    format_ = choice(ele_lis)
                    format_.click()
                    if "selected" in format_.get_attribute("class"):
                        break
        return self

    def buy_goods(self):
        """立即购买"""
        self.driver.find_element(*self.Button.buy).click()
        return self
