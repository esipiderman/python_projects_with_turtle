#virus
import turtle

a=0
b=0
turtle.title('corona')
turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("green")
turtle.penup()
turtle.goto(0,75)#200
turtle.pendown()

for i in range(1100):
    turtle.forward(a)
    turtle.right(b)
    #a+=3
    a+=0.5
    #b+=1
    b+=0.3

turtle.done()