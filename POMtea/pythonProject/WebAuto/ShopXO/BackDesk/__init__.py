# -*- coding: utf-8 -*-
# author: 华测-长风老师

from .LoginPage import LoginPage as Login
from .IndexPage import IndexPage as Index
from .OrderManagePage import OrderManagePage as Order

__all__ = [
    "Login",
    "Index",
    "Order"
]  # 声明 这个初始包数据里面，有且只有这些对象
