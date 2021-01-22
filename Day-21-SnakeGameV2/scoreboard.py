from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('green yellow')
        self.goto(x = 0, y = 170)
        self.score = 0
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        self.display()

    def increment(self):
        self.score += 1
    
    def display(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write('Game Over', align=ALIGNMENT, font=FONT)        