fun = lambda : print('Hello World')
fun()

x = lambda a: a * a 
print(x(5))

fun1 = lambda a, b: a + b
print(fun1(10,20))

def funOne(n):# n is 3
    return lambda num: num ** n # num is 20

sqr = funOne(3) #sqr = lambda num: num ** 3
print(sqr(20))
