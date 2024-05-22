import os 
import pytest

from fileDirOps import createFile, createDir

@pytest.fixture
def tmpDir():
    return './'

def testCreateDirectory(tmpDir):
    dirPath = os.path.join(tmpDir,'MyDirNew1') #  './' +  'MyDirNew1'-->'./MyDirNew1'
    assert not os.path.exists(dirPath)# './MyDirNew1'
    createDir(dirPath)
    assert os.path.exists(dirPath) and os.path.isdir(dirPath)

def testCreateFile(tmpDir):
    dirPath = os.path.join(tmpDir,'MyDirNew1') # './MyNewDir1'      
    createDir(dirPath)
    filePath = os.path.join(dirPath,'aan.txt')# './MyNewDir1/aan.txt'
    assert not os.path.exists(filePath)
    createFile(filePath)
    assert os.path.exists(filePath) and os.path.isfile(filePath)

def myNameOne():
    assert True

def myNameTow():
    assert True
