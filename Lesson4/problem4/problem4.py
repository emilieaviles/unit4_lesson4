from turtle import *

squidward = Turtle()

squidward.color("pale turquoise")
squidward.shape("circle")
squidward.pensize(4)
squidward.speed(6)

squidward.circle(30)

spongebob = Turtle()

spongebob.color("yellow")
spongebob.pensize(4)
spongebob.speed(6)
spongebob.shape("square")

for x in range(3):
	spongebob.forward(70)
	spongebob.right(120)

mainloop()