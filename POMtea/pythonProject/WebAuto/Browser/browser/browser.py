# -*- coding: utf-8 -*-
# author: 华测-长风老师
from selenium import webdriver

"""
函数静态装饰器的使用：
class A:
    
    def a(self,open)
        return open
    
    使用静态装饰器可以减少，我们实例类对象的步骤
    @staticmethod 
    def a(open)
        return open
    A.a()  # 使用的时候
    
    
    @property
    def b(self,arg)    如果需要将一个函数转化为一个属性，是不能有参数的
        return
        
"""


class Browser:
    """返回一个浏览的对象"""

    @staticmethod  # 将一个函数变为静态方法
    def chrome(options=None) -> webdriver.Chrome:
        if options:
            d = webdriver.Chrome(options=options)
        else:
            d = webdriver.Chrome()
        return d

    @staticmethod  # 将一个函数变为静态方法
    def ie(options=None) -> webdriver.Ie:
        if options:
            d = webdriver.Ie(options=options)
        else:
            d = webdriver.Ie()
        return d

    @staticmethod  # 将一个函数变为静态方法
    def edge(options=None) -> webdriver.Edge:
        if options:
            d = webdriver.Edge(options=options)
        else:
            d = webdriver.Edge()
        return d

    @staticmethod  # 将一个函数变为静态方法
    def firefox(options=None) -> webdriver.Firefox:
        if options:
            d = webdriver.Firefox(options=options)
        else:
            d = webdriver.Firefox()
        return d


class BrowserOperate:
    """
    浏览器的一些操作，本质上是driver对象的一写操作
    """

    def __init__(self, d):
        self.d = d

    def open(self, url):
        self.d.get(url)
        return self

    def max(self):
        self.d.maximize_window()
        return self

    @property  # 如果不加这个装饰器，我们在调用 handles 的时候： BrowserOperate().handles()
    def handles(self):
        return self.d.window_handles

    def wait(self, timeout):
        self.d.implicitly_wait(timeout)
        return self

    @property
    def __switch__(self):
        return self.d.switch_to

    def frame(self, frame):
        self.__switch__.frame(frame)
        return self

    def window(self, window):
        self.__switch__.window(window)
        return self

    @property
    def __alert__(self):
        return self.__switch__.alert

    def alert_accept(self):
        self.__alert__.accept()
        return self

    def alert_dismiss(self):
        self.__alert__.dismiss()
        return self

    def alert_send_keys(self, content):
        self.__alert__.send_keys(content)
        return self

    def find_element(self, by, value):
        print(f"时间 定位元素-> by=[{by}] value=[{value}]")
        return self.d.find_element(by, value)

    def find_elements(self, by, value):
        print(f"时间 定位元素-> by=[{by}] value=[{value}]")
        return self.d.find_elements(by, value)


if __name__ == '__main__':
    from selenium import webdriver

    driver = Browser.chrome()  # Browser().chrome()
    operate = BrowserOperate(driver)
    operate.open("https://www.baidu.com")
