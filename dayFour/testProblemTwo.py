from problemTwo import sortedList
import pytest

'''
 myList = [(9,'Hello'),(67, 'aaai'),(55,'byeee'),(33,'Bhaiii'),(65,'Haiii')]
    print(f'myList: {myList}')
    newList = sortedList(myList)
    print(f'myList: {myList}--> {newList}')
    newList = sortedList(myList, False)
    print(f'myList: {myList}--> {newList}')
'''

@pytest.fixture
def listData():
    return [(9,'Hello'),(67, 'aaai'),(55,'byeee'),(33,'Bhaiii'),(65,'Haiii')]

def testEmptyList():
    lst = []
    newLst = sortedList(lst)    
    assert lst == newLst

def testSortFirst(listData):
    newList = sortedList(listData)

    assert listData[0] == (9,'Hello')
    assert newList[0][0] == 9
    assert newList[len(newList)-1][0] == 67



