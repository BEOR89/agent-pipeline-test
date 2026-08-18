import pytest
from app import add, multiply, divide, power, square, cube

def test_add():
    assert add(2, 3) == 5

def test_multiply_positive_integers():
    assert multiply(4, 3) == 12

def test_multiply_negative_and_positive_integers():
    assert multiply(-2, 5) == -10

def test_multiply_float_and_integer():
    assert multiply(2.5, 4) == 10.0

def test_divide():
    assert divide(8, 2) == 4
    assert divide(5, 2) == 2.5
    assert divide(-9, 3) == -3
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 3) == -8

def test_square():
    assert square(4) == 16
    assert square(-3) == 9
    assert square(0) == 0

def test_cube():
    assert cube(2) == 8
    assert cube(-3) == -27
    assert cube(0) == 0
