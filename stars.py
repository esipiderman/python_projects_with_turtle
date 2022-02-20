#srtars
import turtle

turtle.bgcolor('black')
turtle.speed(9)
color=['yellow','blue','white','green']
for i in range(50):
    turtle.forward(i*10)
    turtle.right(144)
    turtle.color(color[i%4])
turtle.done()