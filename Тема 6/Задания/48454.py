from turtle import*
tracer(0)
koef = 10

for i in range(9):
    forward(18 * koef)
    right(72)

up()
for x in range (- koef *5, koef*5):
    for y in range (- koef *5, koef*5):
        goto(x*koef, y * koef)
        dot(3)
exitonclick()