from turtle import *

colors = [
    "medium violet red",
    "deep pink",
    "light sea green",
    "teal",
    "gold",
    "peach puff",
]

pen()
speed(0)
bgcolor("slate gray")
penup()
goto(50, 40)
pendown()

i = 0
while i < 360:
    for j in range(len(colors)):
        pencolor(colors[j])
        width(i / 100 + 1)
        forward(i)
        left(59)
        i += 1
done()
