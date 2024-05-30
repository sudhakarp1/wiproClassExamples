

'''
    global space or main space...
'''

def fun():
    print('1. fun() called') 
    funOne()
    print('2. fun() called')# this statement is not executed

def funOne():
    print('1. funOne() called')
    funTwo()#--> 
    print('2. funOne() called')# this statement is not executed

def funTwo():
    print('1. funTwo() called')
    funThree()#--> 
    print('2. funTwo() called')# this statement is not executed

def funThree():
    print('funThree called')

if __name__ == '__main__':
    fun()    
    