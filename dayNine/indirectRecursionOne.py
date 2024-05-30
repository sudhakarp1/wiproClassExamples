

def printEven(num):
    if num <= 10:
        print(f'E : {num}',end=' ')
        printOdd(num+1)

def printOdd(num):
    if num <= 10:
        print(f'O: {num}',end=' ')
        printEven(num+1)

if __name__ == '__main__':
    printEven(0)