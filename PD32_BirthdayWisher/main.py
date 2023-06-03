# ---------------------IMPORT/VARIABLE------------------------#
import smtplib
import random
import datetime as dt
import pandas
from email.message import EmailMessage
import pytz


my_mail = "shivamrastogi605@gmail.com"
my_pass = "hmpobwjwyrkvtots"

# 2. Check if today matches a birthday in the birthdays.csv
file = pandas.read_csv("birthdays.csv")
# india_timezone = pytz.timezone('Asia/Kolkata')
clock = dt.datetime.now(pytz.timezone('Asia/Kolkata'))
# clock = dt.datetime.now()
cur_month = clock.month
cur_date = clock.day

row = file[(file['month'] == cur_month) & (file['day'] == cur_date)]
if row.empty:
    print("No Bday")
else:
    row = row.to_dict()
    his_mail = list(row["email"].values())[0]
    name = list(row["name"].values())[0]
    no = random.choice([1,2,3])
    with open(file=f"./letter_templates/letter_{str(no)}.txt") as data:
        letter = data.read()
        letter = letter.replace("[NAME]",f"{name}")

    msg = EmailMessage()
    msg['Subject'] = "Happy Birthday"
    msg.set_content(f"{letter}")
    msg['From'] = my_mail
    msg['To'] = his_mail

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_mail,password=my_pass)
        connection.send_message(msg)

