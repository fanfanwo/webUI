# -*- coding: utf-8 -*-
# author: 华测-长风老师


from .LoginPage import LoginPage as Login
from .OrderPage import OrderPage as Order
from .HomePage import HomePage as Home
from .GoodsInfoPage import GoodsInfoPage as GoodsIn
from .EvaluationPage import EvaluationPage as Evaluation
from .BuyPage import BuyPage as Buy

__all__ = [
    "Login",
    "Order",
    "Home",
    "GoodsIn",
    "Evaluation",
    "Buy",
]
