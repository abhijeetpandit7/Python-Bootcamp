from datetime import datetime
import requests
import json
import os
from dotenv import load_dotenv
from twilio.rest import Client
# For accessing through server
# from twilio.http.http_client import TwilioHttpClient
load_dotenv()

LETTER = '📰'
UMBRELLA = '☂️'
SUNNY = '☀️'
MIN = '🔻'
MAX = '🔺'

# proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
parameters = {
    'lat': 19.049370,
    'lon': 73.020462,
    'units': 'metric',
    'exclude': 'current,minutely,daily,alerts',
    'appid': os.getenv('API_KEY')
}
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
all_data = response.json()['hourly'][:16]

weather_data = []
for data in all_data:
    weather_data.append({
        'time': datetime.fromtimestamp(data['dt']).strftime('%I:%M %p'),
        'temperature': data['temp'],
        'weather_id': data['weather'][0]['id'],
        'weather_condition': data['weather'][0]['main'],
        'weather_description': data['weather'][0]['description']
    })

did_rain = 0
min_temp=weather_data[0]['temperature']
min_temp_time=weather_data[0]['time']
max_temp=weather_data[0]['temperature']
max_temp_time=weather_data[0]['time']
with open('text.txt','w') as f:
    f.write(".\n[LETTER]Daily Weather Forecast[LETTER]")
for coll in weather_data:
    if coll['weather_id'] < 700:
        did_rain += 1
        if did_rain==1:
            with open('text.txt','a') as f:
                f.write("Please carry an umbrella today[UMBRELLA]!!")
        with open('text.txt','a') as f:
            f.write(f"\n{coll['time']} => {coll['weather_description'].title()}")
    if coll['temperature'] < min_temp:
        min_temp = coll['temperature']
        min_temp_time = coll['time']
    if coll['temperature'] > max_temp:
        max_temp = coll['temperature']
        max_temp_time = coll['time']
if (did_rain==0):
    with open('text.txt','a') as f:
        f.write("\nNeed not carry umbrella today![SUNNY]")
with open('text.txt','a') as f:
    f.write(f"\n{max_temp_time} => Max: {max_temp}°C[MAX] \n{min_temp_time} => Min: {min_temp}°C[MIN]")

with open('text.txt','r') as f:
    sms = f.read()
    sms = sms.replace('[LETTER]',LETTER)
    sms = sms.replace('[UMBRELLA]',UMBRELLA)
    sms = sms.replace('[SUNNY]',SUNNY)
    sms = sms.replace('[MIN]',MIN)
    sms = sms.replace('[MAX]',MAX)

# Send sms
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}
client = Client(account_sid, auth_token)
#  ,http_client=proxy_client)
message = client.messages \
                .create(
                     body=sms,
                     from_='+14078637908',
                     to=os.getenv('MY_PHONE')
                 )

print(message.status)