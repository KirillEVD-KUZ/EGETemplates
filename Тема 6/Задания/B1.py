from turtle import*
tracer(0)
koef=10

for i in range(5):
    forward(15*koef)
    right(90)
    forward(15*koef)
    right(90)
up()
forward(9* koef)
right(90)
forward(5 * koef)
left(90)
down()
for i in range(5):
    forward(34*koef)
    right(90)
    forward(34*koef)
    right(90)
up()
for x in range(-koef,koef):
    for y in range(-koef, koef):
        goto(x* koef, y * koef)
        dot(3)
exitonclick()