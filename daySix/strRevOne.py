
def myStrRevOne(myStr):
    myList = [*myStr]
    myList.reverse()
    return ''.join(myList)

def myStrRevTwo(myStr):
    return myStr[::-1]

def myStrRevThree(myStr):
    myList = [*myStr]
    strLen = len(myStr)
    for i in range(strLen//2):
        myList[i], myList[strLen-i-1] = myList[strLen-i-1],myList[i]
    return ''.join(myList)

if __name__ == '__main__':
    mystr1 = 'Hello'
    mystr2 = 'World'
    mystr3 = 'pots & pans'

    res = myStrRevOne(mystr1)
    print(f'Rev: {mystr1} --> {res}')

    res = myStrRevOne(mystr2)
    print(f'Rev: {mystr2} --> {res}')

    res = myStrRevOne(mystr3)
    print(f'Rev: {mystr3} --> {res}')