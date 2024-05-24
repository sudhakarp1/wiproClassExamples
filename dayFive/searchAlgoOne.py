#[11:58 AM] shivanikatoju6@gmail.com (Unverified)
from random import randint
 
def mySearch (dataList, data):
    pos = 0
    while pos < len(dataList):
        if dataList[pos] == data:
            return pos
        pos += 1
    return -1
 
if __name__ == '__main__':
    lst = [randint(1,100) for _ in range(10)]
    print("The list is: ",lst)
    data = int(input('enter the element to be searched: '))
    print(f'{data} found at index',mySearch(lst, data))