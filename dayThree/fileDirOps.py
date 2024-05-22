
import os 
def createFile(filePath):
    with open(filePath, 'w') as fileObj:
        pass

def createDir(dirPath):
    os.makedirs(dirPath, exist_ok=True)
