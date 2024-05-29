'''
    Creating a Bad Character Table using dictionary
'''

def BCTable(patt):    
    table = {}
    for i in range(len(patt)):
        table[patt[i]] = i
    
    return table 

if __name__ == '__main__':
    patt = 'ABC'
    res = BCTable(patt)
    print(f'table for {patt} is {res}')

    patt = 'ABCBBCCA'
    res = BCTable(patt)
    print(f'table for {patt} is {res}')
