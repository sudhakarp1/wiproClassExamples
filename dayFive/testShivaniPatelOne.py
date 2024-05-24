#[11:15 AM] shivanipatel8282@gmail.com (Unverified)
import sortAlgoOne as sa
 
def test_mySort():
    assert sa.mySort([6,4,2,9,1,8]) == [1,2,4,6,8,9]
    assert sa.mySort([6,55,204,8,36]) == [6,8,36,55,204]
    assert sa.mySort([0,1000,8]) == [0,8,1000]
    assert sa.mySort([661,1999,2024,56]) == [56,661,1999,2024]
 
 
#[11:18 AM] shivanipatel8282@gmail.com (Unverified)
import random
 
def mySort(dataList):
    for i in range(len(dataList)):
        for j in range(i+1, len(dataList)):
            if dataList[i] > dataList[j]:
                 dataList[i], dataList[j] =dataList[j],dataList[i]
    return dataList
 
 
if __name__ == '__main__':
    dataList = [random.randint(1, 100) for _ in range(10)]
    print(f"Before Sorting : {dataList}")
    b=mySort(dataList)
    print(f"After Sorting: {b}")
