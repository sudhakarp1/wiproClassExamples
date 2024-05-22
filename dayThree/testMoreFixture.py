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

def testAddition(a, b, expectedRes):
    res = a + b
    assert res == expectedRes


