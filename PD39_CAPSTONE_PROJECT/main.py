# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


flight_obj = FlightData()
filemanager = DataManager(flight_data = flight_obj)
message_obj = NotificationManager()
iata_list = filemanager.item
price_dict = filemanager.fdict
flight_searcher = FlightSearch(message_obj,iata_list,price_dict)
