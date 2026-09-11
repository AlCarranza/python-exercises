from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-5) == 25
    assert square(-8) == 64

def test_zero():
    assert square(0) == 0