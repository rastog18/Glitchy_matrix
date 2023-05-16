import sys
from turtle import *
import time
from Snake import Snake
from Food import Food
from scoreboard import Scoreboard
import pickle


def init():
    global decision
    scr_turtle = Turtle()
    scr_turtle.hideturtle()
    screen.setup(width=500, height=400)
    screen.bgpic("game.png")
    scr_turtle.penup()
    tracer(0)
    scr_turtle.goto(0, 160)
    scr_turtle.write(arg="Welcome to Snake.io", align="center", font=('Verdana', 20, 'normal'))
    scr_turtle.goto(0, -180)
    scr_turtle.write(arg="Created by Shivam Rastogi", align="center", font=('Verdana', 10, 'normal'))
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
        scoreboard.high_score(high_scr)
        screen.update()
        time.sleep(0.1)

        if snake.snake_head.distance(food.position()) < 20:
            snake.create_body()
            food.food_posit()
            count += 1
            scoreboard.score(count)
            scoreboard.high_score(high_scr)

        # Detecting collision with wall.
        if x >= 250 or x <= -250 or y >= 250 or y <= -250:
            game_is_on = False
            clearscreen()
            scoreboard.game_over(count, high_scr)

        # Detecting collision with itself.
        for i in snake.snake_body[1:]:
            if i.distance(x, y) < 5:
                game_is_on = False
                clearscreen()
                scoreboard.game_over(count, high_scr)
    time.sleep(2)
    return count


game = True
while game:
    screen = Screen()
    screen.clear()
    init()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    try:
        file = open("scr_tracker.bin", "rb")
        file.seek(0)
        a = pickle.load(file)
        file.close()
        high_scr = int(a[0])
    except FileNotFoundError:
        # If the Game is being played for the first time, the high score will be zero.
        file = open("scr_tracker.bin", "wb")
        data = [0]
        pickle.dump(data, file)
        high_scr = 0
        file.close()

    if decision == "Yes":
        update()
        variable = game_setup()
        print(a, variable)
        if a[0] < variable:
            a = [variable]
            file = open("scr_tracker.bin", "wb")
            pickle.dump(a, file)
            file.close()
    else:
        game = False
        # I tried using bye(), but it raissed Turtle Terminator error, so I used sys.exit(), at that time I also had written game_is = False,maybe that was the error.
        sys.exit()


