
oneD = [x for x in  range(1,101)]

#twoD = [[i for i in oneD[j:j+10]] for j in range(0, len(oneD),10)]
twoD = [oneD[j:j+10] for j in range(0, len(oneD),10)]

print(oneD)
print(twoD)