from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('azure')
        self.move_x = 10
        self.move_y = 10
        self.pace = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.move_y *= -1

    def paddle_bounce(self):
        self.move_x *= -1
        if self.pace > 0.02:
            self.pace -= 0.01

    def home(self):
        time.sleep(1)
        self.move_x *= -1
        self.goto(0,0)
        self.pace = 0.1