import imp


import turtle as t

t.bgcolor("black")
t.pencolor("white")
t.speed(0)
t.hideturtle()

for i in range(150):
    for j in range(6):
        t.forward(i)
        t.left(46)
    t.left(33)

t.done()
