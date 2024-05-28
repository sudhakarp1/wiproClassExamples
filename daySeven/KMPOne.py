

'''
    creating a lps table
    lps table --> Longest proper prefix which is also suffix 
'''
def lpsCreate(pat):
    lps = [0] * len(pat)
    for i in range(1,len(pat)):
        j = lps[i-1]
        while j > 0 and pat[i] != pat[j]:
            j = lps[j-1]
        if pat[i] == pat[j]:
            lps[i] = j+1
    return lps

def myKMPSearch(text, patt):
    lps = lpsCreate(patt)
    ''' The searching logic here'''
    i,j = 0,0 
    indices = []
    while i < len(text):
        if text[i] == patt[j]:
            i,j = i+1, j+1
            if j == len(patt):
                indices.append(i - j)
                j = lps[j - 1]
        else:
            if j > 0:
                j =  lps[j-1]
            else:
                i+=1
    return indices

if '__main__' == __name__:
    text = 'AAAABAAABAAAABAABA'
    pat = 'AAA'
    res = myKMPSearch(text, pat)
    print(f'pat: {pat}\tIndices: {res}')
