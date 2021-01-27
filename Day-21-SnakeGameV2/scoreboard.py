from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('green yellow')
        self.goto(x = 0, y = 200)
        self.score = 0
        self.high_score = self.fetch_score()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        self.display()

    def fetch_score(self):
        with open('data.txt','r') as file:
            content = file.read()
            return int(content)

    def increment(self):
        self.score += 1
        self.display()
    
    def display(self):
        self.clear()
        self.write(f'Score: {self.score} | Highest: {self.high_score}', align=ALIGNMENT, font=FONT)
    
    # Not using this method
    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write('Game Over', align=ALIGNMENT, font=FONT)     

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt','w') as file:
                file.write(f"{self.score}")
        self.score = 0
        self.display()
           