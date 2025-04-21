from turtle import*
tracer(0)
koef=20

right(30)
for q in range(3):
    right(150)
    forward(6*koef)
    right(30)
    forward(12*koef)
up()
for x in range(-koef*5,koef*5):
    for y in range(-koef * 5, koef * 5):
        goto(x*koef,y*koef)
        dot(3)
exitonclick()