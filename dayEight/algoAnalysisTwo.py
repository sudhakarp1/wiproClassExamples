def testOne(n):	
	for i in range(n): #n 
		for j in range(n): # log n 
			pass

myRes = {0:0,1:1} #memoization
def fibo(n):
	if n not in myRes:
		myRes[n] = fibo(n-1) + fibo(n-2)		
	return myRes[n] 
	

def fiboCaller(n):	
	for i in range(n): #n 
		print(f'{i+1} --> {fibo(i)}')


if __name__ == '__main__':
    from sys import argv
    from time import perf_counter
    start = perf_counter()
    fiboCaller(int(argv[1]))
    end = perf_counter()
    print(f'time taken :{round(end-start, 3)}secs ')
    
    