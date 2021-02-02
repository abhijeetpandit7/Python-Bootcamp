from tkinter import *

window = Tk()
window.title('BMI Calculator')
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)
FONT = ("Comic Sans MS",14,'bold')

# Label
label1 = Label(text='Enter height:', font=FONT)
label1.grid(row=1,column=1)
label2 = Label(text='Enter weight:', font=FONT)
label2.grid(row=2,column=1)
label3 = Label(text='cm', font=FONT)
label3.grid(row=1,column=3)
label4 = Label(text='kg', font=FONT)
label4.grid(row=2,column=3)
label5 = Label(text= ' ', font=("Comic Sans MS",14,'normal'))
label5.grid(row=4,column=1)
label6 = Label(text=' ', font=("Comic Sans MS",14,'normal'))
label6.grid(row=5,column=1)

# Button
def onClick():
    bmi = float(weight.get()) / (float(height.get())/100)**2
    if(bmi <= 18.5):
        comment = "Underweight"
    elif(bmi <= 25):
        comment = "Normal weight"
    elif(bmi <= 30):
        comment = "Overweight"
    elif(bmi <= 35):
        comment = "Obese"
    else:
        comment = "Clinically obese"
    label5.config(text= f'BMI = {bmi:.2f}')
    label6.config(text=f'{comment}')

button = Button(text='Calculate', command=onClick, font=FONT)
button.grid(row=3,column=2)

# Entry
height = Entry(width=3, font=FONT)
height.grid(row=1,column=2)
height.focus()
weight = Entry(width=3, font=FONT)
weight.grid(row=2,column=2)

window.mainloop()