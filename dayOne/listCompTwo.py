#myList = [var * 2 for var in range(0,100,5) if var % 10 == 0]
myList = [var  for var in range(0,100,5)]
newList = [var *2  for var in myList]

print(myList)
print(newList)
