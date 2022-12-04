def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def hello():
    print("hello")

@do_twice
def greet(msg):
    print("hello "+ msg)

hello()
greet("ferdi")