import time
import random
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def game():
    screen.bgpic("game 2.png")
    screen.setup(width=600, height=580)
    screen.tracer(0)
    obj = Player()
    car_list = []
    c = 1
    STARTING_MOVE_DISTANCE = 24
    MOVE_INCREMENT = 4
    score = Scoreboard()

    game_is_on = True
    screen.update()
    screen.listen()

    while game_is_on:
        score.score(c)
        screen.onkey(fun=obj.move_turtle, key="Up")
        screen.update()
        time.sleep(0.1)
        a = random.randint(0, 5)
        if a == 2:
            car = CarManager()
            car_list.append(car)
        for j in car_list:
            j.car_move(STARTING_MOVE_DISTANCE)
            # checking for collision of turtle with car.
            if obj.distance(j) < 30:
                score.collision()
                obj.hideturtle()
                game_is_on = False
            if obj.ycor() > 280:
                c += 1
                STARTING_MOVE_DISTANCE += MOVE_INCREMENT
                obj.goto(0, -280)


def init():
    screen.setup(width=800, height=470)
    screen.bgpic("game.png")
    turtle.hideturtle()
    turtle.color("white")
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.write(arg="Cross Road", align="center", font=('Courier', 60, 'normal'))
    turtle.goto(-150, -30)
    turtle.write(arg="Created by Shivam Rastogi", align="center", font=('Courier', 10, 'normal'))
    time.sleep(1)


screen = Screen()
init()
decision = (screen.textinput(title="Try Your Luck!", prompt="Do you want to play: 'Yes or No'"))
if decision == "Yes":
    screen.clear()
    game()
else:
    screen.bye()
screen.exitonclick()

screen.exitonclick()
