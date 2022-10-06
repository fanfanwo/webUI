# -*- coding: utf-8 -*-
# author: 华测-长风老师
from .BackDesk import *
from .BackDesk import Login as BackLogin
from .FrontDesk import Login as FrontLogin
from .BackDesk import Order as BackOrder
from .FrontDesk import Order as FrontOrder
from .FrontDesk import *

__all__ = [
    "BackLogin",
    "Index",
    "Order",
    "FrontLogin",
    "Order",
    "Home",
    "GoodsIn",
    "Evaluation",
    "Buy",
]  # 声明 这个初始包数据里面，有且只有这些对象
