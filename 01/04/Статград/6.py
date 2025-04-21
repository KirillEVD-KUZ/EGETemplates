from turtle import*
tracer(0)
koef=10

right(270)
for i in range(2):
    forward(8*koef)
    right(120)
right(120)
for i in range(2):
    right(120)
    forward(3*koef)
    right(240)
right(240)
for i in range(2):
    forward(14*koef)
    right(120)
up()
for x in range(- koef*5,koef*5):
    for y in range(-koef*5,koef*5):
        goto(x*koef,y*koef)
        dot(3)
exitonclick()