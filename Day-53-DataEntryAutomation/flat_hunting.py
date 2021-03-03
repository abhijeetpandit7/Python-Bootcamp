from bs4 import BeautifulSoup
from pprint import pprint
import requests
# Add your url with required filters
ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B"west"%3A-122.77737889728276%2C"east"%3A-121.93143163165776%2C"south"%3A37.37039313455323%2C"north"%3A37.905433739761946%7D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"price"%3A%7B"max"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"pmf"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A3000%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"pf"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%7D'

class FlatHunting:
    
    def __init__(self):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
            'Accept-Language': 'en'
        }
        response = requests.get(url=ZILLOW_URL, headers=headers).text
        self.soup = BeautifulSoup(response,'html.parser')
        
    def get_data(self):
        anchor_tags_div = self.soup.find_all(name="div", class_="list-card-top")
        self.links = []
        for div in anchor_tags_div:
            href = div.find(name="a").get("href")
            if "http" not in href:
                self.links.append(f"https://www.zillow.com{href}")
            else:
                self.links.append(href)
        
        prices_div = self.soup.find_all(name="div", class_="list-card-price")
        self.prices = [self.strip_price(div.text) for div in prices_div]

        address_div = self.soup.find_all(name="address")
        self.addresses = [div.text for div in address_div]
    
    def strip_price(self, price):
        if '+' in price:
            split_ele = '+'
        elif '/' in price:
            split_ele = '/'
        else:
            split_ele = ' '
        return price.split(split_ele)[0]