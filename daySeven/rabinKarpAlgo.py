'''
    Rabin-Karp algo for pattern matching
'''
def rabinKarpAlgo(text, patt):
    textLen = len(text) # 'AAAABAA ABAAAABAABA' -->18
    pattLen = len(patt) # AAA --> 3
    prime = 101
    indices = []
    patternHash =  0 
    for i in range(pattLen):
        patternHash = (patternHash * 100 + ord(patt[i])) %  prime 
    
    for i in range(textLen - pattLen + 1): #1 --> 15 
        subStrHash = 0
        for j in range(pattLen):
            subStrHash = (subStrHash * 100 + ord(text[i+j])) %  prime 
        #'AAA' == 'AAA'
        if patternHash == subStrHash and text[i:i+pattLen] == patt:
            indices.append(i)

    return indices       
           
if __name__ == '__main__' :
    text = 'AAAABAAABAAAABAABA' #19
    pat = 'AAB'  #3
    res = rabinKarpAlgo(text, pat)
    print(f'pat: {pat}\tIndices: {res}')