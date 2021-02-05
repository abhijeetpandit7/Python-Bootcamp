from tkinter import *
import pyperclip
import json
from tkinter import messagebox
from password_gen import generatePassword
LBLUE = '#eff8ff'
BLUE = '#cae4db'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genPassword():
    password_entry.delete(0,END)
    new_password = generatePassword()
    # Copy password to clipboard
    pyperclip.copy(new_password)
    password_entry.insert(index=0, string=new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def addPassword():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            'email' : email,
            'password' : password
        }
    }
    # Check for empty fields
    if website=='' or email=='' or password=='':
        messagebox.showwarning(title='Opps!', message="Please don't leave any field empty")
    else:
        # Show confirmation popup
        is_ok = messagebox.askokcancel(
            title=f'{website}', 
            message=f'Are you sure? \nEmail: {email} \nPassword: {password}'
        )
        # Add new data to data.json
        if is_ok:
            try:
                with open('data.json','r') as f:
                    # Read old data
                    data = json.load(f)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                # If no data found
                data = new_data
            else:
                # Update old data with new data
                data.update(new_data)
            finally:
                with open('data.json','w') as f:
                    # Saving new data to json
                    json.dump(data, f, indent=4)
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #
def findPassword():
    website = website_entry.get()
    try:
        with open('data.json','r') as f:
            data = json.load(f)
            email = data[website]['email']
            password = data[website]['password']
            messagebox.askokcancel(
                title=f'{website}', 
                message=f'Email: {email} \nPassword: {password}'
            )
    except (KeyError, FileNotFoundError):
        messagebox.showwarning(title='Error', message=f"No details for {website} exists.")

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
website_entry.grid(row=2, column=2, padx=10, pady=5, sticky='EW')
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=3, column=2, padx=10, pady=5, columnspan=2, sticky='EW')
email_entry.insert(index=END, string='youremail@email.com')
password_entry = Entry()
password_entry.grid(row=4, column=2, padx=10, pady=5, sticky='EW')

# Button
gen_password_btn = Button(text='Generate Password', command=genPassword, bg=BLUE)
gen_password_btn.grid(row=4, column=3)
add_btn = Button(text='Add', command=addPassword, bg=BLUE)
add_btn.grid(row=5, column=2, columnspan=2, sticky='EW')
search_btn = Button(text='Search', command=findPassword, bg=BLUE)
search_btn.grid(row=2, column=3, columnspan=2, sticky='EW')

window.mainloop()