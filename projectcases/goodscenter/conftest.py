import pytest

from utils.mysql_util import db


# @pytest.fixture()
# def banner_num():
#     sql = "select count(1) as banner_num from goods_banner;"
#     result = db.select_db_one(sql)
#     return result['banner_num']
#


"""Define for conftest"""

test_data = [{"test_input": "3+5",
              "expected": 8,
              "id": "验证3+5=8"
              },
             {"test_input": "2+4",
              "expected": 6,
              "id": "验证2+4=6"
              },
             {"test_input": "6 * 9",
              "expected": 54,
              "id": "验证6*9=54"
              }
             ]


def pytest_generate_tests(metafunc):
    ids = []
    if "parameters" in metafunc.fixturenames:
        for data in test_data:
            ids.append(data['id'])  # ids 表示测试用例的编号
        metafunc.parametrize("parameters", test_data, ids=ids, scope="function")  # 用test_data这个列表对parameters进行参数化。