import pytest

def test_AddOne():
    assert True

@pytest.mark.xfail(True,reason='Expecting Failure')
def test_Twotimes():
    assert False

