'''
    Intro to nesting of functions
'''

def outerFun():
    print('Entering outerFun')
    def innerFun():
        print('Entering Inner function...')    
    print('Exiting outerFun')

    return innerFun

res = outerFun()
res()

