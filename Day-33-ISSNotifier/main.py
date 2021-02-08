import requests
import json
import datetime as dt
import smtplib
import time

my_email = 'notmyemail@yahoo.com'
my_password = 'notmypassword'

MY_LAT = 19.049370
MY_LONG = 73.020462

def convTimezone(time):
    hour = int(time.split('T')[1].split(':')[0])
    new_hr = (hour + 5)%24
    return (f'{new_hr:02}')

def isNight():
    parameters = {
        'lat':MY_LAT,
        'lng':MY_LONG,
        'formatted':0
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(convTimezone(data['results']['sunrise']))
    sunset = int(convTimezone(data['results']['sunset']))
    current_hr = dt.datetime.now().hour
    return sunrise<=current_hr<=sunset


def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_position = (
        float(data['iss_position']['latitude']), 
        float(data['iss_position']['longitude'])
    )
    return MY_LAT-6<iss_position[0]<MY_LAT+6 and MY_LONG-6<iss_position[1]<MY_LONG+6:

def send_letter():
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:ISS Detected Overhead\n\nLook up in the sky!!"
        )

while True:    
    if is_iss_overhead() and isNight():
        send_letter()
    time.sleep(60)