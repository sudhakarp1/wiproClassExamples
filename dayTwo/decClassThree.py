'''
A simple class Decorator
'''

class Decorator:
    def __init__(self, fun):
        self.func = fun 

    def __call__(self, mesg):
        print(f'----------------call method ------------------')
        self.func(mesg)
        print('***********************************************')

@Decorator
def fun(mesg):
    print(f'fun() called with {mesg}')

fun('Hello how are you') 