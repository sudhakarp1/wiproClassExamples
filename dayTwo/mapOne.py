def fun(arg):
    #print(f'arg: {arg}', end=' ')
    return arg+101

ret = map(fun, [1,2,3,4,5]) # maping a fun to a list 

print(ret)#printing the map object which is an iterator
for i in ret: #iterating through map object
    print(i) 
