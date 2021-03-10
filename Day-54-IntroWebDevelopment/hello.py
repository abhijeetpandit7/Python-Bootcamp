# Run a Flask server
from flask import Flask
app = Flask(__name__)
# __name__ is a special built-in Python attribute ie a name of
# class, function, method, descriptor or generator instance
# '__main__' is name of scope, which means executing code in particular module.

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def hello_bye():
    return "Bye!"

# On Command Prompt:
# set FLASK_APP=hello.py
# flask run

# Alternative to `flask run`
if __name__=="__main__":
    app.run()