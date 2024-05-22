import pytest

@pytest.fixture
def a():
    return 10

@pytest.fixture
def b():
    return 20

@pytest.fixture
def expectedRes():
    return 10 + 20

@pytest.mark.parametrize("a,b,expectedRes", [
    (100,200, 300),
    (11,22, 33),
    (100, -50, 50),
    (1, -1, 0),
    (100, -200, -100),
])

def testAddition(a, b, expectedRes):
    res = a + b
    assert res == expectedRes


