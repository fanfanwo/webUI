# -*- coding: utf-8 -*-
# author: 华测-长风老师

"""
为元素定位添加日志   --？ 还记的吗？

那时候我们为什么要重新添加一个Find类来收集日志呢？ ---牵扯到一点---》最小颗粒度
"""

"""
程序无非就是两个东西：
1、过程 需要添加信息抓取，需要在函数或被调用，被执行时才能触发
2、数据 需要添加信息抓取，需要在数据被使用之前；
"""
"""
比如说： 
find_element 是以 元素的定位方式和定位值 为根本依据；它是抓数据的

如果不改变源码，我们要做的就是重新构建一个 引用 数据执行的方式（拦截数据）
然后将你整个项目里面用到的find_element/s   都替换为 我们新建的方式

"""