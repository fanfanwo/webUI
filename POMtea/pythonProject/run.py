# -*- coding: utf-8 -*-
# author: 华测-长风老师
import unittest

from execute.HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

testcase = unittest.TestLoader().discover(r"testcase/testcases/", "test*.py")

runner = HTMLTestRunner(open("testcase/reports/run_by_html_test_runner.html", "w"), verbosity=2, title="自动化测试用例执行结果",
                        description="运行者长风")  # 报告存放的位置
runner.run(testcase)


