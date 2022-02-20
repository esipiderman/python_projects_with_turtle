#flower
import turtle

draw=turtle.Turtle()

draw.color("red","yellow")
draw.speed(10)
draw.begin_fill()
for i in range(36):
    draw.forward(150)
    draw.left(170)
draw.end_fill()

turtle.done()
