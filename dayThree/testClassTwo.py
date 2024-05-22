
class TestClassOne:
    myData = 0
    def testOne(self):
        self.myData = 1
        print(f'\n in testOne() myData: {self.myData}')
        assert self.myData == 1

    def testTwo(self):
        self.myData = 1
        print(f'\n in testTwo() myData: {self.myData}')
        assert self.myData == 1
    