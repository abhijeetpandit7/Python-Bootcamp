import pandas as pd
import smtplib
import datetime as dt
import random

my_email = 'notmyemail@yahoo.com'
my_password = 'notmypassword'

persons_dict = pd.read_csv('birthdays.csv').to_dict('records')
present_month = dt.datetime.now().month
present_day = dt.datetime.now().day

def write_letter(name):
    filename = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filename,'r') as f:
        letter = f.read()
    return letter.replace('[NAME]',name)

def send_letter(to_email, message):
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Birthday Wishes\n\n{message}"
        )

for person in persons_dict:
    month = person['month']
    day = person['day']
    if present_month==month and present_day==day:
        name = person['name']
        email = person['email']
        message = write_letter(name)
        send_letter(email, message)