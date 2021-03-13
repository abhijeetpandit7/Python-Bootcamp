from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1 style="text-align:center">Hello World</h1>'\
        '<img src="https://media.giphy.com/media/z3piokwf0WPH81MOhu/giphy.gif" width=200px>'\
        '</div>'

def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f'<i>{function()}</i>'
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello {name}, you're {number} years old."

if __name__=="__main__":
    app.run(debug=True)