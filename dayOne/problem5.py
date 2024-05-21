'''
    Problem solved by satyam sk singh
'''

def header_decorator(header_msg):
    def decorator(func):
        def wrapper(message):
            print(header_msg)
            return func(message)
        return wrapper
    return decorator
 
def footer_decorator(footer_msg):
    def decorator(func):
        def wrapper(message):
            result = func(message)
            print(footer_msg)
            return result
        return wrapper
    return decorator
 
@header_decorator("This is the Header")
@footer_decorator("This is the Footer")
def print_message(message):
    print(message)
 
print_message("This is the message.")
