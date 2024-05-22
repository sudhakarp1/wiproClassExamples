import pytest

@pytest.fixture
def setUpTearDown():
    print('\nSetup: ....')
    yield
    print('\nTeardown: ....')


