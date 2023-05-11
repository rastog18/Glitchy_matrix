import time
import turtle
from turtle import Screen, Turtle, listen, onkey
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard

screen = Screen()
screen.title("Welcome to Arcade Game.")


def init():
    screen.setup(width=800, height=470)
    screen.bgpic("game.png")
    turtle.hideturtle()
    turtle.color("white")
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.write(arg="Pong Game", align="center", font=('Verdana', 60, 'normal'))
    turtle.goto(-150, -30)
    turtle.write(arg="Created by Shivam Rastogi", align="center", font=('Verdana', 10, 'normal'))
    time.sleep(1)


def screen_setup():
    screen_maker = Turtle()
    screen_maker.hideturtle()
    screen.setup(width=800, height=540)
    screen.bgcolor("blue")
    screen_maker.color("white")
    screen.tracer(0)
    screen_maker.penup()
    screen_maker.goto(0, 250)
    screen_maker.right(90)
    c = 250
    while c != -250:
        c -= 10
        screen_maker.pendown()
        screen_maker.forward(10)
        screen_maker.penup()
        screen_maker.forward(10)
        c -= 10
    screen.update()


def game():
    # Objects
    paddle1 = Paddle()
    paddle1.pad1()
    paddle2 = Paddle()
    paddle2.pad2()
    ball = Ball()
    scoreboard = Scoreboard()

    screen_setup()
    time.sleep(1)
    # Main
    p1 = 0
    p2 = 0

    listen()
    onkey(fun=paddle1.move_up, key="W")
    onkey(fun=paddle1.move_down, key="S")
    onkey(fun=paddle2.move_up, key="Up")
    onkey(fun=paddle2.move_down, key="Down")

    while p1 < 11 and p2 < 11:
        scoreboard.score1(p1)
        scoreboard.score2(p2)
        screen.update()
        p1, p2 = ball.move(paddle1, paddle2, p1, p2)

    scoreboard.game_over(p1)


init()
decision = (screen.textinput(title="Try Your Luck!", prompt="Do you want to play: 'Yes or No'"))
if decision == "Yes":
    screen.clear()
    game()
else:
    screen.bye()
screen.exitonclick()
