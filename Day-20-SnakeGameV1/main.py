import time
from turtle import Screen
from snake import Snake

screen = Screen()
# Set screen width & height
screen.setup(width=600, height=600)
# Set backgroundColor
screen.bgcolor('black')
# Set screen title
screen.title("Classic Snake Game")
# Turn off animation
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right') 

game_is_on = True
while game_is_on:
    # Update screen after each segment completes displacement
    screen.update()
    time.sleep(0.1)
    snake.move()  

screen.exitonclick()