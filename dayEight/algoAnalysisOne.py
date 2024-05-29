def binSearch(n):
    print(f'for n as {n}', end=':  ')
    cnt = n 
    while cnt > 0:
        print(f'{cnt}', end = ' ')
        cnt //= 2
    print()

if __name__ == '__main__':	
    binSearch(100)
    binSearch(1000)
    binSearch(10000)
        
