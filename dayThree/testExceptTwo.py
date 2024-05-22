import pytest

class ExceptionGroup(Exception):
    def __init__(self, message, exceptions):
        super().__init__(message)
        self.exceptions = exceptions

def fun():
    print('\nStatement #1 in fun()...')
    raise ExceptionGroup(
        "MY ERROR MESSAGE",
        [
            RuntimeError('RT Error'), 
            TypeError('Type of error'),               
        ],
    )
    print('\nStatement #2...')

def testExceptionOne():
    with pytest.raises(ExceptionGroup) as excinfo:
        print('\n #1. Inside testExceptionOne before calling fun()...')
        fun()
        print('\n #2. Inside testExceptionOne After calling fun()...')
    
        assert  excinfo.group_contains(RuntimeError)
        assert  excinfo.group_contains(TypeError)
        assert  not excinfo.group_contains(SystemExit)
        assert  not excinfo.group_contains(SystemError)
