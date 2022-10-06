# -*- coding: utf-8 -*-
# author: 华测-长风老师

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# WebDriverWait  一般用继承来封装

class Wait(WebDriverWait):
    def __init__(self, driver, timeout):
        super(Wait, self).__init__(driver, timeout)


def text_in_title(text):
    return EC.title_contains(text)


def element_be_display(locator):
    by, value = locator
    print(f"时间 定位元素-> by=[{by}] value=[{value}]")
    return EC.visibility_of_element_located(locator)


def any_elements_be_display(locator):
    by, value = locator
    print(f"时间 定位元素-> by=[{by}] value=[{value}]")
    return EC.visibility_of_any_elements_located(locator)


def all_elements_be_display(locator):
    by, value = locator
    print(f"时间 定位元素-> by=[{by}] value=[{value}]")
    return EC.visibility_of_all_elements_located(locator)


def exist_element(locator):
    by, value = locator
    print(f"时间 定位元素-> by=[{by}] value=[{value}]")
    return EC.presence_of_element_located(locator)


def exist_elements(locator):
    by, value = locator
    print(f"时间 定位元素-> by=[{by}] value=[{value}]")
    return EC.presence_of_all_elements_located(locator)


def element_not_display(locator):
    by, value = locator
    print(f"时间 定位元素-> by=[{by}] value=[{value}]")
    return EC.invisibility_of_element_located(locator)


def any_elements_display(locator):
    by, value = locator
    print(f"时间 定位元素-> by=[{by}] value=[{value}]")
    return EC.visibility_of_any_elements_located(locator)


if __name__ == '__main__':
    Wait(driver="", timeout=10).until(exist_elements(locator=""))
    Wait(driver="", timeout=10).until_not(exist_element(locator=""))
