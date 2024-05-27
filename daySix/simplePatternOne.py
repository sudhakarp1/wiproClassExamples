'''
    Search for a substring in a string and print its indices multiple index)
    
    string = 'this is a sample. jist trying it'
    substring='is'
'''
def printIndices(string , substring):#naive pattern matching algorithm
    strLen = len(string)
    subStrLen = len(substring)  
         
    for i in range(strLen - subStrLen):  
        k = 0         
        for j in range(subStrLen):                 
            if (string[i + j] != substring[j]):
                break 
            k = j + 1

        if k == subStrLen:
            print(i, end=',')
    print()

if '__main__' == __name__:
    string = 'AAAAAAABAAAABAAABAAB'
    substring='AAAA'
    printIndices(string, substring);
