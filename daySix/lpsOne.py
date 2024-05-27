

'''
    creating a lps table
    lps table --> Longest proper prefix which is also suffix 
'''
def lpsCreate(text, pat):
    lps = [0] * len(pat)
    for i in range(1,len(pat)):
        j = lps[i-1]
        while j > 0 and pat[i] != pat[j]:
            j = lps[j-1]
        if pat[i] == pat[j]:
            lps[i] = j+1
    return lps


if '__main__' == __name__:
    pat = 'abcd'
    res = lpsCreate('', pat)
    print(f'pat: {pat}\t\tlps: {res}')

    pat = 'AAAA'
    res = lpsCreate('', pat)
    print(f'pat: {pat}\t\tlps: {res}')

    
    pat = 'AAAABAAB'
    res = lpsCreate('', pat)
    print(f'pat: {pat}\t\tlps: {res}')


