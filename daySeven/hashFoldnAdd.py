'''
    Implementing fold and add
'''

def foldAndAdd(string):
    key = string.ljust(10)
    sum = 0
    print('folding: ',end='')
    for i in range(0,10,2):
        fold = ord(key[i])*100 + ord(key[i+1])
        sum += fold 
        print(f'{fold}  ',end='')
    print(f'\t: Sum: {sum}')

if __name__ == '__main__':
    foldAndAdd('ABC')
    foldAndAdd('ABRACADABRA')

