from flat_hunting import FlatHunting
from data_entry import DataEntry

flat_hunting = FlatHunting()

flat_hunting.get_data()
addresses = flat_hunting.addresses
prices = flat_hunting.prices
links = flat_hunting.links

data_entry = DataEntry()

for i in range(len(links)):
    data_entry.write_data(addresses[i], prices[i], links[i])