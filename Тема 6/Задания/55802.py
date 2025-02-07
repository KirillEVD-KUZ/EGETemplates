from turtle import*
tracer (0)
koef=10

right(315)
for i in range (7):
    forward(16 *koef)
    right(45)
    forward(8 * koef)
    right(135)

up()
for x in range (- koef*2, koef*2):
    for y in range(-koef *2, koef *2):
        goto(x *koef, y * koef)
        dot(3)
exitonclick()