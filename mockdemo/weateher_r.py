from unittest import mock
import demo
import pytest


def test_mock_fun():
    mock_get_sum = mock.patch('demo.get_sum', return_value=20)
    print(demo.get_sum(1, 2))