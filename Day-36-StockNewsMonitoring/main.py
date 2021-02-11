from dotenv import load_dotenv
import os
import requests
import json
from twilio.rest import Client
from datetime import *

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def send_sms():
    with open('text.txt','r') as f:
        sms = f.read()
        sms = sms.replace('[CHART]','📉')
        ARROW = '🔻'
        if stockprice_change_percent>0:
            ARROW = '🔺'
        sms = sms.replace('[ARROW]',ARROW)
        account_sid = os.getenv('ACCOUNT_SID')
        auth_token = os.getenv('AUTH_TOKEN')
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=sms,
                from_='+14078637908',
                to=os.getenv('MY_PHONE')
            )
        print(message.status)

def get_news():
    news_parameters = {
        'q': COMPANY_NAME,
        'sortBy': 'relevance',
        'apiKey': os.getenv('NEWS_API_KEY')
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()['articles'][:3]
    for data in news_data:
        with open('text.txt','a') as f:
            print(f"Headline: {data['title']}", file=f)
            print(f"Brief: {data['description']}", file=f)

av_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': os.getenv('ALPHA_VANTAGE_API_KEY')
}

response = requests.get(url=AV_ENDPOINT, params=av_parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']

today_date = (datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d')
yesterday_date = (datetime.now()-timedelta(days=2)).strftime('%Y-%m-%d')
today_stockprice = float(data[today_date]['4. close'])
yesterday_stockprice = float(data[yesterday_date]['4. close'])
stockprice_change_percent = 100*(today_stockprice - yesterday_stockprice)/today_stockprice
# print(f"{today_stockprice}\n{yesterday_stockprice}\n{stockprice_change_percent}")

if stockprice_change_percent<-5 or stockprice_change_percent>5:
    with open('text.txt','w') as f:
        print(".\nSTOCK MARKET NEWS MONITOR[CHART]", file=f)
        print(f"{STOCK}: [ARROW]{abs(round(stockprice_change_percent))}%", file=f)
    get_news()
    send_sms()