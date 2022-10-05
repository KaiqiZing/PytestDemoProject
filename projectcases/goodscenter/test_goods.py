import allure
import pytest

from api.goods_api import get_banner
from api.user_api import send_code, register, login
from projectcases.usercenter.conftest import delete_code, get_code, delete_user
from utils.read import base_data


@allure.feature("用户中心模块")
class TestUser:
    @allure.story("首页展示窗口")
    @allure.title("测试用例--首页内容")
    def test_banner(self, banner_num):
        print(banner_num)
        result = get_banner()
        assert result.success is True
        assert len(result.body) == banner_num


