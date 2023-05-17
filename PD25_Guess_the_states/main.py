from turtle import Turtle, Screen, listen

import pandas
import pandas as pd

cursor = Turtle()
screen = Screen()
c = 0  # To count how many times the user has answered correctly.

cursor.penup()
cursor.hideturtle()
screen.title("Name the States")
screen.bgpic("blank_states_img.gif")
screen.setup(width=700, height=500)
listen()

file = pd.read_csv("50_states.csv")
state_list = file["state"].to_list()
x_list = file["x"].to_list()
y_list = file["y"].to_list()


def state_writer(i, state):
    x = x_list[i]
    y = y_list[i]
    cursor.goto(x, y)
    cursor.write(arg=f"{state}", align="center", font=('Verdana', 10, 'normal'))

game = True
while game:
    guess = screen.textinput(title=f"Score:{c}", prompt="Enter State or ask for 'Help'")
    if guess == "Help":
        screen.tracer(0)
        #A new file will be created so that you can learn missing states.
        dict = {"country":state_list}
        data = pandas.DataFrame(dict)
        data.to_csv("Learn_Here.csv")
        for i in range(len(state_list)):
            cursor.color("red")
            state_writer(i, state_list[i])
        screen.tracer(1)
        game = False
    else:
        try:
            iteration = state_list.index(guess)
            c += 1
            state_writer(iteration, guess)
            state_list.remove(guess)
            x_list.pop(iteration)
            y_list.pop(iteration)
            if c == 50:
                game = False
        except ValueError:
            pass

screen.exitonclick()
