# Import Classes from module
from turtle import Turtle, Screen
# Create objects
tinny = Turtle()
my_screen = Screen()
# Access object attributes
canvh = my_screen.canvheight
# Access object methods
tinny.shape('turtle')
tinny.color('red','green')
tinny.forward(100)
my_screen.exitonclick()