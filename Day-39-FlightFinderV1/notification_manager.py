#This class is responsible for sending notifications with the deal flight details.
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()
my_email = os.getenv('EMAIL')
to_email = os.getenv('TO_EMAIL')
my_password = os.getenv('PASSWORD')

class NotificationManager:
    
    def __init__(self):
        pass

    def send_alert(self, data):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=("Subject:Cheap Fare Alert!\n\n"+
                    "Low price alert!\n"+
                    f"Only Rs.{data['price']} "+
                    f"to fly from {data['cityFrom']}-{data['cityCodeFrom']} "+
                    f"to {data['cityTo']}-{data['cityCodeTo']},\n"+
                    f"from {data['dateFrom']} to {data['dateTo']}")
            )