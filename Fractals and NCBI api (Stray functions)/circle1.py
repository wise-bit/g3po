import turtle


b = input("Turtle size? ")
a = turtle.Turtle()
a.speed(0)
a.hideturtle()


def set_position():
	a.penup()
	a.forward(0)  # moding it right
	a.left(90)
	a.forward(old_r - radius)  # moving it up
	a.right(90)
	a.pendown()

def iter_circle(radius, old_r):
	a.penup()
	a.forward(0)  # moding it right
	a.left(90)
	a.forward(old_r - radius)  # moving it up
	a.right(90)
	a.pendown()
	a.circle(radius)
	if radius > 2:
		old_r = radius
		radius *= 0.75
		iter_circle(radius, old_r)
		turtle.update()

iter_circle(b*0.75, b)
turtle.exitonclick()
