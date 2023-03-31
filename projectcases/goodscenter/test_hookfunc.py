import pytest


def test_eval(parameters):
    assert eval(parameters['test_input']) == parameters['expected']

if __name__ == '__main__':
    pytest.main(["-sv", "demo_1.py"])
