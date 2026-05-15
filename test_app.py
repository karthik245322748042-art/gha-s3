def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_fail():
    assert add(2, 2) == 5  # This will FAIL on purpose so AI explains it
