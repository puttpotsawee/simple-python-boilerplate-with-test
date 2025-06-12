import pytest  # Import pytest for testing
from src.my_math import add, subtract, multiply, divide  # Import the functions to be tested

def test_add():
    assert add(2, 3) == 5  # Test case for addition

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5), 
    (0, 0, 0), 
    (-1, 1, 0)
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

def test_subtract():
    assert subtract(5, 3) == 2  # Test case for subtraction

def test_multiply():
    assert multiply(2, 3) == 6  # Test case for multiplication

def test_divide():
    assert divide(6, 3) == 2  # Test case for division
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"