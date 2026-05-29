import pytest
from app import add, divide

def test_add_success():
    assert add(3, 5) == 8

def test_divide_success():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)