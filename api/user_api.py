from core.api_util import api_utils
from utils.response_util import process_response


def send_code(json_data):
    """

    :param json_data:
    :return:
    """
    response = api_utils.get_code(json=json_data)
    return process_response(response)


def register(code, mobile):
    """
    注册接口
    :param code:
    :param mobile:
    :return:
    """

    json_data = {
        "code": str(code),
        "password": "123456",
        "username": str(mobile)
    }

    response = api_utils.register_mobile(json=json_data)
    return process_response(response)


def login(username, password):
    """
    用户登录接口
    :param username:
    :param passsword:
    :return:
    """
    json_data = {
        "username": username, "password": password
    }

    response = api_utils.user_login(json=json_data)
    return process_response(response)

def add_shopping_cart(params, token):
    """
    购物车添加
    :param username:
    :param passsword:
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_utils.shopping_add(json=params, headers=headers)
    return process_response(response)

