
def Header(fun):
    def wrapper(args=None):
        print('HEADER'.center(60,'*'))
        fun(args)
    return wrapper

@Header
def fun(args = None):
    print(f'fun() called ... with {args}')

fun()

'''
var = Header(fun) # returns wrapper
var(834) # wrapper(834) ---> printing the header --> fun(834)
'''

