from turtle import*
tracer(0)
koef=10

for i in range(2):
    forward(10*koef)
    right(90)
    forward(20*koef)
    right(90)
up()
backward(4*koef)
right(90)
forward(7*koef)
left(90)
down()
for q in range(4):
    forward(8*koef)
    left(90)
    forward(12*koef)
    left(90)
up()
forward(10*koef)
down()
for l in range(4):
    forward(12*koef)
    right(90)
up()
for x in range(-koef*5,koef*5):
    for y in range(-koef*5,koef*5):
        goto(x*koef, y*koef)
        dot(3)
exitonclick()