#virus
import turtle
turtle.bgcolor("black")
turtle.speed(0)
turtle.penup()
turtle.goto((300,60))
turtle.pendown()
turtle.color("cyan")
b=200
while b>0:
    turtle.left(b)
    turtle.forward(b*3)
    b=b-1
turtle.done()