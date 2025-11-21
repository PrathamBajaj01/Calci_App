import pytest
from calci import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(10, 5) == 15

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(4, 5) == 20

def test_positive_integers_only():
    import pytest
    with pytest.raises(ValueError):
        add(-1, 2)
    with pytest.raises(ValueError):
        subtract(3, -5)
    with pytest.raises(ValueError):
        multiply(-2, 3)
