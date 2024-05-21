def College(name):
    print(f'College name: {name}')
    def Group(gName):
        print(f'You are admitted to {gName} Group')
        def Section(className):
            print(f'You are in {className} part of {gName}')
            return 'something'
        return Section
    return Group

College('XYZ')('Science')('Mathematics Hons')

'''
college = College('XYZ')
group = college('Science')
section = group('Mathematics Hons')
#final = section()
#print(f'final Res: {final}')
'''
    