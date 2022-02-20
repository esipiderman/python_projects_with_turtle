#spiral helix
import turtle

w=turtle.Screen()
w.title('spiral helix')
w.bgcolor('blue')#black

colors =["black","white"]
#'red','purple','blue','green','orange','yellow','white'
t=turtle.Pen()
t.speed(0)

for x in range(362):
    color=colors[x % len(colors)]
    t.pencolor(color)
    t.width(x / 100 +1)
    t.forward(x)
    t.right(59)

turtle.done()