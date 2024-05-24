import pytest

def test_CMDLineArgs(request):
    test_one = request.config.getoption("--test_one")
    print(f'option --test_one passed with {test_one}')
