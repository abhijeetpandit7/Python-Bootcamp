import smtplib
import datetime as dt

# Note: Turn on less secure app access in Google settings
# For Yahoo create a new app password
my_email = 'notmyemail@yahoo.com'
my_password = 'notmypassword'
to_email = 'notmymail@gmail.com'

# # Host => Gmail:smtp.gmail.com | Hotmail:smtp.live.com | Yahoo:smtp.mail.yahoo.com
# connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
# # Secure connection
# connection.starttls()
# # Login
# connection.login(user=my_email, password=my_password)
# connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Hello Abhijeet!")
# connection.close()

with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=to_email, 
        msg="Subject:Greetings\n\nHello Abhijeet!"
    )
    
# print(dt.datetime.now())
# print(dt.datetime(2000,7,13))