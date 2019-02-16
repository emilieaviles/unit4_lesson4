from turtle import *

bob = Turtle()
screen = Screen()

screen.bgcolor("black")

bob.shape("arrow")
bob.pensize(2)
bob.speed(6)

for x in range(30):
	bob.color("red")
	bob.forward(20)
	bob.left(10)
	bob.color("white")

	for x in range(5):
		bob.forward(150)
		bob.right(90)

mainloop()