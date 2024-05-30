#returns the reversed array
def reverseList(arr):
    if len(arr) == 1:
        return arr
    return reverseList(arr[1:]) + [arr[0]]
    
if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    print(f'Before reversing is {arr}')
    res= reverseList(arr)
    print(f'After reversing is {res}')