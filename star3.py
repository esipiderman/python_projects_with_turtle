import turtle as t

t.bgcolor("black")
t.pensize(2)
t.speed(0)
colors=['red', 'yellow', 'blue', 'purple', 'green', 'pink', 'black', 'white']

distance=170
t.hideturtle()

for color in colors:
    t.color(color)
    for j in range(8):
        t.left(45)
        for i in range(2):
            t.forward(distance)
            t.left(60)
            t.forward(distance)
            t.left(120)

t.done()