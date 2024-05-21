'''
    function callbacks...
'''

def WrapperFun(fn): #decorator function
    def funCaller():
        print(f'Before calling -->')
        fn() # calling the function 
        print(f'After calling --> ')
        print('*' * 50)
    return funCaller

@WrapperFun
def fun(): #decorated function
    print('fun() called')

@WrapperFun
def funOne():
    print('funOne() called')

fun() # 
funOne()


