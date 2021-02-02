from tkinter import *

window = Tk()
window.title('First GUI')
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)

# Label
label = Label(text='Old Text', font=('arial',18,'bold'))
label.config(text='New Text')
label.grid(row=1,column=1)

# Button
def onClick():
    print("Do something")
    label.config(text=user_input.get())
# Calls onClick whenever clicked
button1 = Button(text='Click Me', command=onClick)
button1.grid(row=2,column=2)
button2 = Button(text='Click Me', command=onClick)
button2.grid(row=1,column=3)

user_input = Entry(width=30)
user_input.grid(row=3,column=4)

window.mainloop()