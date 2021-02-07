import smtplib
import datetime as dt
import random

my_email = 'notmyemail@yahoo.com'
my_password = 'notmypassword'
to_email = 'notmyemail@gmail.com'
weekday = dt.datetime.now().weekday()

if weekday==0:
    
    with open('quotes.txt','r') as f:
        quotes = f.read().splitlines()
    
    with smtplib.SMTP(host='smtp.mail.yahoo.com', port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Monday Motivational Quote\n\n{random.choice(quotes)}"
        )