#inplace reversing
def reverseList(arr,first, last):
    if first >= len(arr) // 2:
        return
    arr[first], arr[last] =  arr[last], arr[first]   
    reverseList(arr, first + 1, last -1)

if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    print(f'Before reversing is {arr}')
    reverseList(arr,0, len(arr)-1)
    print(f'After reversing is {arr}')