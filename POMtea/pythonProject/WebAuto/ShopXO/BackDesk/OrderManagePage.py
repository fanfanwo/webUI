# -*- coding: utf-8 -*-
# author: 华测-长风老师
import time
from random import choice
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from WebAuto.Browser.browser.Wait import *
from WebAuto.POM.create_pom import create_data
from WebAuto.Browser.browser.browser import BrowserOperate


@create_data("/Volumes/huace/Web自动化测试课程/class12/课程代码/pythonProject/data/pom_data/BackDesk/OrderManagePage.json")
class OrderManagePage:
    # iframe = "ifcontent"  # iframe id

    class Button:
        # search = ("css selector", ".am-icon-search")  # 搜索按钮
        # submit_pay = ("css selector", ".submit-pay")  # 支付按钮
        # confirm = ("xpath", '//button[text()="确认"]')  # 确认按钮
        # submit_delivery = ("css selector", '.submit-delivery')  # 交付按钮
        # logistics_companys = ("css selector", ".express-list>li")  # 物流公司
        pass

    class Input:
        # search = ("name", "f0p")  # 搜索输入框
        # Logistics_number = ("name", "express_number")  # 物流单号
        pass

    def __init__(self, driver):
        self.driver = BrowserOperate(driver)

    def switch_to_frame(self):
        """进入frame"""
        self.driver.frame(self.iframe)
        return self

    def search(self, text):
        """搜索"""
        self.driver.find_element(*self.Input.search).send_keys(text)
        self.driver.find_element(*self.Button.search).click()
        return self

    def click_submit_pay(self):
        """点击支付按钮"""
        self.driver.find_element(*self.Button.submit_pay).click()
        return self

    def click_confirm(self):
        """点击确认按钮"""
        time.sleep(1)
        # self.driver.find_elements(*self.Button.confirm).click()
        Wait(self.driver, 10).until(any_elements_be_display(self.Button.confirm))[0].click()
        return self

    def submit_delivery_process(self, logistics_number):
        """
        交付流程
        :param logistics_number: 物流单号
        :return:
        """
        self.driver.find_element(*self.Button.submit_delivery).click()
        choice(self.driver.find_elements(*self.Button.logistics_companys)).click()
        self.driver.find_element(*self.Input.Logistics_number).send_keys(logistics_number)
        self.click_confirm()  # 点击确认
        return self


if __name__ == '__main__':
    print(OrderManagePage.iframe)
