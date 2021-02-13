import requests
import json
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
GENDER = 'male'
WEIGHT = 70
HEIGHT = 172
AGE = 20

# Get data based on user workout inut
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise/"
headers = {
    'x-app-id': os.getenv("API_ID"),
    'x-app-key': os.getenv("API_KEY")
}
params = {
    'query': input("Please tell me about your workout/exercise:\n"),
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}
response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
data = json.loads(response.text)['exercises'][0]
date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%X')
exercise = data['user_input'].title()
duration = data['duration_min']
calories = data['nf_calories']

# Write data to google sheets
sheety_endpoint = "https://api.sheety.co/126f9e38bb1fc18f122cb26e242ee654/workoutTracker/workouts"
headers = {
    'Authorization': os.getenv('AUTH_TOKEN')
}
sheets_data = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories
    }
}
response = requests.post(url=sheety_endpoint, json=sheets_data, headers=headers)
print(response.text)