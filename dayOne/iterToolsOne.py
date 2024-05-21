from itertools import count

myCnt = count(10, 3)
for i in range(5):
    print(next(myCnt), end=' ')
print('\n------------------------------------------')

newCnt = count(1.0, 1.3)
for i in range(5):
    print(round(next(newCnt),1), end=' ')
