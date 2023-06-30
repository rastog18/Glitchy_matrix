# This class is responsible for talking to the Flight Search API.
import requests
import datetime as dt
from notification_manager import NotificationManager
import os


class FlightSearch:
    def __init__(self, notification_manager: NotificationManager, list, dict):
        self.message_obj = notification_manager
        self.list = list
        self.dict = dict
        self.dates = []
        self.message = True
        self.search_API = os.environ.get("FD_FS_search_API")
        self.search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.clock_now = dt.datetime.now().strftime("%d/%m/%Y")
        year = int(dt.datetime.now().strftime("%Y"))
        month = int(dt.datetime.now().strftime("%m")) + 6
        date = int(dt.datetime.now().strftime("%m"))
        if month > 12:
            month -= 1
            year += 1
        self.clock_then = f"{date}/{month}/{year}"
        self.search()

    def search(self):
        header = {"apikey": self.search_API}
        for item in self.list:
            self.message = False
            price = self.dict[item]
            parameter = {"fly_from": "DEL",
                         "fly_to": item,
                         "date_from": self.clock_now,
                         "date_to": self.clock_then}
            response = requests.get(url=self.search_endpoint, headers=header, params=parameter).json()["data"]
            for i in response:
                if int(i["price"]) < price:
                    self.dates.append(i["local_departure"][:10])
                    self.message = True
                    dest_city = i["cityTo"]
            if self.message == True:
                message_list = [price, dest_city, item, self.dates[0], self.dates[len(self.dates) - 1]]
                self.message_obj.sendmessage(message_list)


