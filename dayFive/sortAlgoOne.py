from random import randint

def mySort(dataList):
	for i in range(len(dataList)):
		for j in range(i + 1, len(dataList)):
			if dataList[i] > dataList[j]:
				dataList[i], dataList[j] = dataList[j], dataList[i]
	return dataList			
						
	
def validateMySort():
	myList = [randint(1,100) for _ in range(10)]		
	print(f'len: {len(myList)}: {myList}')
	mySort(myList)
	print(f'len: {len(myList)}: {myList}')
	

if __name__ == '__main__':
	validateMySort()