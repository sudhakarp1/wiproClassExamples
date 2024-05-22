'''
    UDE --> User Defined Exceptions
'''

class UDException(Exception):
    pass

def testUDExcept():
    try:
        print('\nStatement #1...')
        raise UDException('User Defined Exception')
        print('\nStatement #2...')
    except UDException as e:
        assert str(e) == 'User Defined Exception'
    else:
        assert False, 'User Defined Exception Not Raised'


    
    
