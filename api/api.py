import json
from core.api_util import api_utils
#传入入参参数
# 获取到响应结果
def mobile_query(params):
    response = api_utils.get_mobile_belong(params=params)
    return response.json()


def test_json(json_data):
    """
    测试post方法
    :param json_data:
    :return:
    """
    response = api_utils.post_data(json=json_data)
    return response.json()
