
from calculator import add, subtract, multiply


def test_add():
    assert add(5, 3) == 9


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(5, 3) == 15
