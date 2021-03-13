from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1 style="text-align:center">Guess a number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=500 style="display:block; margin:auto">'

actual_number = random.randint(1,9)
print(f"Shhh! Answer is {actual_number}")

@app.route("/<int:guess>")
def game(guess):
    if guess==actual_number:
        message = 'You found me!'
        color = 'green'
        url = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'
    elif guess>actual_number:
        message = 'Too high, try again!'
        color = 'purple'
        url='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
    else:
        message = 'Too low, try again!'
        color = 'tomato'
        url='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'

    return f'<h1 style="text-align:center; color:{color}">{message}</h1>'\
        f'<img src="{url}" width=400 style="display:block; margin:auto">'

if __name__=='__main__':
    app.run(debug=True)