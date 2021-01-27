import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
# Set screen width & height
screen.setup(width=600, height=600)
# Set backgroundColor
screen.bgcolor('darkgreen')
# Set screen title
screen.title("Classic Snake Game")
# Turn off animation
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment()
        snake.grow()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()