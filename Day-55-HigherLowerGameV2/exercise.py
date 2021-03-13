# Create a logging_decorator() which is going to log the name of the function that was called, 
# the arguments it was given and finally the returned output.
def logging_decorator(function):
    def wrapper(*args):
        print(f'You called {function.__name__}{args}')
        result = function(*args)
        print(f'It returned: {result}')
    return wrapper

@logging_decorator
def add(a,b,c):
    return (a+b+c)

add(1,2,3)