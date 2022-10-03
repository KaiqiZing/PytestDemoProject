import pytest
import requests
from api.api import mobile_query
from utils.read import base_data

#注意项目最开始使用的是result['status'] 返回的是字典数据不是body数据
# 项目最开始的Pytest.ini 文件的adopts地址是没有配置的


def test_mobile():
    param = base_data.read_data()["mobile_belong"]
    result = mobile_query(param)
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "浙江"
    assert result['result']["city"] == "杭州"
    assert result['result']["company"] == "中国移动"
    assert result['result']["cardtype"] is None
    assert result['result']["areacode"] == "0571"

if __name__ == '__main__':
    pytest.main()


# url = "https://api.binstd.com"
# def test_mobile():
#     param = base_data.read_data()["mobile_belong"]
#     print("测试手机归属地get请求")
#     r = requests.get(url + '/shouji/query',
#                      params={"shouji": param['shouji'], "appkey": param['appkey']})
#     print(r.status_code)
#     assert r.status_code == 200
#     result = r.json()
#     assert result['status'] == 0
#     assert result['msg'] == "ok"
#     assert result['result']["shouji"] == "13456755448"
#     assert result['result']["province"] == "浙江"
#     assert result['result']["city"] == "杭州"
#     assert result['result']["company"] == "中国移动"
#     assert result['result']["cardtype"] is None
#     assert result['result']["areacode"] == "0571"
#
#
# if __name__ == '__main__':
#     pytest.main()
