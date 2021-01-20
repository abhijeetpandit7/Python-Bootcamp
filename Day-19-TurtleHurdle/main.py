from turtle import Turtle,Screen
import random

screen = Screen()
# Setup width & height of screen
screen.setup(width=500,height=400)

colors = ['red','orange','yellow','green','blue','purple']
turtles_obj = []
for i in range(6):
    tim = Turtle(shape='turtle')
    turtles_obj.append(tim)
    tim.penup()
    tim.color(colors[i])

race = 'yes'
while race=='yes':    
    # Set all turtles to start position
    for index,y in enumerate(range(-75,76,30)):
        turtles_obj[index].goto(-200,y)

    # Take user input for turtle bet
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet:
        race_on = True

    while race_on:
        for turtle in turtles_obj:
            if turtle.xcor() > 230:
                if user_bet in turtle.pencolor():
                    race = screen.textinput(title="Race again?", prompt=f"You've won! The {turtle.pencolor()} turtle is the winner!\n Race again? yes/no: ")
                else:
                    race = screen.textinput(title="Race again?", prompt=f"You've lost! The {turtle.pencolor()} turtle is the winner!\n Race again? yes/no: ")
                race_on = False
            distance = random.randint(0,10)
            turtle.forward(distance)

# Adding event listener
screen.listen()
screen.exitonclick()