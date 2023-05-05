from turtle import Turtle, Screen,textinput
import random


screen = Screen()

decision = textinput( prompt= "CHOOSE A COLOR:",title="Which turtle do you bet on ?")
screen.setup(width=675, height=800)
screen.bgpic("racetrack.png")
color = ["red", "turquoise", "green", "blue", "purple"]
turtles = []
x = -250
y = -320

for i in range(5):
    turtle = Turtle()
    turtle.turtlesize(stretch_len=4,stretch_wid=4)
    turtle.color(color[i])
    turtles.append(turtle)
    turtle.shape("turtle")
    turtle.penup()
    turtle.setposition(x, y)
    y += 160

a = True
while a is True:
    for i in turtles:
        i.speed(10)
        dist = random.randint(0,10)
        i.forward(dist)
        x = i.xcor()
        if x >= 240:
            y = i.color()
            a = False

if y[0] == decision:
    print("You won the bet.")
else:
    print(f"You Loose. {y[0]}Turtle won the game.")
screen.exitonclick()


