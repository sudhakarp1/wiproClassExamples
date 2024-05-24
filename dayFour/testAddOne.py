import pytest

def isNotWindows():
    import os 
    return os.name != 'nt'

@pytest.mark.skip(reason='Just dont want to work with CMD option')
def test_AddOne(request):
    a = int(request.config.getoption('--op1'))
    b = int(request.config.getoption('--op2'))
    expRes =  int(request.config.getoption('--expRes'))
    
    res = a + b
    print(f'Args: {a} + {b} --> {expRes} getting {res}')
    assert res==expRes, f'result of {a} + {b}  is not {expRes}'


def test_Twotimes():
    assert True

