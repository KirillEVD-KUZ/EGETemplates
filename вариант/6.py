from turtle import*
tracer(0)
koef=10

for i in range(4):
    forward(36* koef)
    right(90)
    forward(41*koef)
    right(90)
up()
right(90)
forward(20* koef)
left(90)
forward(20* koef)
down()
for y in range(4):
    forward(25* koef)
    right(90)
up()
forward(7 *koef)
left(90)
forward(7 * koef)
right(90)
down()
for p in range(7):
    forward(16 * koef)
    right(90)
up()
for x in range(-koef*5,koef*5):
    for y in range(- koef*5,koef*5):
        goto(x* koef,y* koef)
        dot(3)
exitonclick()