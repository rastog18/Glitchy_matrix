import requests
import datetime as dt
import os
query = input("Enter your Workout:")
# ---------------------------Nutritionix API website-------------------------_#
nutri_API = os.environ.get("WS_nutri_API")
nutri_Appid = os.environ.get("WS_nutri_Appid")
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_parameter={"query":query,
                 "gender":"male",
                 "weight_kg":79.1,
                 "height_cm":180,
                 "age":18}

nutri_header = {"x-app-id":nutri_Appid,"x-app-key":nutri_API}

response = requests.post(url=nutri_endpoint,json=nutri_parameter,headers=nutri_header).json()["exercises"]

# ---------------------------Shetty_Spreadsheet API website-------------------------_#
shetty_endpoint = "https://api.sheety.co/671a84e3088f2b708d75aa10a672a436/myWorkoutSessions/workouts"
shetty_API = os.environ["WS_shetty_API"]
shetty_header = {"Authorization":f"Bearer {shetty_API}","Content-Type":"application/json"}
date = dt.datetime.now().strftime("%Y/%m/%d")
time = dt.datetime.now().strftime("%X")

for i in response:
    excercise = i["user_input"]
    duration = i["duration_min"]
    calories = i["nf_calories"]
    Json = {"workout" :{"date":date,
                    "time":time,
                    "exercise":excercise,
                    "duration":duration,
                    "calories":calories}}
    response2 = requests.post(url=shetty_endpoint,json=Json,headers=shetty_header)
    print(response2.text)