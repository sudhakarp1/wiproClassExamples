oneD = [x for x in  range(1,101)]
twoD = []

for j in range(10):
    twoD.append(list())    
    for i in oneD[j*10 : j*10 + 10]:# 0:10, 10:20
        twoD[j].append(i) 


#twoD = [[i for i in oneD[j:j+10]] for j in range(0, len(oneD),10)]

#print(oneD)
print(twoD)