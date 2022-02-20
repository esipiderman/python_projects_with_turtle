#stars in stars in stars
import turtle

draw = turtle.Turtle()
def star(turtle,size):
    if size<=10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)

draw.penup()
draw.goto((-200,70))
draw.pendown()

screen=turtle.Screen()
screen.bgcolor("cyan")
draw.speed(10)
star(draw,360)

turtle.done()