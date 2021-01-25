from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        self.pace = 0.1

    def up(self):
        self.forward(MOVE_DISTANCE)
    
    def is_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.pace *= 0.9
            return True
        return False