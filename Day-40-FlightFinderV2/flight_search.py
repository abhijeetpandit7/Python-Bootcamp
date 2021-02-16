#This class is responsible for talking to the Flight Search API.
from dotenv import load_dotenv
from pprint import pprint
from datetime import *
import requests
import os

load_dotenv()
FLY_FROM = 'BOM'
CURRENCY = 'INR'
FLIGHT_TYPE = 'oneway'
SORT_BY = 'date'

class FlightSearch:

    def __init__(self):
        self.from_date =(datetime.now()+timedelta(days=1)).strftime('%d/%m/%Y')
        self.to_date =(datetime.now()+timedelta(days=180)).strftime('%d/%m/%Y')
        self.kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search/"
        self.headers = {
        'apikey': os.getenv('API_KEY')
        }
        self.parameters = {
            'fly_from': FLY_FROM,
            'fly_to': '',
            'date_from': self.from_date,
            'date_to': self.to_date,
            'curr': CURRENCY,
            'flight_type': FLIGHT_TYPE,
            'one_per_date': 1,
            'sort': SORT_BY
        }
    
    def get_data(self, fly_to):
        self.parameters['fly_to'] = fly_to
        response = requests.get(url=self.kiwi_endpoint, params=self.parameters, headers=self.headers)
        try:
            data = response.json()['data']
        except KeyError:
            print(f"No flights available to {fly_to}")
            return []
        else:
            # pprint(data[0])
            return data