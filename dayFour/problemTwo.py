'''
Have list of name and mesg. 
	Sort the list and its assocative messages in order based on choice given by user.
		if choice it True
			sort based on name 
		else 
			sort based on mesg 

	validate your functions before sorting and after sorting by writing testcases using pytest.
'''

def sortedList(data, choice=True):
    sortedData = data
    if len(data)>0 :
        if choice is True:
            sortPos = 0
        else:
            sortPos = 1
        sortedData = sorted(data, key=lambda a: a[sortPos])
    return sortedData


def sortListCaller():
    myList = [(9,'Hello'),(67, 'aaai'),(55,'byeee'),(33,'Bhaiii'),(65,'Haiii')]
    print(f'myList: {myList}')
    newList = sortedList(myList)
    print(f'myList: {myList}--> {newList}')
    newList = sortedList(myList, False)
    print(f'myList: {myList}--> {newList}')



if __name__ == '__main__':
    sortListCaller()
