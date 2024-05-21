
def CondCheck(num):
    if num % 2 != 0:
        return True
    return False

ret = filter(CondCheck, [1,2,3,4,5]) # 
print(f'ret: {ret}')
print(list(ret))

retOne = filter(lambda a : True if a % 2 == 0 else False, [1,2,3,4,5]) # 
print(f'retOne: {retOne}')
print(list(retOne))