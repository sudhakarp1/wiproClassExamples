from functools import reduce

def Add(a,b):
    return a + b
ret = reduce(Add, [1,2,3,4,5]) # 
print(f'ret: {ret}')

retOne = reduce(lambda a, b : a + b, [1,2,3,4,5]) # 
print(f'retOne: {retOne}')
