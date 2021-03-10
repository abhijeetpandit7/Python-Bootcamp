import time
# Python Decorator Function

# It wraps another function, modifies or add some additional functionality
def delay_decorator(function):
    def wrapper_function():
        # Do something
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")
say_hello()

def say_greeting():
    print("Greeting")
# `@delay_decorator` Alternative for
decorated_function = delay_decorator(say_greeting)
decorated_function()

def say_bye():
    print("Bye")