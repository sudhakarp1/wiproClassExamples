# O(1) --> 
def myHashingFun(key, maxLen):
    sum =  ord(key[0]) * ord(key[1])   #NOT USING a loop --> one statement  
    print(f'sum: {sum}',end = ' ')    
    return (sum % maxLen) 

if __name__ == '__main__':
    key = 'Different String'
    res = myHashingFun(key,101)
    print(f'sum: {key} and num below {res}')

    key = 'ABC'
    res = myHashingFun(key,11)
    print(f'sum: {key} and num below {res}')

    key = 'DEFT'
    res = myHashingFun(key,11)
    print(f'sum: {key} and num below {res}')
    #[] --> 100 elements 

    key = 'SOME'
    res = myHashingFun(key,11)
    print(f'sum: {key} and num below {res}')
    
    key = 'OSBORNE'
    res = myHashingFun(key,11)
    print(f'sum: {key} and num below {res}')