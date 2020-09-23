from random import *
from turtle import *

# global variables
time = 100
number_of_turtles = 30
a = 200
speedmax = 20


def drawborder():
    penup()
    speed(100000)
    goto(-a, -a)
    pendown()
    goto(-a, a)
    goto(a, a)
    goto(a, -a)
    goto(-a, -a)


drawborder()

pool = [Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-a, a), randint(-a, a))
    unit.speed(randint(1, speedmax))
    unit.setheading(randint(0, 360))

for tick in range(time):
    for unit in pool:
        if abs(unit.xcor()) > a:
            unit.setheading(180 - unit.heading())
        if abs(unit.ycor()) > a:
            unit.setheading(180 - (unit.heading()-180))
        unit.forward(unit.speed() * 0.5)
