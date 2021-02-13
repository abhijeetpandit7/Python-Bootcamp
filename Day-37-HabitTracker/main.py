import requests
import json
from dotenv import load_dotenv
import os
from datetime import datetime

USERNAME = 'abhijeet'
GRAPH_ID = 'graph1'
TODAY = datetime.today().strftime('%Y%m%d')
load_dotenv()

headers = {
    'X-USER-TOKEN': os.getenv("API_TOKEN"),
}

# Create a new user
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    'token': os.getenv("API_TOKEN"),
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# response = requests.post(url=pixela_endpoint, json=user_params)

# Create new graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    'id': GRAPH_ID,
    'name': 'Running Graph',
    'unit': 'km',
    'type': 'float',
    'color': 'ajisai' 
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Post a pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    'date': TODAY,
    'quantity': '5'
}
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

# Update a pixel
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
update_pixel_config = {
    'quantity': input('How many kilometers did you run today? ')
}
response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)

# Delete a pixel
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
update_pixel_config = {
    'quantity': '10'
}
# response = requests.delete(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)

print(response.text)