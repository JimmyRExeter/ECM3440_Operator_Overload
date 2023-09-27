from rational import Rational


def test_add():
    v1 = Rational(1, 2)
    v2 = Rational(1, 4)
    assert (v1 + v2) == Rational(3, 4)


"""def test_subtract():
    v1 = Rational(3, 4)
    v2 = Rational(1, 2)
    assert (v1 - v2) == Rational(1, 4)
"""


def test_str():
    v1 = Rational(1, 2)
    # assert str(v1) == "1/2"
    assert str(v1) == "1.0/2.0"


def test_integer():
    v1 = Rational(4, 2)
    # assert v1 == 2
    assert v1 == Rational(2, 1)


def test_add_integer():
    v1 = Rational(1, 2)
    # v2 = 1
    v2 = Rational(1, 1)
    assert (v1 + v2) == Rational(3, 2)
