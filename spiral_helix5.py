#spiral helix
import turtle


def square(x):
    for j in range(4):
        turtle.forward(x)
        turtle.left(90)


def square2(x):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.left(10)
    turtle.forward(x/2)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(x/2)
    for i in range(3):
        turtle.left(90)
        turtle.forward(x)
    turtle.left(90)
    turtle.forward(x/2)
    turtle.right(90)


turtle.bgcolor("black")
turtle.speed(0)
turtle.color("yellow")
turtle.width(2)
for i in range(38):
    square(250)
    turtle.left(10)

distance = [i*5 for i in range(80)]
turtle.color("purple")
for i in distance:
    square2(i)


turtle.done()

