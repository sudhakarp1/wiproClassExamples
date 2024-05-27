'''
    Search for a substring in a string and print its indices multiple index)
    
    string = 'this is a sample. jist trying it'
    substring='is'
'''
def printIndices(string , substring):
    strLen = len(string)
    subStrLen = len(substring)  

    for i in range(strLen - subStrLen):  
        if (string[i:i + subStrLen] == substring): # using slicing               
            print(i, end=',')
    print()

if '__main__' == __name__:
    string = 'this is a sample. jist trying it'
    substring='is'
    printIndices(string, substring);
