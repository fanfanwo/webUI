# -*- coding: utf-8 -*-
# author: 华测-长风老师
from functools import wraps  # python 提供的一个装饰器修复方式


def wrapper(func):
    @wraps(func)  # 将一个对象的基础信息赋予被装饰的对象
    def wrap(*args, **kwargs):
        return func(*args, **kwargs)

    return wrap


@wrapper  # func_ = wrapper(func_)
def func_(a, c, d):
    return "你好"


# func_.__name__

print("func_的name的变化情况：", func_.__name__)
"""
装饰器有两个要求：
1、被装饰的函数的信息不能发生变化
2、不能改动被装饰器的内容（源码）
"""
