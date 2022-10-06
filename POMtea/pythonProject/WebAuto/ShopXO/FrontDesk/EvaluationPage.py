# -*- coding: utf-8 -*-
# author: 华测-长风老师
from random import choice

from WebAuto.POM.create_pom import create_data
from WebAuto.Browser.browser.browser import BrowserOperate


@create_data("/Volumes/huace/Web自动化测试课程/class12/课程代码/pythonProject/data/pom_data/FrontDesk/EvaluationPage.json")
class EvaluationPage:
    class Button:
        # level = ("css selector", ".rating>li")  # 评价等级
        # submit = ("xpath", '//button[text()="提交"]')  # 提交按钮
        pass

    class Input:
        # content = ("name", "content[]")  # 评价输入框
        pass

    def __init__(self, driver):
        self.driver = BrowserOperate(driver)

    def evaluation(self, text):
        """评论流程"""
        choice(self.driver.find_elements(*self.Button.level)[:5]).click()
        self.driver.find_element(*self.Input.content).send_keys(text)
        self.driver.find_element(*self.Button.submit).click()
        return self
