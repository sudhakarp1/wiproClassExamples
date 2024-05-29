
def setBitCount(num):
    count = 0
    while num > 0:
        if num & 1 == 1:
            count+=1    
        num >>= 1
    return count

if __name__ == '__main__':
    res = setBitCount(10)
    print(f'count: 10 --> {res}')
    res = setBitCount(1000)
    print(f'count: 1000 --> {res}')

    res = setBitCount(127)
    print(f'count: 127 --> {res}')