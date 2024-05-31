
def LISequence(arr):
    arrLen = len(arr)
    lisTable = [1] * arrLen
    
    for i in range(1, arrLen):
        for j in range(0, i):
            if arr[i] > arr[j] and lisTable[i] < lisTable[j] + 1:
                lisTable[i] = lisTable[j]+1
    
    print(*lisTable)
    return max(lisTable)

if __name__ == '__main__':
    arr = [10,89,22,3,35,68,99,34]
    print(f'{arr}')

    print(f'Length of the LIS: {LISequence(arr)}')