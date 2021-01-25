from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

class CarManager:

    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            self.new_car()

    def new_car(self):
        new_car = Turtle(shape='square')
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(self.position())
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def position(self):
        # x = random.randrange(-275,275,20)
        y = random.randrange(-200,200,20)
        return (-300,y)

    def redirect(self):
        for car in self.cars:
            if car.xcor() > 300:
                car.setx(-car.xcor())
                car.sety(random.randrange(-200,200,20))