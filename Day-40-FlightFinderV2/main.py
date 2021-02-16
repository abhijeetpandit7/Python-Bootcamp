#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager

notification_manager = NotificationManager()
flight_search = FlightSearch()
flight_data = FlightData()
data_manger = DataManager()
user_list = data_manger.get_users()
destination_list = data_manger.get_data()

for city in destination_list:
    city_id = city['id']
    lowest_price = city['lowestPrice']
    fly_to = city['iataCode']
    price_data = flight_search.get_data(fly_to)
    # Check if no flights available
    if not price_data:
        continue
    is_cheap_deal = flight_data.compare(price_data, lowest_price)
    if is_cheap_deal:
        flight_details = flight_data.get_data()
        data_manger.update_data(city_id, flight_data.min_price)
        notification_manager.send_alert(flight_details, user_list)