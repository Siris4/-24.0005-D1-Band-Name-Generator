def turn_left():
	pass

def wall_in_front():
	pass

def move():
	pass

def turn_right():
	turn_left()
	turn_left()
	turn_left()

def jump_over_hurdle():
	turn_left()
	move()
	turn_right()
	move()
	turn_right()
	move()
	turn_left()

while not at_goal():    #The bigger goal is to reach the goal. Keep going til there.
	if wall_in_front():    #while not at goal yet, if wall in front, jump over it!
		jump_over_hurdle()
	else:
		move()              #otherwise, the ONLY thing left to do is just to move foward