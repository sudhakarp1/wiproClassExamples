from itertools import cycle

myIter = cycle(['one','two','three','four'])

for i in range(10):
    print(next(myIter))