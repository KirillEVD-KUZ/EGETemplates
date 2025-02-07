from turtle import*
tracer(0)
koef=20

for i in range (2):
    forward(9 * koef)
    right(90)
    forward(15 * koef)
    right(90)
up()
forward(12 * koef)
right(90)
down()

for i in range (2):
    forward(6 * koef)
    right(90)
    forward(12 * koef)
    right(90)

up()
for x in range(-koef, koef):
    for y in range (- koef, koef):
        goto(x * koef, y *koef)
        dot(3)
exitonclick()