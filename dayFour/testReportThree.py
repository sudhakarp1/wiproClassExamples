import pytest 
@pytest.mark.parametrize('user, mesg',[
    ('user#1','Statements related to usser#1'),
    ('user#2','Statements related to usser#2'),
    ('user#3','Statements related to usser#3'),
])
def test_sampleOne(user,mesg):    
    print(f'Got from {user} --> mesg: {mesg}')
    assert True
