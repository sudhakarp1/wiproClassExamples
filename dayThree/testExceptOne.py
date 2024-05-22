'''

'''
import pytest

def fun():
    print('\nStatement #1 in fun()...')
    raise TypeError
    print('\nStatement #2...')


def testExceptionOne():
    with pytest.raises(TypeError):
        print('\n #1. Inside testExceptionOne before calling fun()...')
        fun()
        print('\n #2. Inside testExceptionOne After calling fun()...')
