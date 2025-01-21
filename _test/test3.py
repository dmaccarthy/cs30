"""
This program checks if the 'Turtle Graphics' module is working.

"""

from turtle import setup, speed, pencolor, penup, pendown, left, forward, backward, exitonclick

# Set the canvas size, turtle speed, and pen color
setup(600, 480)
speed(1)
pencolor("red")

# Move turtle into position
penup()
backward(120)
left(60)

# Draw a hexagon
pendown()
for side in range(6):
    forward(120)
    left(-60)

# Finished!
exitonclick()
