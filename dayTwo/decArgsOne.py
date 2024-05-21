
def Header(title): #argument to your decorator
    def wrapper(fun): #fun as argument ...function callback
        def inner(args): #fun() is called with args passed
            print(title.center(60,'*'))
            fun(args)
        return inner
    return wrapper

@Header('TITLE') #
def fun(args = None):
    print(f'fun() called ... with {args}')

fun(123)

'''
ret = Header('Title') # return wrapper
wrapRet = ret(fun) # passing fun() and returning inner
wrapRet(123) #==> inner(123) --> print-->fun(123)
'''






