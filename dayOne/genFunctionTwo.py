
def genFun():
    #print('one')
    yield 1
    #print('two')
    yield 2
    #print('three')
    yield 3

resGen = genFun()

for i in resGen:
    print(i, end = ' ')

'''
print(next(resGen))
print(next(resGen))
print(next(resGen))
print(next(resGen))
'''

