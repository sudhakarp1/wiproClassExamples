'''
    What is recursion...
        a function calling itself is called recursive function
'''

def recur(num):
    if num <= 5:
        print(f'{num}', end=' ')
        recur(num+1)
        print(f'{num}', end=' ')

if __name__ =='__main__':
    recur(1)
    print('\n************************')
