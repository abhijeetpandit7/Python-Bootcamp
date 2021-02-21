import os
import smtplib
import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
from dotenv import load_dotenv
load_dotenv()
my_email = os.getenv('FROM_EMAIL')
my_password = os.getenv('PASSWORD')
to_email = os.getenv('TO_EMAIL')

PRICE_LIMIT = 10000
product_url = "https://www.amazon.in/Fossil-Neutra-Chrono-Analog-Black/dp/B07CGRCJG3/ref=sr_1_32?crid=SCJBM1YN90HW&dchild=1&keywords=watch+for+men&qid=1613923319&refinements=p_n_feature_fourteen_browse-bin%3A11142592031%2Cp_n_feature_seven_browse-bin%3A1480900031%2Cp_n_feature_sixteen_browse-bin%3A15752672031%7C5756155031&rnid=5756152031&s=watches&sprefix=wat%2Caps%2C314&sr=1-32"

# Add header to bypass as actual user
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    'Accept-Language': 'en'
}
response = requests.get(url=product_url, headers=headers).text
content = BeautifulSoup(response, 'html.parser')
price_tag = content.find(name="span", id="priceblock_ourprice")
product_price = float(unidecode(price_tag).getText().split()[1].replace(',',''))
product_name = content.find(name="span", id="productTitle").getText().strip()

# Notify if price is below set margin price
if product_price<PRICE_LIMIT:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=("Amazon Price Alert!🎁\n\n"+
                f"{product_name} is now ₹{product_price}\n"+
                f"{product_url}"
                ).encode('utf-8')
        )