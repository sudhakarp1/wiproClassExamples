
def fun(first, second, *args, **kwargs):
    print(f'fun() called')
    print(f'\t\tWith : first: {first} \tsecond:{second}')
    print(f'\t\tWith : args: {args}')
    print(f'\t\tWith : kwargs: {kwargs}')

fun(10,20,30,40,50,'test','rest','best',a=1, b=20, p=30,name='Virat Babu')

#fun(10,20)

'''
myDict = {'a':10, 'b':20, 'fname':'Sudhakar','lname':'Palanivelu','phNo':8923479823}

print(f'#1:  {myDict}')
print(f'#2:  {myDict.keys()}')
print(f'#3:  {myDict.values()}')
print(f'#4:  {myDict.items()}')

def fun(**abc): #key word arguments --> kw args or kwargs
    print(f'fun() called with {abc}') #--> dictionary

fun()
fun(a=1)
fun(fname='Sachin', lname='Tendulkar')



def fun(*args): # variable number of args --> tuple
    print(f'fun() called ... {args}--> ', *args)

fun()
fun(10)    
fun(100,200)
fun(100,200,'test','some more',83645)

def fun(arg):
    print(f'fun() called...{arg}')

fun(10)
fun(['test',93847,'some more',9834.456])

fun((100,200))
'''

