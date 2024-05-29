
def minValue(arr):
    # you can write your own logic here 
    return min(arr)


def maxValue(arr):
    # you can write your own logic here 
    return max(arr)

def totalSum(arr):
    return sum(arr)

if __name__ == '__main__':
    lst = [10,29,30,40,50,60,3]
    print(f'min: {minValue(lst)}')
    print(f'max: {maxValue(lst)}')
    print(f'total: {totalSum(lst)}')
