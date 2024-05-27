'''
#[3:14 PM] Satyam Singh (Unverified)
def SplitterOne(string, delim =' '):
    return string.split(delim)

def SplitterTwo(string, delim =' '):
    lst = []
    word = ""
    for char in string:
        if char != delim:
            word += char
        else:
            if word:
                lst.append(word)
                word = ""
    if word:  
        lst.append(word)
    return lst 


if '__main__' == __name__:
    string = "This is a sample. jist trying it."
    result = SplitterOne(string)
    print(result)
    
    result = SplitterTwo(string)
    print(result)
'''


#[3:14 PM] yaswanthkumarkuna06@gmail.com (Unverified)
def mySpillterWithOutBulitIn(string, delim=" "):
    List = []
    tmp = ""
    for i in string:
        if i == delim:
            List.append(tmp)
            tmp = ""
        else:
            tmp += i
    List.append(tmp)
    return List
 
def mySpillterWithBuiltIn(string, delim=" "):
    return string.split(delim)
 
if __name__ == '__main__':
    string = 'this is a sample in a string. list trying it'
    myList = mySpillterWithBuiltIn(string)
    myList1 = mySpillterWithOutBulitIn(string)
 
    print("List with Built In methods: ", myList)
    print("List without Built In methods: ", myList1)
