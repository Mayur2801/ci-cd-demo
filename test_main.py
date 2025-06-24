# test_main.py

import pytest
from main import add, subtract, multiply, divide


def test_add():
    assert add(2, 3 , 3) == 8


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
