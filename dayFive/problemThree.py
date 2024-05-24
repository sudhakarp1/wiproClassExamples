'''
    Dealing with array of numbers ...
'''
#part I
def createFillArray(firstNum):
    myList = [firstNum + i for i in range(100)]    
    return myList

def isPrime(num):
    primeFlag = True
    for i in range(2,num):
        if num % i == 0:
            primeFlag = False
            break
    return primeFlag

#part II
def processArray(arr):
    for i in range(len(arr)):
        if isPrime(arr[i]) is False:
            arr[i] = 0

#part III
def countMaxZeroes(arr):
    zeroCnt = 0
    coll= []
    maxZeroes,first,last=0,None, None
    for i in range(len(arr)):
        if arr[i] == 0:
            zeroCnt+=1
        else:            
            if zeroCnt > maxZeroes:
                maxZeroes = zeroCnt
                last = arr[i] 
                first = i - maxZeroes - 1 
                if first < 0:
                    first = None
                else:
                    first = arr[first] 
            zeroCnt = 0 
    print(f'{maxZeroes} of zereos between {first} and {last}')
    print(f'coll: {coll}')
    return maxZeroes,first,last

if __name__ == '__main__':
    firstNum = int(input('Enter the first num: '))
    myList = createFillArray(firstNum)
    print(f'len: {len(myList)}: {myList}')
    processArray(myList)
    print(f'len: {len(myList)}: {myList}')

    res = countMaxZeroes(myList)
    print(f'final Result: {res}')

    