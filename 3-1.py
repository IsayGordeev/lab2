from random import *
import turtle

for step in range(1000):
    turtle.forward(10 * random())
    if random() > 0.5:
        turtle.left(randint(0, 90))
    else:
        turtle.right(randint(0, 90))
