import turtle


t = turtle.Turtle()


def cantor_loop(length, current_loop_number):
	t.penup()
	t.setposition(0, current_loop_number)
	t.pendown()
	for i in range(int(current_loop_number*3/10)):
		t.forward(length)
		if t.isdown():
			t.penup()
		else:
			t.pendown()
	if current_loop_number == 1:
		current_loop_number += 9
	else:
		current_loop_number += 10
	length *= 0.3
	if length > 2:
		cantor_loop(length, current_loop_number)

cantor_loop(100, 1)
turtle.exitonclick()
