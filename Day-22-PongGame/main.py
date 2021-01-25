from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor('darkslategray')
screen.tracer(0)

lhs_scoreboard = Scoreboard(-50)
rhs_scoreboard = Scoreboard(50)
rhs_paddle = Paddle((350,0))
lhs_paddle = Paddle((-350,0))
ball = Ball()
screen.tracer(0)

screen.listen()
screen.onkey(lhs_paddle.up, 'w')
screen.onkey(lhs_paddle.down, 's')
screen.onkey(rhs_paddle.up, 'Up')
screen.onkey(rhs_paddle.down, 'Down')

game_on = True
while game_on:
    time.sleep(ball.pace)
    ball.move()
    screen.update()

    # Detect collision with top & bottom wall
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.wall_bounce()

    # Detect collision with paddle
    if (ball.distance(lhs_paddle) < 50 or ball.distance(rhs_paddle) < 50) and (ball.xcor() == 330 or ball.xcor() == -330):
        ball.paddle_bounce()
    
    # Detect collision with left & right wall
    if ball.xcor() > 330:
        lhs_scoreboard.increment()
        ball.home()
    elif ball.xcor() < -330:
        rhs_scoreboard.increment()
        ball.home()

screen.exitonclick()