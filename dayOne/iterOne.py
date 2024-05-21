
myList = tuple(range(0,50,5))
myIter = iter(myList)

print(myIter)
for i in range(11):
    print(next(myIter), end=' ')



