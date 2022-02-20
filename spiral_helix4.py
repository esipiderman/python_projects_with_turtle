#spiral helix
import turtle


def square(x):
    for j in range(4):
        turtle.forward(x)
        turtle.left(90)


turtle.bgcolor("black")
turtle.speed(0)
turtle.color("yellow")
turtle.width(2)
for i in range(38):
    square(110)
    turtle.left(10)

turtle.color("purple")
for i in range(100):
    square(i)
    turtle.left(10)


turtle.done()

