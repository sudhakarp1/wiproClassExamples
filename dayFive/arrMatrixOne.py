#[3:17 PM] satish.kumar17@siesgst.ac.in (Unverified)

def createMatrix(row,col, first):
    li = []
    for i in range(row):
        l = []
        for j in range(col):
            l.append(first)
            first += 1
        li.append(l)
    
    return li
    
if __name__ == '__main__':
    row, col, first = map(int, input('Enter row,col,first number: ').split(','))
    listMat = createMatrix(row, col, first)
    print(f'listMat:\n{listMat}')

