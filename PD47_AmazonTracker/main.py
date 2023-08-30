# ----------------------------------------- Imports ----------------------------------------- #
import requests
from bs4 import BeautifulSoup
import smtplib
import os

# ----------------------------------- Web - Scraping desired item ----------------------------------#
url_link = input("Paste the url link of the product from amazon which you wish to monitor:")
expense_limit  = int(input("Enter your expense limit:"))
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
           "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
           }
response = requests.get(url=url_link,headers=headers).text
soup = BeautifulSoup(response,"lxml")
value = float(soup .find(name="span",class_="a-offscreen").getText().lstrip("$"))
name = str(soup.find(name="span",class_="a-size-large product-title-word-break").getText().strip())

# ----------------------------------- Mailing the User ----------------------------------#
my_mail = os.environ.get("A_my_mail")
my_pass = os.environ.get("A_my_pass")

if value < expense_limit:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Ensures a secure connection.
        connection.login(user=my_mail, password=my_pass)
        connection.sendmail(from_addr=my_mail, to_addrs=my_mail, msg=f"subject:Amazon Price Alert!\n\n Item name: {name} is now available at {value} . CLick here:{url_link}".encode('utf-8'))

