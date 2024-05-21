import myProgram as mp

def test_capitalize():
    assert mp.funCapitalize('some text') == 'SOME TEXT'

def test_reverse():
    assert mp.funReverse('hello') == 'olleh'
    assert mp.funReverse([1,2,3,4]) == [4, 3, 2, 1]

