from turtle import*
tracer(0)
koef =10

for i in range(777):
    forward(25 * koef)
    left(90)
    forward(34 * koef)
    left(90)
up()

forward(12 * koef)
left(90)
forward(17 * koef)
right(90)

down()
for i in range(1996):
    forward(25 * koef)
    left(90)
    forward(17 * koef)
    left(90)

up()
for x in range(- koef *3, koef*3):
    for y in range(- koef*3, koef *3):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()

print(13 * 17)