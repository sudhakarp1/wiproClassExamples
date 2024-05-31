
def LCSTable(seq1, seq2):
    seqLenOne,seqLenTwo = len(seq1), len(seq2)

    tbl = [[0] * (seqLenTwo + 1) for _ in range(seqLenOne+1)]
    for i in range(1, seqLenOne+1):
        for j in range(1, seqLenTwo+1):
            if seq1[i-1] == seq2[j-1]:
                tbl[i][j] = tbl[i-1][j-1] + 1
            else:
                tbl[i][j] = max(tbl[i-1][j] , tbl[i][j-1])
    return tbl  #tbl[seqLenOne][seqLenTwo]

def findLCS(str1, str2):
    tbl = LCSTable(str1, str2)
    lcs = []
    i,j = len(str1), len(str2)
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i,j = i-1, j-1
        elif tbl[i-1][j] > tbl[i][j-1]:
            i-=1
        else:
            j-=1

    return ''.join(reversed(lcs))

if __name__ == '__main__':
    str1 = 'SOMEMORESEQUENCE'
    str2 = 'MORESEQUENCE'
    res = findLCS(str2, str1)
    print(f'{str1} & {str2} --> {res}')