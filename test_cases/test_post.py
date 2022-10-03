import pytest
from api.api import test_json
from utils.read import base_data

def test_post():
    """
    测试post方法；
    地址是：https://jsonp/laceholder.typicode.com
    :return:
    """
    json_data = base_data.read_data()["json_data"]
    result = test_json(json_data)
    assert result['id'] == 101


if __name__ == '__main__':
    pytest.main()