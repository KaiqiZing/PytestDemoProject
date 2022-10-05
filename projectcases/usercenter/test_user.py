import allure
import pytest

from api.user_api import send_code, register, login, add_shopping_cart
from projectcases.usercenter.conftest import delete_code, get_code, delete_user, get_shop_cart_num
from utils.read import base_data


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
        assert  result.body['token'] is not None

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


