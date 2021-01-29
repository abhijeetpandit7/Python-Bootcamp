import turtle
from quiz import Quiz
from dataframe import Dataframe

screen = turtle.Screen()
screen.title('India States Game')
screen.bgpic('blank_states.GIF')

# # Get coordinates for states
# def get_coordinates(x,y):
#     print(x,y)
#     with open('new.txt','a') as f:
#         f.write(f',{x},{y}\n')
# turtle.onscreenclick(get_coordinates)
# turtle.mainloop()

df = Dataframe()
quiz = Quiz()
game_on = True
while game_on:
    input_state = screen.textinput(title=f'{quiz.score}/28 States correct',prompt='Enter state')
    if quiz.check_input(input_state, df.state_list):
        df.get_data(input_state)
        quiz.display_statename(df.state, df.x, df.y)
    if quiz.score == 28 or input_state == 'exit':
        game_on = False
        for state in df.state_list:
            if state not in quiz.correct_states:
                df.get_data(state)
                quiz.display_statename(df.state, df.x, df.y)

screen.exitonclick()