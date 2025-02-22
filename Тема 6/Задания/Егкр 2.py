from turtle import *
tracer(0)
koef= 10

for i in range (3):
    forward(20 * koef )
    right(90)
    forward(4 * koef )
    right(90)

for i in range (2):
    forward(6 * koef )
    right(90)
    forward(13 * koef)
    right(90)
up()
for x in range(- koef* 3, koef*3):
    for y in range(-koef * 3, koef* 3):
        goto(x * koef, y* koef )
        dot(3)
exitonclick()