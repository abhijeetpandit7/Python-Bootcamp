from turtle import Turtle
import random
BOUNDARY = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.color('orange')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(x=self.random_position(), y=self.random_position())

    def random_position(self):
        return random.randrange(-BOUNDARY,BOUNDARY,20)