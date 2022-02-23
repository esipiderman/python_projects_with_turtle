import turtle

turtle.pensize(2)
turtle.speed(0)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.fillcolor("red")
turtle.begin_fill()
turtle.left(140)
turtle.forward(113)
curve()
turtle.left(120)
curve()
turtle.forward(112)
turtle.end_fill()

turtle.done()