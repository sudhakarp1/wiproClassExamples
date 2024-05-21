'''
    generator functions
'''
def generateNums():
    for i in range(10):
        yield i

print(type(generateNums()))

for var in generateNums():
    print(var, end=' ')

