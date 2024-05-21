from itertools import product, combinations, permutations


print('\n==================PRODUCT==========================')
myIter = product('XYZ', repeat=2)
for i in myIter:
    print(''.join(i), end=' ')
print('\n=====================COMBINATION============================')
myIterTwo = combinations('XYZ', 2)
for i in myIterTwo:
    print(''.join(i), end=' ')
print('\n====================PERMUTATION========================')

myIterThree = permutations('XYZ', 2)
for i in myIterThree:
    print(''.join(i), end=' ')
print('\n=======================================================')