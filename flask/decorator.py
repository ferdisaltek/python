import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")


def say_bye():
    print("byee")

def say_greeting():
    print("how are you ?")


say_hello()