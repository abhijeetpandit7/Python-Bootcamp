# Sign up for new user
import os
import requests
from dotenv import load_dotenv
load_dotenv()

print("Welcome to the Flight Club!.")
print("Join our Flight Club and never pay full fare again")
fName = input("What is your first name?\n")
lName = input("What is your last name?\n")
email = input("What is your email?\n")
print("You're in the club, We'll email you with amazing flight deals!")

# Add new user to sheets
sheety_endpoint = "https://api.sheety.co/126f9e38bb1fc18f122cb26e242ee654/flightDeals/users"
headers = {
'Authorization': os.getenv('AUTH_TOKEN')
}
user_config = {
    'user': {
      "firstName": fName,
      "lastName": lName,
      "email": email
    }
}
response = requests.post(url=sheety_endpoint, json=user_config, headers=headers)
print(response.text)