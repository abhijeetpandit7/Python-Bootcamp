#This class is responsible for talking to the Google Sheet.
import os
import json
from pprint import pprint
import requests
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/126f9e38bb1fc18f122cb26e242ee654/flightDeals"
        self.headers = {
        'Authorization': os.getenv('AUTH_TOKEN')
        }

    def get_data(self):
        response = requests.get(url=self.sheety_endpoint+'/prices', headers=self.headers)
        data = json.loads(response.text)['prices']
        return data

    def update_data(self, row_id, new_price):
        sheety_update_endpoint = f"{self.sheety_endpoint+'/prices'}/{row_id}"
        price_config = {
            'price': {
                "lowestPrice": round(new_price)
            }
        }
        response = requests.put(url=sheety_update_endpoint, json=price_config , headers=self.headers)
        print(response.text)

    def get_users(self):
        response = requests.get(url=self.sheety_endpoint+'/users', headers=self.headers)
        data = json.loads(response.text)['users']
        return data