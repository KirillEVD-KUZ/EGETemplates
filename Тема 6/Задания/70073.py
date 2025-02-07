from turtle import*
koef=10
tracer(0)
screensize(400,400)

for i in range (9):
    forward(29 *koef)
    right(90)
    forward(17 * koef)
    right(90)
up()
forward(5 * koef)
right(90)
forward(1 * koef)
left(90)
down()
for i in range (9):
    forward(64 * koef)
    right(90)
    forward(48 * koef)
    right(90)

up()
for x in range (-koef,koef):
    for y in range (-koef,koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()