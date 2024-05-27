'''
1. start from mid(col) and top(row)							
2. if curr pos is top row --> go to bottom row + 1 col							
3. if right most column --> got first colum - 1 row							
4. if right top diagonal is free --> fill it							
5. no other options ==> go 1 row down		
row --> m-->	5
first --> f	-->1
last  --> l-->	f + m * m - 1
sum --> s -->	(f+l) / 2 * m
'''

row , first, = 3,1
last = first + row * row  - 1
rowSum =(first + last)//2 * row 
#null matrix of row * row 
mat = []
for _ in range(row):
    mat.append([0] * row)

rCnt, cCnt = 0, row//2 # 1 point
while first <= last:
    mat[rCnt][cCnt] = first
    if rCnt == 0 and cCnt != row - 1: # second point
       rCnt, cCnt = row-1, cCnt + 1 
    elif cCnt == row - 1 and rCnt != 0: # third Point
       rCnt, cCnt = rCnt - 1, 0 
    elif cCnt != row - 1 and rCnt != 0 and mat[rCnt-1][cCnt+1] == 0: #fourth
        rCnt, cCnt = rCnt - 1 , cCnt + 1
    else: # fifth point
        rCnt = rCnt + 1
    first += 1

print(mat)

