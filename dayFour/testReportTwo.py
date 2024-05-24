import pytest 

@pytest.fixture(params=[
    ('user#1','Statements related to usser#1'),
    ('user#2','Statements related to usser#2'),
    ('user#3','Statements related to usser#3'),
])
def getData(request):
    return request.param

def test_sampleOne(getData):
    user,mesg=getData
    print(f'Got from {user} --> mesg: {mesg}')
    assert True
