from math_utils import add, power


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_power():
    assert power(2) == 4
    assert power(3) == 9
    assert power(2, 3) == 8
