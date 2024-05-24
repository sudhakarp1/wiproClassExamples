myNums = [93,82,86,28,18,47,65]

print(f'List: {len(myNums)} : {myNums}')

for i in range(len(myNums)):
    print(f'{myNums[i]}', end =' ' ) #accessing elements
print()

myNums.insert(3,1000) # inserting after 3 position
myNums.insert(7,500)# inserting after 7 position
print(f'List: {len(myNums)} : {myNums}')

var = myNums.pop()
print(f'var: {var} popped from myNums')
var = myNums.pop() # last element 
print(f'var: {var} popped from myNums')
print(f'List: {len(myNums)} : {myNums}')
myNums.remove(28)
print(f'List: {len(myNums)} : {myNums}')
del myNums[5]
print(f'List: {len(myNums)} : {myNums}')
myNums[3] = 2000
print(f'List: {len(myNums)} : {myNums}')