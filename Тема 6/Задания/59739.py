from turtle import *

tracer(0)
koef = 20

x = 4
forward((x + 2) * koef)
for i in range(4):
    forward(x * koef)
    right(90)
    forward((x + 2) * koef)
right(90)
forward(2 * x * koef)
for i in range(4):
    right(90)
    forward(((3 * x) - 1) * koef)

up()
for i in range(-koef, koef):
    for y in range(-koef, koef):
        goto(i * koef, y * koef)
        dot(3)
exitonclick()

for q in range(1, 100):
    s = ((q + 2 + q) ** 2) + ((3 * q - 1) ** 2) - ((q + 2) * (q * 2))
    print(q, s)