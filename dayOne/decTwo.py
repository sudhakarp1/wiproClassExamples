'''
    function callbacks...
'''

def WrapperFun(fn):
    def funCaller():
        print(f'Before calling -->')
        fn() # calling the function 
        print(f'After calling --> ')
        print('*' * 50)
    return funCaller

def fun():
    print('fun() called')

def funOne():
    print('funOne() called')

funCaller = WrapperFun(fun)
funCaller()

funCaller = WrapperFun(funOne)
funCaller()


