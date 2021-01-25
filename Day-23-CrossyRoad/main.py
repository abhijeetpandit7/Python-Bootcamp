import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Crossy Road")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.up,'Up')

game_is_on = True
while game_is_on:
    time.sleep(player.pace)
    screen.update()
    
    # Create new car
    car_manager.create_car()

    # Car starts motion
    car_manager.move()

    # Car leaving screen
    # car_manager.redirect()

    # Detect collision with car
    for car in car_manager.cars:
        if (player.ycor() == car.ycor()):
            if player.distance(car) < 25:
                game_is_on = False
                scoreboard.game_over()

    # Player reaches finish line
    if player.is_finish():
        scoreboard.increment()

screen.exitonclick()