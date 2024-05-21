class Decorator:
    def __init__(self, *args):
        print(f'Arguments passed {args}', *args)



obj1 = Decorator()
obj2 = Decorator(10,20)
obj3 = Decorator(10,20,'test','rest','best')
 