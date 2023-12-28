def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6             #these 4 lines shows how to use a While Loop
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
        print(number_of_hurdles)