def move():
	pass

def turn_left():
	turn_right()
	turn_right()
	turn_right()

def turn_right():
	turn_left()
	turn_left()
	turn_left()

def jump_over_hurdle():
	move()
	turn_left()
	move()
	turn_right()
	move()
	turn_right()
	move()
	turn_left()

#to prove if this statement is True or False, test it against it's negation
while not at_goal():   #"while not at goal", keep running this code block
	jump_over_hurdle()     #below in indents
