# --------------------------- Imports/ Variables ---------------------------#
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_key_stock = "LH9HMGF5RHYDB88T"
API_key_news = "afee0acb80f840acac91388669ebe89f"
API_Key_twilio = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC363873931e368fc6327c5a0b7b3bb2fe"
auth_token = "242bc3ecb549693c971dfb3c19f4992b"

parameter_stocks = {"function": "TIME_SERIES_DAILY",
                    "symbol": STOCK,
                    "apikey": API_key_stock, }

# ------------------------------- Running API_Stocks -------------------------------#
response = requests.get(url="https://www.alphavantage.co/query?", params=parameter_stocks)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_keys = list(data.keys())[:2]

# Stock Prices at the time of closing for the previous two days.
day1_price = float(data[data_keys[0]]["4. close"])
day0_price = float(data[data_keys[1]]["4. close"])

percent_change = round(((day1_price - day0_price) / day1_price)*100,3)

if 5 <= percent_change <= -5:

    # ----------------------------Running API_News------------------------------------#
    parameter_news = {"q": COMPANY_NAME,
                      "from": data_keys[0],
                      "to": data_keys[1],
                      "sortBy": "popularity",
                      "apiKey": API_key_news}
    response_news = requests.get(url="https://newsapi.org/v2/everything?", params=parameter_news)
    data = response_news.json()["articles"][:3]
    news1 = [data[0]["title"], data[0]["description"]+data[0]["url"]]
    news2 = [data[1]["title"], data[1]["description"]+data[1]["url"]]
    news3 = [data[2]["title"], data[2]["description"]+data[2]["url"]]

    # ----------------------------Running API_Twilio----------------------------------#
    if 5 <= percent_change:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"TSLA: 🔺{percent_change}\nHeadline: {news1[0]}\nBrief: {news1[1]}\n\nHeadline: {news2[0]}\nBrief: {news2[1]}\n\nHeadline: {news2[0]}\nBrief: {news2[1]}",
            from_='+14847498096',
            to='+917895873303'
        )
    else:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"TSLA: 🔺{percent_change}\nHeadline: {news1[0]}\nBrief: {news1[1]}\n\nHeadline: {news2[0]}\nBrief: {news2[1]}\n\nHeadline: {news2[0]}\nBrief: {news2[1]}",
            from_='+14847498096',
            to='+917895873303'
        )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Your Stocks are consistent. Don't Worry.",
        from_='+14847498096',
        to='+917895873303'
    )


