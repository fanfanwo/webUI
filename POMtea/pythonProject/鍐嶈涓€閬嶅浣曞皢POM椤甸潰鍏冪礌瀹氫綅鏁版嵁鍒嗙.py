# -*- coding: utf-8 -*-
# author: 华测-长风老师
import json


# 转化为装饰器的写法
def create(file):
    def wrapper(cls):
        data = open(file, "r", encoding="utf-8").read()
        data = json.loads(data)
        # button = getattr(cls, "Button")
        # input = getattr(cls, "Input")
        #
        # setattr(button)
        # setattr(cls)
        for i in data:
            type_ = i["type"]
            if type_ == "button":
                name = i["name"]
                selector = i["selector"]
                value = i["value"]
                setattr(getattr(cls, "Button"), name, (selector, value))
            if type_ == "input":
                name = i["name"]
                selector = i["selector"]
                value = i["value"]
                setattr(getattr(cls, "Input"), name, (selector, value))
            if type_ == "url":
                value = i["value"]
                setattr(cls, "url", value)
        return cls

    return wrapper


"""
create(file="xxxpage.json")  会得到 wrapper 的引用

装饰器原则：

def a(func):  # func 相当于接受 b 的参数位置
    pass

@a
def b():
    pass

在引用b() 的时候

就相当于 b = a(b)
"""


# @func("文件名")  确定 装饰器 必定会带参数
# @create(file="xxxpage.json")
# @wrapper(func)
@create(file="xxxpage.json")
class XXXPage:
    class Button:
        """点击类型的元素"""
        # name = value ===>  必须是元组（一般选择元素，因为是基础数据，要保障它的不可变性），或者说列表

    class Input:
        """输入类型的元素"""


# 如果这个元素，它是点击类型的元素：
# name = "属性的名称"
# selector = "元素的定位方式"
# value = "元素定位方式的值"
# setattr_value = (selector, value)  # 元素赋值的属性值
# setattr(XXXPage.Button, name, setattr_value)
# print(XXXPage.Button.属性的名称)

"""
底层逻辑
# open_file_data = []  # 不一定是列表可以是其它形式数据，主要取决于读取文件之后的数据类型  # 可迭代数据类型
open_file_data = open("xxxpage.json", "r", encoding="utf-8").read()  # 实例值演示
open_file_data = json.loads(open_file_data)  # 将文件读取的str类型，转化为Python中的可用数据类型
for i in open_file_data:  # 使用i 去遍历这个数据，i得到就是dict
    # i["type"]  # 用于过滤类型的，过滤元素属于什么类型
    # i["selector"]  # 元素的定位方式
    # i["value"]  # 元素的定位值
    # i["name"]  # 元素的命名
    data_type = i["type"]
    if data_type == "button":
        setattr(XXXPage.Button, i["name"], (i["selector"], i["value"]))
        
print(XXXPage.Button.__dict__)
"""

"""
使用装饰器之后，查看被装饰主体的信息
"""

print(XXXPage.__name__)
