import requests
import json

parameters = {
    'amount' : 10,
    'category' : 20,
    # 'difficulty' : 'easy',
    'type' : 'boolean'
}
response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
data = response.json()

question_data = data['results']