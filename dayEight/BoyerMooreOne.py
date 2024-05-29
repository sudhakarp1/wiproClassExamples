def BCTable(patt):    
    table = {}
    for i in range(len(patt)):
        table[patt[i]] = i
    
    return table 

def boyerMooreSearch(text, patt):
    textLen = len(text)
    pattLen = len(patt)
    bctable = BCTable(patt)
    #print(f'table: {bctable}')
    indices = []
    i = 0
    while i < textLen - pattLen:
        j = pattLen - 1
        while j >= 0 and patt[j] == text[ i + j ]:
            j -= 1        
        if j < 0:
            indices.append(i)
            i+=1
        else:
            if text[i+j] in bctable:                
                i += max(1, j - bctable[text[i+j]])
            else:
                i += j + 1
    return indices

if __name__ == '__main__':
    text = 'AAAABAAABAAAABAABA'
    pat = 'AAB'
    res = boyerMooreSearch(text, pat)
    print(f'pat: {pat}\tIndices: {res}')
