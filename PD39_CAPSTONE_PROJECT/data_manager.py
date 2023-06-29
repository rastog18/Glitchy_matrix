# This class is responsible for talking to the Google Sheet.
import requests
from flight_data import FlightData
import os


class DataManager:

    def __init__(self, flight_data: FlightData):
        self.fdict = None
        self.city_list = None
        self.flight_obj = flight_data
        self.city = []
        self.item = []
        self.iswrite = True
        self.shetty_API = os.environ.get("FD_DM_shetty_API")
        self.shetty_header = {"Authorization": self.shetty_API}
        self.shetty_reader()

    def shetty_reader(self):
        shetty_endpoint_get = "https://api.sheety.co/671a84e3088f2b708d75aa10a672a436/flightDeals/prices"
        response = requests.get(url=shetty_endpoint_get, headers=self.shetty_header).json()["prices"]
        self.city_list = [item["city"] for item in response]
        self.city = [item["city"] for item in response if item["iataCode"] == ""]
        if self.city == []:
            self.iswrite = False
            self.item = [item["iataCode"] for item in response]
            self.fdict = {item["iataCode"]: item["lowestPrice"] for item in response}
            print("Data Sheet is up to date.")
            pass
        else:
            dat1 = {item["city"]: item["iataCode"] for item in response if item["iataCode"] == ""}
            data = self.flight_obj.code_adder(dat1, self.city)
            self.shetty_writer(data)

    def shetty_writer(self, data):
        city = list(data.keys())
        for item in city:
            index = self.city_list.index(item) + 2
            shetty_endpoint_put = f"https://api.sheety.co/671a84e3088f2b708d75aa10a672a436/flightDeals/prices/{index}"
            shetty_put_json = {"price": {"iataCode": data[item]}}
            response2 = requests.put(url=shetty_endpoint_put, json=shetty_put_json, headers=self.shetty_header)
        print("Data added successfully.")
        self.shetty_reader()

