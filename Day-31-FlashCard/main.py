from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ('Ariel',40,'italic')
FONT2 = ('Ariel',60,'bold')

try:
    df = pd.read_csv('./data/words_to_learn.csv')
except:
    df = pd.read_csv('./data/Punjabi_words.csv')
rows = df.shape[0]
from_lang = df.columns[0]
to_lang = df.columns[1]
# Can convert to various dictionary types, eg.records
to_learn = df.to_dict(orient='records')

window = Tk()
window.title('Flashy')
window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=1, column=1, columnspan=2)
card_title = canvas.create_text(400, 150, font=FONT1)
card_word = canvas.create_text(400, 263, font=FONT2)

def flip_card():
    global current_card
    # new_word = to_learn[rnd_row][to_lang]
    canvas.itemconfig(card_image, image=back_img)
    canvas.itemconfig(card_word, text=current_card[to_lang], fill='white')
    canvas.itemconfig(card_title, text=to_lang, fill='white')

current_card = random.choice(to_learn)
flip_timer = window.after(3000, flip_card, current_card)

def pop_card():
    global current_card
    to_learn.remove(current_card)
    new_df = pd.DataFrame(to_learn)
    new_df.to_csv('./data/words_to_learn.csv', index=False)
    next_card()

def next_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    # rnd_row = random.randint(0,rows)
    # # Using dataframe directly
    # new_word =  df[from_lang][rnd_row]
    # Using dictionary
    if (len(to_learn)==0):
        df = pd.read_csv('./data/Punjabi_words.csv')
        to_learn = df.to_dict(orient='records')
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=front_img)
    canvas.itemconfig(card_word, fill='black', text=current_card[from_lang])
    canvas.itemconfig(card_title, fill='black', text=from_lang)
    flip_timer = window.after(3000, flip_card)

# Button
cross_img = PhotoImage(file='./images/wrong.png')
unknown_btn = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_btn.grid(row=2, column=1)
check_img = PhotoImage(file='./images/right.png')
known_btn = Button(image=check_img, highlightthickness=0, command=pop_card)
known_btn.grid(row=2, column=2)

next_card()

window.mainloop()