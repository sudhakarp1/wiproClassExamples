

class genNumbers:
    def __init__(self, max ):
        self.num = 0
        self.max = max
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num < self.max:
            res = self.num
            self.num += 1 
            return res 
        raise StopIteration

for i in genNumbers(5):
    print(i)

'''       
numRes = genNumbers(5)
print(next(numRes))
print(next(numRes))
print(next(numRes))
print(next(numRes))
print(next(numRes))
print(next(numRes))
'''



