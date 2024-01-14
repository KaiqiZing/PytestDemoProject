import pytest
from unittest.mock import  patch


def test_case1(test_data):
    global global_varibale
    username = test_data["username"]
    assert len(username)>0