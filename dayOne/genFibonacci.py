def fiboGen():
    a, b = 0,1
    while True:
        yield a 
        a, b = b, a + b

fiboSeries = fiboGen()

for i in range(10):
    print(next(fiboSeries), end = ' ')
    
'''
cnt = 0
for i in fiboSeries:
    print(f'{cnt} --> {i}')
    cnt += 1
    if cnt > 10:
        break
    
'''