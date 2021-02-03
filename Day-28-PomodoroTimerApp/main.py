import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
LIGHTGREEN = "#bedbbb"
GREEN = "#16c79a"
DARKGREEN = "#99d22d"
BLUE = "#dff3e3"
PINK = "#e2979c"
RED = "#e7305b"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = '✓'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    global reps
    reps = 0
    window.after_cancel(timer)
    label1.config(text='Timer', fg=DARKGREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label2.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps%8 == 0:
        label1.config(text='Break', fg=RED)
        countdown(long_break_sec)
    elif reps%2 == 0:
        label1.config(text='Break', fg=PINK)
        countdown(short_break_sec)
    else:
        label1.config(text='Work', fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes = count//60
    seconds = count%60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        startTimer()
        label2.config(text=CHECKMARK*(reps//2))

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro Timer App')
window.minsize(width=200, height=200)
window.config(padx=100, pady=50, bg=BLUE)

# Canvas
background_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
canvas.create_image(100, 112, image=background_img)
timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME,35,'bold'))
canvas.grid(row=2,column=2)

# Label
label1 = Label(text='Timer', font=(FONT_NAME,40), bg=BLUE, fg=DARKGREEN)
label1.grid(row=1, column=2)
label2 = Label(text='', font=(FONT_NAME,14,'normal'), bg=BLUE, fg=GREEN)
label2.grid(row=4, column=2)

def start():
    startTimer()

def reset():
    resetTimer()

# Button
start_btn = Button(text='Start', command=start, font=FONT_NAME, bg=LIGHTGREEN, highlightthickness=0)
start_btn.grid(row=3, column=1)
reset_btn = Button(text='Reset', command=reset, font=FONT_NAME, bg=LIGHTGREEN, highlightthickness=0)
reset_btn.grid(row=3, column=3)

window.mainloop()