from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

tim.shape('turtle')
tim.color('SeaGreen')

def move_forwards():
    tim.forward(10)
def move_down():
    tim.backward(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.onkey(move_forwards,"Up")
screen.onkey(move_down,"Down")
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")
screen.onkey(clear,"c")
# Adding event listener
screen.listen()
screen.exitonclick()