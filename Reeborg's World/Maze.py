def turn_right():
    turn_left()
    turn_left()
    turn_left()

while True:
    if at_goal():
        break
    elif wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
