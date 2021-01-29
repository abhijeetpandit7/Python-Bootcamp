from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 10, "normal")

class Quiz(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.correct_states = []

    def check_input(self,state,states):
        if state.title() in states and state.title() not in self.correct_states:
            self.score += 1
            self.correct_states.append(state.title())
            return True
        return False
    
    def display_statename(self,state,x,y):
        self.goto(x,y)
        self.write(f'{state}', align=ALIGNMENT, font=FONT)