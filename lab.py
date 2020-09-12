import math
import turtle

import numpy as np

turtle.shape('turtle')

# 3
# for step in range(4):
#     turtle.left(90)
#     turtle.forward(100)
#
# 4
# for step in range(100):
#     turtle.left(1)
#     turtle.forward(2)
#
# 5
# x = 20
# for step1 in range(10):
#     for step in range(4):
#                 turtle.forward(x)
#                 turtle.left(90)
#     turtle.penup()
#     turtle.backward(10)
#     turtle.right(90)
#     turtle.forward(10)
#     turtle.left(90)
#     turtle.pendown()
#     x += 20
# 6
# for step in range(12):
#     turtle.right(30)
#     turtle.forward(100)
#     turtle.stamp()
#     turtle.right(180)
#     turtle.forward(100)
#     turtle.left(180)
# 7
# #
# k = 0.1
# phi = 0.1
# convert_rot = phi * (180 / 3.14)
# for i in range(1000):
#     ro = k * phi
#     turtle.forward(ro)
#     turtle.left(convert_rot)
#     phi += 0.1
#     ro += ro
# 8
# y = 10
# for step in range(1000):
#     turtle.left(90)
#     turtle.forward(y)
#     y+= 6
# # 9
# def mnogoug(num: int):
#     a = (50 + (num-3)*30) * 2 * math.sin(math.pi / ( (num)))
#     turtle.left(180 - (180 * (num - 2)) / (num * 2))
#     for step in range(num):
#         turtle.forward(a)
#         turtle.left(360 / num)
#     turtle.right(180 - (180 * (num - 2)) / (num * 2))
#     turtle.penup()
#     turtle.forward(30)
#     turtle.pendown()
#
# for step in range(3,20):
#     mnogoug(step)
# # 10
# def circles():
#     for step in range(360):
#         turtle.left(1)
#         turtle.forward(1)
#     for step in range(360):
#         turtle.right(1)
#         turtle.forward(1)
# turtle.speed(10000000000)
# for ang in range(3):
#     circles()
#     turtle.left(60)
# 11
#
# def circles(x):
#     for step in range(360):
#         turtle.left(1)
#         turtle.forward(x)
#     for step in range(360):
#         turtle.right(1)
#         turtle.forward(x)
#
#
#
# turtle.left(90)
# for radius in np.arange(1,2,0.1):
#     circles(radius)
# 12
# def circlesr(x):
#     for step in range(50):
#         turtle.right(3.6)
#         turtle.forward(x)
#
# turtle.left(90)
# for it in range(3):
#     circlesr(5)
#     circlesr(0.75)
#
# 13
def circle1(x):
    for step in range(360):
        turtle.right(1)
        turtle.forward(x)
def gotowithout(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
def cemicircle1(x):
    for step in range(180):
        turtle.right(1)
        turtle.forward(x)
turtle.speed(2**1000000)
turtle.begin_fill()
turtle.color("yellow")
circle1(2)
turtle.end_fill()
gotowithout(-50,-50)
turtle.begin_fill()
turtle.color("blue")
circle1(0.3)
turtle.end_fill()
gotowithout(50,-50)
turtle.begin_fill()
turtle.color("blue")
circle1(0.3)
turtle.end_fill()
gotowithout(0,-90)
turtle.begin_fill()
turtle.color("brown")
turtle.width(10)
turtle.goto(0,-130)
turtle.end_fill()
gotowithout(60,-140)
turtle.color("red")
turtle.width(10)
turtle.right(90)
cemicircle1(1)
turtle.exitonclick()
# 14
# def peak(n:int):
#     for step in range(1):
#         turtle.left(180-360/(2*n))
#         turtle.forward(200)
#
# for step in range(11):
#     peak(11)
# # turtle.penup()
# # turtle.goto(200,200)
# # turtle.pendown()
# for step in range(5):
#     peak(5)
# turtle.exitonclick()