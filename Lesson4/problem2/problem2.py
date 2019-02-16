from turtle import *

porg = Turtle()

porg.shape("circle")
porg.color("dark slate gray")
porg.speed(6)
porg.pensize(10)

for x in range(4):
	porg.forward(300)
	porg.right(90)

mainloop()
