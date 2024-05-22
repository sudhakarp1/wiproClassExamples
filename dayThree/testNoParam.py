'''
    Using multiple datas in a single test function without passing 
    paramters or using fixtures
'''

def testAddition():
    for data in [(10,20,30),(30, 50 ,80),(10,-5,5)]:
        a , b, expectedRes = data
        res = a + b
        assert res == expectedRes
