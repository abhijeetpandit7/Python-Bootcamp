from tkinter import *
import pyperclip
from tkinter import messagebox
from password_gen import generatePassword
LBLUE = '#eff8ff'
BLUE = '#cae4db'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.minsize(width=200, height=200)
window.config(padx=50, pady=50, bg=LBLUE)

# Canvas
bg_image = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, bg=LBLUE, highlightthickness=0)
canvas.create_image(100, 100, image=bg_image)
canvas.grid(row=1, column=2)

# Label
label1 = Label(text='Website:', bg=LBLUE)
label1.grid(row=2, column=1)
label2 = Label(text='Email/Username:', bg=LBLUE)
label2.grid(row=3, column=1)
label3 = Label(text='Password:', bg=LBLUE)
label3.grid(row=4, column=1)

# Entry
website_entry = Entry()
website_entry.grid(row=2, column=2, padx=10, pady=5, columnspan=2, sticky='EW')
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=3, column=2, padx=10, pady=5, columnspan=2, sticky='EW')
email_entry.insert(index=END, string='youremail@email.com')
password_entry = Entry()
password_entry.grid(row=4, column=2, padx=10, pady=5, sticky='EW')

def genPassword():
    password_entry.delete(0,END)
    new_password = generatePassword()
    # Copy password to clipboard
    pyperclip.copy(new_password)
    password_entry.insert(index=0, string=new_password)

def addPassword():
    # Check for empty fields
    if website_entry.get()=='' or email_entry.get()=='' or password_entry.get()=='':
        messagebox.showwarning(title='Opps!', message="Please don't leave any field empty")
    else:
        # Show confirmation popup
        is_ok = messagebox.askokcancel(
            title=f'{website_entry.get()}', 
            message=f'Are you sure? \nEmail: {email_entry.get()} \nPassword: {password_entry.get()}'
        )
        # Add new data to data.txt
        if is_ok:
            with open('data.txt','a') as f:
                # Using print() to write files
                print(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}", file=f)
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()

# Button
gen_password_btn = Button(text='Generate Password', command=genPassword, bg=BLUE)
gen_password_btn.grid(row=4, column=3)
add_btn = Button(text='Add', command=addPassword, bg=BLUE)
add_btn.grid(row=5, column=2, columnspan=2, sticky='EW')

window.mainloop()