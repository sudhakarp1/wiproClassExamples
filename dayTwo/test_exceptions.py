
def myFun():
    print('myFun() called... ')
    raise SystemExit(1)
    print('This statement never executes')

import pytest
def test_myfun():
    with pytest.raises(SystemExit):
        myFun()


