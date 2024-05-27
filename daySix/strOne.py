
myStr = 'Give in a string'

print(f'myStr: {myStr}')
myList = list(myStr)# method #1
print(f'myList: {myList}')
myListOne = [*myStr] #method #1
print(f'myListOne: {myListOne}')

lst = []
for i in myStr:#method #3
    print(f'{i}', end = ' ')
    lst.append(i) 
print(lst)

myListTwo = [123,'some string', [123,345,456,67]] 
myListTwo.extend([10,20,30]) #method #4
print(f'\nmyListTwo: {myListTwo}')
