from turtle import*
koef = 10
tracer()


for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot()
exitonclick()
