
def LCSTable(seq1, seq2):
    seqLenOne,seqLenTwo = len(seq1), len(seq2)

    tbl = [[0] * (seqLenTwo + 1) for _ in range(seqLenOne+1)]
    for i in range(1, seqLenOne+1):
        for j in range(1, seqLenTwo+1):
            if seq1[i-1] == seq2[j-1]:
                tbl[i][j] = tbl[i-1][j-1] + 1
            else:
                tbl[i][j] = max(tbl[i-1][j] , tbl[i][j-1])
    print('table ')
    for i in tbl:
        print(*i)

if __name__ == '__main__':
    str1 = 'XYZABC'
    str2 = 'PQRXRSTA'
    LCSTable(str1, str2)