#spiral helix
import turtle
import colorsys

turtle.bgcolor('black')
turtle.speed(0)
n=500
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    turtle.color(c)
    for j in range(2):
        turtle.left(250)
        turtle.forward(i*1.5)
turtle.done()