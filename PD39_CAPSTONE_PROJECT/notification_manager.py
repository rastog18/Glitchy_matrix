# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import os


class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ.get("FD_NM_account_sid")
        self.auth_token = os.environ.get("FD_NM_auth_token")
        self.number = os.environ.get("FD_NM_number")

    def sendmessage(self,list):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=f"Low price alert! For less than £{list[0]}, fly from Delhi-DEL to {list[1]}-{list[2]}, from {list[3]} to {list[4]}.",
            from_=self.number,
            to= os.environ.get("FD_NM_mynumber")
        )



