# The program does not contain sensitive data, such as API Key, number etc.
import requests
from twilio.rest import Client

my_lat = 28.8333
my_lon = 78.7833
API_Key = ""
account_sid = ""
auth_token = ""

parameter = {"lat":my_lat,
             "lon":my_lon,
             "exclude":"current,minutely,daily,alerts",
             "appid":API_Key}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?",params=parameter)
response.raise_for_status()
hour12_data = response.json()["hourly"][:12]
main_data = {hour12_data.index(i):i["weather"][0]["id"] for i in hour12_data}
values = main_data.values()

if min(values) <600:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Rainy Today",
            from_='+14847498096',
            to=''
        )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is not going to rain, So you can continue with your favorite Family Guy.",
        from_='+14847498096',
        to=''
    )
