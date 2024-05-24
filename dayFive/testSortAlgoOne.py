import sortAlgoOne as sa
 
def test_mySortOne():
    assert sa.mySort([6,4,2,9,1,8]) == [1,2,4,6,8,9]
    assert sa.mySort([6,55,204,8,36]) == [6,8,36,55,204]
    assert sa.mySort([0,1000,8]) == [0,8,1000]
    assert sa.mySort([661,1999,2024,56]) == [56,661,1999,2024]

def test_mySortTwo():
    myList = [6,4,2,9,1,8]
    assert sa.mySort(myList) == [1,2,4,6,8,9]
    assert myList[0] < myList[1]
    assert myList[1] < myList[2]
    assert myList[0] < myList[len(myList)-1]
