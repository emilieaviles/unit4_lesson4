from turtle import *

laser_sword = Turtle()

laser_sword.color("cyan")
laser_sword.pensize(5)
laser_sword.shape("circle")
laser_sword.speed(6)


for x in range(6):
	laser_sword.forward(50)
	laser_sword.left(60)

mainloop()