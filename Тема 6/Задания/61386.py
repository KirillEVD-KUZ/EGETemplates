from turtle import*
koef=20
tracer(0)


up()
for x in range(-koef,koef):
    for y in range (-koef,koef):
        goto(x*koef,y*koef)
        dot(3)
exitonclick()

