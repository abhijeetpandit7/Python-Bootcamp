# This class is responsible for sending notifications with the deal flight details.
from calendar import month_name
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()
my_email = os.getenv('EMAIL')
my_password = os.getenv('PASSWORD')

class NotificationManager:

    def send_alert(self, data, users):
        link = (f"https://www.google.co.in/flights?hl=en#flt={data['cityCodeFrom']}.{data['cityCodeTo']}."+
            f"{data['dateFrom']}*{data['cityCodeTo']}.{data['cityCodeFrom']}.{data['dateTo']}")
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            for user in users:
                to_email = user['email']
                fName = user['firstName']
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=to_email,
                    msg=("Subject:Flight Deals Alert!✈️\n\n"+
                        f"Hi, {fName},\n"
                        f"Super cheap fares to {data['cityTo']}. Get in. On this!\n"+
                        f"This is the cheapest deal to {data['cityTo']} in the upcoming 6 months.\n\n"
                        f"Only ₹{data['price']:,} to fly from, \n"+
                        f"{data['cityFrom']} ({data['cityCodeFrom']}) "+
                        f"to {data['cityTo']} ({data['cityCodeTo']}).\n"+
                        f"Tickets available from {self.dateFormat(data['dateFrom'])} to {self.dateFormat(data['dateTo'])}\n"+
                        f"{link}\n\n"+
                        "Cheers, \nAbhijeet").encode('utf-8')
                )

    def dateFormat(self, str):
        arr = str.split('-')
        return (f"{arr[2]} {month_name[int(arr[1].strip('0'))]}, {arr[0]}")