import pytest

global_variable = "global_value"

@pytest.fixture(scope="module")
def test_data():
    data = {
        "username":"test_user",
        "password":"test_password"

    }
    return data


