# This class is responsible for structuring the flight data.
import requests
import os


class FlightData:
    def __init__(self):
        self.search_API = os.environ.get("FD_FD_search_API")

    def code_adder(self, data, city):
        endpoint = "https://api.tequila.kiwi.com/locations/query"
        header = {"apikey": self.search_API}
        for i in city:
            params = {"term": i, "location_types": "airport"}
            response2 = requests.get(url=endpoint, headers=header, params=params).json()
            id = response2["locations"][0]["id"]
            data[i] = id
        return data


