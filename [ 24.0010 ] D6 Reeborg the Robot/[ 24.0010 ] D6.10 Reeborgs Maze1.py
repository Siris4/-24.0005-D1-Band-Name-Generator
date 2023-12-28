def jump_over_hurdle():
    while wall_in_front():
        turn_left()
        if wall_in_front():
            jump_over_hurdle()
    else:
        move()
        turn_right()
        while not wall_in_front():
            move()
            turn_right()
            if wall_on_right() and not wall_in_front():
                move()
        else:
            turn_left()
            while front_is_clear():
                move()
                turn_right()
                while front_is_clear():
                    move()
                jump_over_hurdle()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# def U-turn():
#    turn_left()
#    turn_left()
#    move()


while not at_goal():
    while front_is_clear():
        move()
    jump_over_hurdle()
    if at_goal():
        done()
        pause()
