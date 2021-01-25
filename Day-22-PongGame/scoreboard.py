from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")
Y = 250

class Scoreboard(Turtle):

    def __init__(self,x):
        super().__init__()
        self.center_line()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('cadetblue')
        self.goto(x,Y)
        self.write(f'{self.score}', align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f'{self.score}', align=ALIGNMENT, font=FONT)

    def center_line(self):
        line = Turtle()
        line.hideturtle()
        line.speed('fastest')
        line.color('aquamarine')
        line.pensize(3)
        line.setheading(270)
        for y in range(300,-300,-20):
            line.penup()
            line.goto(0,y)
            line.pendown()
            line.forward(10)