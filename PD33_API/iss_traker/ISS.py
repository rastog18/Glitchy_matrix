from turtle import Turtle, Screen
import requests
import time

# --------------------------- Objects/Varibales -------------------------------#
obj = Turtle()
screen = Screen()
iss_tracker = True

# --------------------------- Screen -------------------------------#
screen.title("ISS_TRACKER")
screen.bgpic("map.png")
# screen.screensize(canvwidth=850,canvheight=506)
screen.setup(width=1050, height=470)
# screen.setworldcoordinates()
screen.listen()

# --------------------------- ISS -------------------------------#
obj.shape("circle")
obj.shapesize(stretch_wid=0.25, stretch_len=0.25)
obj.color("red")
obj.hideturtle()
obj.penup()
obj.goto(0, -56)


# x =56, y = 59

def exit_iss(x, y):
    global iss_tracker
    iss_tracker = False


screen.onclick(fun=exit_iss)

# --------------------------- ISS_API -------------------------------#
while iss_tracker:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    xunit = iss_longitude / 20 * 56
    yunit = (iss_latitude / 20 * 59) - 59
    obj.goto(xunit, yunit)
    obj.showturtle()
    print(iss_longitude, iss_latitude)
    time.sleep(1)


