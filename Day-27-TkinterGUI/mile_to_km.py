from tkinter import *

window = Tk()
window.title('Unit Conversion')
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)
FONT = ("Comic Sans MS",14,'bold')

# Label
label1 = Label(text='0', font=FONT)
label1.grid(row=2,column=2)
label2 = Label(text='Miles', font=FONT)
label2.grid(row=1,column=3)
label3 = Label(text='Kilometres', font=FONT)
label3.grid(row=2,column=3)
label4 = Label(text='is equivalent to:', font=FONT)
label4.grid(row=2,column=1)

# Button
def onClick():
    converted_value = float(user_input.get()) * 1.609
    label1.config(text=f'{converted_value:.2f}')
# Calls onClick whenever clicked
button = Button(text='Calculate', command=onClick, font=FONT)
button.grid(row=3,column=2)

# Entry
user_input = Entry(width=5, font=FONT)
user_input.grid(row=1,column=2)
user_input.focus()

window.mainloop()