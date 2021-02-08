import requests
import json
import datetime as dt

LATITUDE = 19.049370
LONGITUDE = 73.020462
def convTimezone(time):
    hour = int(time.split('T')[1].split(':')[0])
    minute = int(time.split('T')[1].split(':')[1])
    new_hr = hour + 5
    new_min = minute + 30
    if new_min>=60:
        new_min = new_min%60
        new_hr += 1
    new_hr = new_hr%24
    return (f'{new_hr:02}:{new_min:02}')

# response = requests.get(f'https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGITUDE}')
# Alternate method
parameters = {
    'lat':LATITUDE,
    'lng':LONGITUDE,
    'formatted':0
}
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = convTimezone(data['results']['sunrise'])
sunset = convTimezone(data['results']['sunset'])


print(sunrise)
print(f'{dt.datetime.now().hour}:{dt.datetime.now().minute}')
print(sunset)