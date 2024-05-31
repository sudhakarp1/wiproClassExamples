
def LISequence(arr):
    arrLen = len(arr)
    lisTable = [1] * arrLen
    indices = [-1] * arrLen # storing the indexes of previous num

    for i in range(1, arrLen):
        for j in range(0, i):
            if arr[i] > arr[j] and lisTable[i] < lisTable[j] + 1:
                lisTable[i] = lisTable[j]+1
                indices[i] = j
    
    print(f'lis Table : ',*lisTable)
    #return max(lisTable)
    i = lisTable.index(max(lisTable))
    lisArray = []
    while i != -1:
        lisArray.append(arr[i])
        i = indices[i]

    lisArray.reverse()
    print(f'Longest Increasing Subsequence: ',*lisArray)

    return max(lisTable)

if __name__ == '__main__':
    arr = [10,89,22,3,35,68,99,34]
    print(f'{arr}')

    print(f'Length of the LIS: {LISequence(arr)}')