from turtle import*
tracer(0)
koef=6
for q in range(9):
    forward(50* koef)
    right(90)
    forward(35* koef)
    right(90)
up()
forward(5* koef)
right(90)
forward(10*koef)
right(90)
down()
for q in range(4):
    forward(35* koef)
    right(90)
    forward(17*koef)
    right(90)
up()
for x in range(- koef*11,koef*11):
    for y in range(-koef*11,koef*11):
        goto(x*koef,y*koef)
        dot(3)
exitonclick()