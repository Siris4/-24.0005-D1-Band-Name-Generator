# Import the Reeborg library

#Basically: if there's not a wall on the right, take that first right you can, if not right, then straight. If not right or straight,
#then turn left and repeat all the above. Once at goal, pass to end!!

# Your defined functions (leave them untouched)
def keep_right():
    if not wall_on_right():
        turn_right()
        move()
        while wall_on_right() and front_is_clear():
            move()
    else:
        turn_left()
        keep_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Your defined functions end here

# Call your defined functions to navigate the maze


# Stop on the checkered flag
while not at_goal():       #this part by AI. The rest was all me!
    keep_right()
pass
