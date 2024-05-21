'''
    function callbacks...
'''

def WrapperFun(fn):
    def funCaller(name):
        print(f'Before calling -->{name}')
        fn() # calling the function 
        print(f'After calling -->{name} ')
        print('*' * 50)
    return funCaller

def fun():
    print('fun() called')

def funOne():
    print('funOne() called')

funCaller = WrapperFun(fun)
funCaller('fun')

funCaller = WrapperFun(funOne)
funCaller('funOne')


