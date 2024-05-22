import pytest

@pytest.fixture(params=[
    (100,200, 300),
    (11,22, 33),
    (100, -50, 50),
    (1, -1, 0),
    (100, -200, -100),
])
def getData(request): # request is a fixture, using this request you can get 
    return request.param 

def testAddition(getData):
    a,b,expectedRes = getData
    res = a + b
    assert res == expectedRes


