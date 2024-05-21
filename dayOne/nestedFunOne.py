'''
    Intro to nesting of functions
'''

def outerFun():
    print('Entering outerFun')
    def innerFun():
        print('Entering Inner function...')
    innerFun() # calling inner fun
    print('Exiting outerFun')

outerFun()
