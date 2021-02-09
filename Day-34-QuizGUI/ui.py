from tkinter import *
THEME_COLOR = "#375362"
FONT1 = ('Arial',14,'italic')
FONT2 = ('Arial',12,'normal')

class QuizInterface():

    # Optional, can pass quiz_brain datatype
    # from quiz_brain import QuizBrain
    # def __init__(self, quiz_brain: QuizBrain)

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz GUI")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # Label
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=FONT2)
        self.score_label.grid(row=1, column=2)

        # Canvas
        self.canvas  = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125, 
            text='Hola pepsi cola', 
            width=200, 
            fill=THEME_COLOR, 
            font=FONT1
        )
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        # Buttons
        check_img = PhotoImage(file='images/true.png')
        self.check_btn = Button(image=check_img, highlightthickness=0, command=self.true_pressed, bd=0)
        self.check_btn.grid(row=3, column=1)
        cross_img = PhotoImage(file='images/false.png')
        self.cross_btn = Button(image=cross_img, highlightthickness=0, command=self.false_pressed, bd=0)
        self.cross_btn.grid(row=3, column=2)

        self.get__question()

        self.window.mainloop()

    def get__question(self):
        self.enable_btn()
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            qtext = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=qtext)
        else:
            self.canvas.itemconfig(
                self.question_text, 
                text=f"You've completed the quiz.\nYour final score: {self.quiz.score}/10"
            )
            self.check_btn.config(state='disabled')
            self.cross_btn.config(state='disabled')
            self.disable_btn()

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.disable_btn()
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get__question)

    def disable_btn(self):
        self.check_btn.config(state='disabled')
        self.cross_btn.config(state='disabled')

    def enable_btn(self):
        self.check_btn.config(state='normal')
        self.cross_btn.config(state='normal')