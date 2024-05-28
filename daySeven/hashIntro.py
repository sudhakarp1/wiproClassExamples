
def myHashingFun(key, maxLen):
    sum = 0
    for i in key:
        sum += ord(i)
    print(f'sum: {sum}',end = ' ')    
    return (sum % maxLen) 

if __name__ == '__main__':
    key = 'Different String'
    res = myHashingFun(key,101)
    print(f'sum: {key} and num below {res}')

    myList = [' '] * 11
    key = 'ABC'
    res = myHashingFun(key,11)
    print(f'sum: {key} and num below {res}')
    myList[res] = key

    key = 'DEFT'
    res = myHashingFun(key,11)
    print(f'sum: {key} and num below {res}')
    myList[res] = key
    #[] --> 100 elements 

    key = 'Everything'
    res = myHashingFun(key,11)
    print(f'sum: {key} and num below {res}')
    if myList[res] == ' ' :
        myList[res] = key
    else:
        myList[res+1] = key

    #[] --> 100 elements

    key = 'Nothing'
    res = myHashingFun(key,11)
    print(f'sum: {key} and num below {res}')
    myList[res] = key
  
    print (f'Mylist: {myList}')

