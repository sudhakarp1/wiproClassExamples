import pytest

@pytest.fixture
def giveSomeData():
    return 'one'


def testValidData(giveSomeData):
    with pytest.raises(ValueError):
        var = int(giveSomeData)
        assert var == 878668

