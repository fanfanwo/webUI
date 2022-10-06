# -*- coding: utf-8 -*-
# author: 华测-长风老师


"""
1、什么是断言
一个可以触发异常的判断语句

判断语句 我们之前学过 if 分支  它不会触发异常

所以断言是另外一个关键字函数:assert
它接受两个默认内容 两个默认内容之间，使用 "," 分割
第一个内容，是判断语句
例如：
a==b # a 等于 b
a>b  # a 大于 b
a in b  # a 存在于 b
a is b  # a 是 b


第二个内容：
发生异常时需要打印的信息---》 msg
"""
# 举例说明
import unittest

# a = "1234567"
# b = "167"
# assert b in a, f"{b}不存于{a} 中"
"""
python有且只有一个断言关键字，其它所有的断言都是由这里封装衍生出来的


所以我们来简单说一下，unittest里面的断言是什么； 不建议使用
"""


class Test(unittest.TestCase):

    def test(self):
        a = 14
        b = 13

        # assert a < b, f"{a} 不小于{b}"
        assert a == b, f"{a} 不等于 {b}"
        # 将断言作为数据看待
        # self.assertEqual(a, b, "ab不相等时打印的内容嘛")
        # self.assertIn() # assert a in b
        # self.assertIs() # # assert a is b
        # self.assertIsNot() # assert a is not b
        # self.assertIsNone() # # assert a is None
        # self.assertIsNotNone() # assert a is not None
        # 企业中用到的用例组织框架，pytest 和 unittest
        # assert  #  pytest 就只有它


"""
ddt 不同的用例执行的结果不同
断言很麻烦；将断言数据化，数据化了就可以分离了

登录成功的断言，和登录失败的断言；
1、提示语句，有没有存不存在，包含与否

"""
