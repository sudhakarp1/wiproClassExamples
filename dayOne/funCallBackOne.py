'''
    function callbacks...
'''

def funCaller(fn, name):
    print(f'Before calling -->{name}')
    fn() # calling the function 
    print(f'After calling -->{name} ')
    print('*' * 50)

def fun():
    print('fun() called')

def funOne():
    print('funOne() called')

funCaller(fun, 'fun')
funCaller(funOne,'funOne')
