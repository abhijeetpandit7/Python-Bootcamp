from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 20, "bold")
POSITION = (-220,240)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.score = 0
        self.write(f'Level: {self.score}', align=ALIGNMENT, font=FONT)
    
    def increment(self):
        self.score += 1
        self.clear()
        self.write(f'Level: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over', align=ALIGNMENT, font=FONT)