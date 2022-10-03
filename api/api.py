import json
from core import api_util
#传入入参参数
# 获取到响应结果
def mobile_query(params):
    response = api_util.get_mobile_belong(params=params)
    return response.json()

