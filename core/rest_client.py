import requests
from utils.read import base_data
api_root_url = base_data.read_ini()['host']['api_sit_url']


# 获取api_util文件传入
# 返回对应的get地址和响应结果

def get(url, params, **kwargs):
    return requests.get(api_root_url + url, params=params, **kwargs)