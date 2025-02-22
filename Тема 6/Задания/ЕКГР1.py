from turtle import *
tracer(0)
koef=10

for i in range(3):
    forward(19 * koef)
    right(90)
    forward(3 * koef)
    right(90)
for i in range(3):
    forward(5 * koef)
    right(90)
    forward(11 * koef)
    right(90)

up()
for x in range (-koef*4, koef*4):
    for y in range(- koef*4, koef*4):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()