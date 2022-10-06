# -*- coding: utf-8 -*-
# author: 华测-长风老师


"""
1、登录商城
2、选择任意商品加入购物车
3、使用货到付款方式完成下单操作
4、请前往商城后台：http://shop-xo.hctestedu.com/admin.php 完成对该订单的信息核对（后台的用户名密码皆为:huace_tester）
5、请在后台完成支付的确认，并操作发货
6、选择任意物流平台进行发货
7、请回到商城个人中心-订单管理核对物流信息完成收货，并进行评价操作
"""

# 下面都是POM的部分
import unittest

# 有没有什么办法可以简化？
"""

"""
# from WebAuto.ShopXO import FrontDesk
# from WebAuto.ShopXO.FrontDesk.BuyPage import BuyPage
# from WebAuto.ShopXO.FrontDesk.EvaluationPage import EvaluationPage
# from WebAuto.ShopXO.FrontDesk.GoodsInfoPage import GoodsInfoPage
# from WebAuto.ShopXO.FrontDesk.HomePage import HomePage
# from WebAuto.ShopXO.FrontDesk.LoginPage import LoginPage as FrontLoginPage  # 前台的 login page
# from WebAuto.ShopXO.FrontDesk.OrderPage import OrderPage
# from WebAuto.ShopXO.BackDesk.IndexPage import IndexPage
# from WebAuto.ShopXO.BackDesk.LoginPage import LoginPage as BackLoginPage  # # 后台的 login page
# from WebAuto.ShopXO.BackDesk.OrderManagePage import OrderManagePage
# from WebAuto.ShopXO import BackDesk
from WebAuto import ShopXO
from WebAuto.Browser import Browser
from testcase.ddt import ddt


# data = {"front_username": "test_changfeng", "front_password": "changfeng", "back_username": "huace_tester",
#         "back_password": "huace_tester", "single_number": "物流单号的数据", "evaluation_content": "评论的数据不得少于6个字符"}


@ddt.ddt
class Test(unittest.TestCase):

    # @ddt.unpack
    @ddt.file_data("/Volumes/huace/Web自动化测试课程/class12/课程代码/pythonProject/data/test_data/test_shopping.json")
    def test_001(self, front_username, single_number, evaluation_content, front_password, back_username, back_password):
        """
        数据分离：
        1、分离的数据有类型划分，比如说，测试用例，是用例需要驱动的数据；浏览器对象相关的配置数据，它不属于测试驱动数据，所以不需要使用ddt分离；
        2、实现分离
        """
        # front_username, front_password = "test_changfeng", "changfeng"
        # back_username, back_password = "huace_tester", "huace_tester"
        # single_number = "物流单号的数据"
        # evaluation_content = "评论的数据不得少于6个字符"
        # print(front_username, single_number, evaluation_content, front_password, back_username, back_password)
        driver = Browser.chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        home = ShopXO.Home(driver)  # 实例homepage页面
        home.open_url().click_login()  # 打开商城首页网址，并点击首页登录按钮
        front_login = ShopXO.FrontLogin(driver)  # 前台登录页面实例
        front_login.login(front_username, front_password)  # 登录，页面跳转首页
        home.random_choice_goods()  # 首页随机选择商品

        handles = driver.window_handles  # 随机选择商品会新增窗口（句柄）
        driver.switch_to.window(handles[-1])

        goods_info = ShopXO.GoodsIn(driver)  # 商品详情页实例

        goods_info.random_choice_format().buy_goods()  # 去到 商品详情页 进行随机选择规格，并购买
        buy = ShopXO.Buy(driver)  # 购买页面实例

        buy.cash_on_delivery().click_submit_orders().click_my_orders()  # 购买页面进行货到付款操作，和提订单，然后点击我的订单去到订单页面

        order = ShopXO.FrontOrder(driver)  # 订单页面实例

        order_number = order.get_order_numbers()  # 去到订单页面获取订单号

        # 新增标签页
        driver.switch_to.new_window()  # 新增一个标签页
        back_login = ShopXO.BackLogin(driver)  # 后台登录页面实例
        back_login.open_url().login(back_username, back_password)  # 在新增的标签页进行后台登录页面的打开，并进行登录操作， 登录完之后，页面来到后台初始页

        index = ShopXO.Index(driver)  # 后台初始页实例
        index.click_level1_order_manage().click_level2_order_manage()  # 后台初始页，进行一级目录订单管理的点击，二级订单管理的点击

        order_manage = ShopXO.BackOrder(driver)  # 订单管理页面实例
        order_manage.switch_to_frame().search(order_number).click_submit_pay().click_confirm().submit_delivery_process(
            single_number)  # 订单管理页面，进行了切换frame，通过订单号搜索订单，支付，确认，发货等操作

        # 后台操作完之后，我们要回到前台的订单页面，所以，推理出前台的订单页面的句柄为句柄集合中的下标 1；进行切换句柄
        handles = driver.window_handles
        driver.switch_to.window(handles[1])

        order.search(order_number).confirm_goods().click_comments()  # 订单页面进行，搜索订单，并进行确认收货；进行评价的点击，会打开一个新的窗口

        # 切换新窗口
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        evaluation = ShopXO.Evaluation(driver)  # 评价页面的实例

        evaluation.evaluation(evaluation_content)  # 操作评价的流程




