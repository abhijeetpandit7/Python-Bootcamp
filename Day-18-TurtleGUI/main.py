from turtle import Turtle, Screen
import random

# Changing module turtle's property()
# If its set to 255, color() takes rgb value in range(0,255)
# But here we pass decimal values using random() so set to 1 instead
import turtle
turtle.colormode(1)

# Create object of class Turtle
tim = Turtle()
tim.shape('turtle')
tim.color('SeaGreen')

# Draw square
def square():
    for i in range(4):
        tim.forward(100)
        tim.left(90)

# Draw dashed line
def dashedLine():
    for i in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon & decagon
def geometryShapes():
    for i in range(3,11):
        tim.color(random.random(), random.random(), random.random())
        for ii in range(i):
            tim.forward(100)
            tim.left(360/i)

# Random Walk
def randomWalk():
    tim.pensize(10)
    tim.speed(0)
    for i in range(200):
        tim.color(random.random(), random.random(), random.random())
        tim.setheading(random.choice([0,90,180,270]))
        tim.forward(30)

# Spirograph
def spirograph():
    tim.speed(0)
    for i in range(0,361,5):
        tim.color(random.random(), random.random(), random.random())
        tim.setheading(i)
        tim.circle(100)
    

screen = Screen()
screen.exitonclick()