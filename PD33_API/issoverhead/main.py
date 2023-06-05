# -------------------- IMPORT / VARIABLE---------------------#
import requests, smtplib
from datetime import datetime, timezone
import time

run_again = False
MY_LAT = 28.833139  # Your latitude
MY_LONG = 78.765282  # Your longitude
my_mail = "shivamrastogi605@gmail.com"
my_pass = "____________"

# -------------------- SETTING UP API ---------------------#
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def iss_checker():
    global run_again
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = int(datetime.now(timezone.utc).hour)
    print(iss_longitude, iss_latitude)
    if -5 < (iss_longitude - MY_LONG) < 5 < (iss_longitude - MY_LAT) < -5:
        run_again = True
        if sunset < time_now < sunrise:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_mail, password=my_pass)
                connection.send_message(from_addr=my_mail, to_addrs="shivam20050125@gmail.com",
                                        msg="subject:ISS_SATTILITE Approaching\n\nLook Up")
    else:
        run_again = False


while True:
    time.sleep(60)
    iss_checker()
