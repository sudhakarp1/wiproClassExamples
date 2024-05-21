
class Decorator:
    def __init__(self, first):
        print(f'inside __init__ ==> {first}')
        self.arg = first

    def __call__(self, args=None):
        print(f'inside __call__() --> {args}')
        def Inner(someName):
            print(f'inside Inner() --> {someName}')
            args(someName)      

        return Inner

@Decorator('SOME ARG') 
def fun(args):
    print(f'Inside fun()--> {args}')
    
fun(102)


