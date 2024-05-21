'''
A simple class Decorator
'''

class Decorator:
    def __init__(self, arg):
        print(f'Here arg is {arg}')
        self.arg = arg #TITLE is passed

    def __call__(self, *args):#call takes fun as argument--> args[0]
        print(f'Arguments passed....{self.arg}')
        def Wrapper(mesg):   # mesg --> Hello how are you            
            args[0](mesg)
        return Wrapper

@Decorator('TITLE') # __init__('title')
def fun(mesg):
    print(f'fun() called with {mesg}')

fun('Hello how are you') 


'''
obj = Decorator('TITLE') # __init__('TITLE)
ret = obj(fun) # obj.__call__(fun) --> return Wrapper here 
ret('Messages here') #wrapper('Messages here')
'''
