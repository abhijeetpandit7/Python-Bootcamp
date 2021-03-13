# Advanced decorators with *args & **kwargs
class User:

    def __init__(self,username):
        self.name = username
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper_function(*args,**kwargs):
        if(args[0].is_logged_in):
            function(args[0])
    return wrapper_function
    
@is_authenticated_decorator
def create_blog_post(user):
    print(f"Welcome to {user.name}'s new blog post!")

new_user = User("Abhijeet")
new_user.is_logged_in = True
create_blog_post(new_user)