from turtle import *
import time
from Snake import Snake
from Food import Food
from scoreboard import Scoreboard


def init():
    global decision
    hideturtle()
    screen.setup(width=500, height=400)
    screen.bgpic("game.png")
    penup()
    tracer(0)
    goto(0, 160)
    write(arg="Welcome to Snake.io", align="center", font=('Verdana', 20, 'normal'))
    goto(0, -180)
    write(arg="Created by Shivam Rastogi", align="center", font=('Verdana', 10, 'normal'))
    update()
    time.sleep(1)
    decision = (textinput(title="Try Your Luck!", prompt="Do you want to play: 'Yes or No'"))
    tracer(0)


def screen_set():
    screen.bgpic("")
    colormode(255)
    # Setting the Screen
    screen.setup(width=500, height=500)
    screen.tracer(0)
    screen.listen()
    screen.bgcolor("black")
    screen.onkey(fun=snake.turn_left, key="Left")
    screen.onkey(fun=snake.turn_right, key="Right")
    screen.onkey(fun=snake.turn_up, key="Up")
    screen.onkey(fun=snake.turn_down, key="Down")
    screen.title("Snake.io")


def game_setup():
    screen_set()
    snake.begin()
    count = 0
    scoreboard.score(0)
    game_is_on = True
    while game_is_on:
        snake.move()
        x = snake.snake_head.xcor()
        y = snake.snake_head.ycor()
        screen.update()
        time.sleep(0.1)

        if snake.snake_head.distance(food.position()) < 20:
            snake.create_body()
            food.food_posit()
            count += 1
            scoreboard.score(count)

        # Detecting collision with wall.
        if x >= 250 or x <= -250 or y >= 250 or y <= -250:
            game_is_on = False
            clearscreen()
            scoreboard.game_over(count)

        # Detecting collision with itself.
        for i in snake.snake_body[1:]:
            if i.distance(x, y) < 5:
                game_is_on = False
                clearscreen()
                scoreboard.game_over(count)

    screen.exitonclick()


screen = Screen()
init()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

if decision == "Yes":
    update()
    game_setup()
else:
    bye()
