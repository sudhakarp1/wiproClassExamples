

def OBSTree(keys, freqs):
    keysLen = len(keys)
    costTable  = [[0] * keysLen for _ in range(keysLen)]
    rootTable  = [[0] * keysLen for _ in range(keysLen)]

    for i in range(keysLen):
        costTable[i][i] = freqs[i]
        rootTable[i][i]  = i

    for length in range(2, keysLen + 1):
        for i in range(keysLen - length + 1):
            j = i + length - 1           
            costTable[i][j] = float('inf')
            #recursivelly try out all possible roots under current sub tree
            for r in range(i, j + 1):
                leftSub = 0 if r == i else costTable[i][r-1]
                righSub = 0 if r == j else costTable[r+1][j]
                totalSum = leftSub  + righSub + sum(freqs[i:j+1])

                if totalSum < costTable[i][j]:
                    costTable[i][j] = totalSum
                    rootTable[i][j] = r 
    
    print('root table')
    for i in rootTable:
        print(*i)

    return costTable, rootTable






def buildTree(keys, root, i, j):
    if i > j:
        return None
    elif i == j:
        return keys[i]
    else:
        rootIndex = root[i][j]
        rootKey = keys[rootIndex]
        leftTree = buildTree(keys, root, i , rootIndex -1)
        rightTree = buildTree(keys, root, rootIndex + 1, j)
        return {'key': rootKey, 'left': leftTree, 'right': rightTree}

if __name__== '__main__':
    keys = [10, 15, 20]
    freq = [70, 50, 30]

    cost, root = OBSTree(keys, freq)
    print(f'Minimum cost: {cost[0][len(keys)-1]}')

    OBST = buildTree(keys, root, 0 , len(keys)-1)
    print(OBST)


