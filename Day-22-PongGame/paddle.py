from turtle import Turtle
BOUNDARY_LIMIT = 220

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('aquamarine')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
    
    def up(self):
        if self.ycor() <= BOUNDARY_LIMIT:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -BOUNDARY_LIMIT:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)