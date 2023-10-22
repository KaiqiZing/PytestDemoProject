import allure
import pytest

from api.user_api import send_code, register, login, add_shopping_cart
from projectcases.usercenter.conftest import delete_code, get_code, delete_user, get_shop_cart_num
from utils.read import base_data

"""
全流程测试：
1、先使用随机手机号码进行注册，返回验证码，使用验证码和手机号发送数据，对响应结果和数据库落表的验证码进行一致性校验
2、使用手机号码和密码进行登录，并返回token；
3、通过商品ID获取到数据库中对应商品的库存及其他信息；
4、头部携带token和需要操作的参数；
5、对比返回的状态和库存数与数据库中是否保持一致 即可；
"""
@allure.feature("用户中心模块")
class TestUser:
    @allure.story("用户注册后登录")
    @allure.title("测试用例--注册手机号码")
    def test_register(self):
        json_data = base_data.read_data()['test_register']
        #删除验证码
        delete_code(json_data['mobile'])
        #发送验证码
        result = send_code(json_data)
        assert result.success is True
        # 获取验证码
        mobile = result.body['mobile']
        code = get_code(mobile)
        # 注册账户
        register_result = register(code, mobile)
        assert register_result.success is True
        # 删除用户
        delete_user(mobile)

    @pytest.mark.parametrize("username, password", base_data.read_data()['user_login'])
    @allure.story("用户登录")
    @allure.title("测试用例--用户登录")
    def test_login(self,username, password):
        # 用户登录
        result = login(username, password)
        assert result.success is True
        assert  result.body['token'] is not None


    @pytest.mark.parametrize("username, password", base_data.read_data()['user_login'])
    @allure.story("购物车相关")
    @allure.title("测试用例--购物车添加")
    def test_shopping_cart(self,username, password):
        #添加购物车流程---先登录=添加指定商品id ==添加购物车结果，查询购物车内数据，对比前后结果；
        # 接口登录操作
        result = login(username, password)
        assert result.success is True
        assert result.body['token'] is not None

        # 购物车添加需要用到token
        token = result.body['token']
        # 购物车函数传参
        params = base_data.read_data()['shopping_cart']  # 添加的商品ID
        #购物车添加结果
        result = add_shopping_cart(params, token)
        # 查询购物车内商品数量
        num = get_shop_cart_num(username, params['goods'])
        assert result.success is True
        assert result.body['nums'] == num



        tokens = result.body("token")
        inputParam = base_data.read_data()
        shoopingResult = add_shopping_cart(inputParam, tokens)
        assert shoopingResult.success is True
        shoopingNum = get_shop_cart_num(username, inputParam['goods'])
        assert shoopingResult.body["nums"]  == shoopingNum


