import requests
from twilio.rest import Client

my_lat = 28.8333
my_lon = 78.7833
API_Key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC363873931e368fc6327c5a0b7b3bb2fe"
auth_token = "58e7665e1b376f3c0bc13010053084c7"

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
            to='+917895873303'
        )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is not going to rain, So you can continue with your favorite Family Guy.",
        from_='+14847498096',
        to='+917895873303'
    )
