
import os 
def listFiles(path):
    print(path) #./.pytest_cache
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childPath = os.path.join(path, filename)            
            listFiles(childPath)


if __name__ == '__main__':
    listFiles('./')
