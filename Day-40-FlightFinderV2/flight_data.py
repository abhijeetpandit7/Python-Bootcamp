#This class is responsible for structuring the flight data.
class FlightData:

    def compare(self, price_data, lowest_price):
        # Normalize API price hike
        lowest_price += lowest_price*14.8/100
        self.price_data = price_data
        self.price_array = []
        self.date_array = []
        for data in self.price_data:
            self.price_array.append(int(data['price']))
            self.date_array.append((data['route'][0]['local_arrival'])[:10])
        self.min_price = min(self.price_array)
        return self.min_price < lowest_price

    def get_data(self):
        low_limit = self.price_array.index(self.min_price)
        self.price_array.reverse()
        high_limit = self.price_array.index(self.min_price)
        self.min_price -= self.min_price*13/100
        flight_details = {
            'price': round(self.min_price),
            'cityFrom': self.price_data[0]['route'][0]['cityFrom'],
            'cityCodeFrom': self.price_data[0]['route'][0]['cityCodeFrom'],
            'cityTo': self.price_data[0]['route'][0]['cityTo'],   
            'cityCodeTo': self.price_data[0]['route'][0]['cityCodeTo'],
            'dateFrom': self.date_array[low_limit],
            'dateTo': ''
        }
        self.date_array.reverse()
        flight_details['dateTo'] = self.date_array[high_limit]
        return flight_details