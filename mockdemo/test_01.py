import pytest
from pytest_mock import mocker

# test_example.py

import os
def rm(filename):
    os.remove(filename)

def test_rm(mocker):
    filename = 'test.file'
    mocker.patch('os.remove')
    rm(filename)