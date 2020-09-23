from math import sqrt
from turtle import *

# global variable
step_num = 50
side_num = 40
speed(100)
num = [0] * 10

num[0] = [(2 * side_num, 90), (side_num, 90), (2 * side_num, 90), (side_num, 0)]
num[1] = [(2 * side_num, 180), (2 * side_num, -135), (side_num * sqrt(2), 180), (side_num * sqrt(2), 45)]
num[2] = [(side_num, 45), (side_num * sqrt(2), -135), (side_num, 180), (side_num, 135), (side_num * sqrt(2), -45),
          (side_num, -90), (side_num, 180), (side_num, 0)]
num[3] = [(0, 45), (side_num * sqrt(2), -135), (side_num, 135), (side_num * sqrt(2), 180), (side_num * sqrt(2), -135),
          (side_num, 135), (side_num * sqrt(2), -135), (side_num, 180), (side_num, 0)]
num[4] = [(2 * side_num, 180), (side_num, -90), (side_num, 90), (side_num, 180), (side_num, -90), (side_num, -90),
          (side_num, 90)]
num[5] = [(0, 90), (side_num, -90), (side_num, -90), (side_num, 90), (side_num, 90), (side_num, 180), (side_num, -90),
          (side_num, -90), (side_num, 90), (side_num, 90), (side_num, 0)]
num[6] = [(0, 45), (side_num * sqrt(2), -45), (side_num, -90), (side_num, -90), (side_num, -90), (side_num, 135),
          (side_num * sqrt(2), 45)]
num[7] = [(0, 45), (side_num * sqrt(2), -45), (side_num, 180), (side_num, 45), (side_num * sqrt(2), -135),
          (side_num, 180), (side_num, 0)]
num[8] = [(2 * side_num, 90), (side_num, 90), (2 * side_num, 90), (side_num, 90), (side_num, 90), (side_num, 90),
          (side_num, 90), (side_num, 0)]
num[9] = [(side_num, 45), (side_num * sqrt(2), 180), (side_num * sqrt(2), -135), (side_num, 90), (side_num, 90),
          (side_num, 0)]


def nd(digit):
    for leng, ang in num[digit]:
        forward(leng)
        right(ang)

def step_digit():
    penup()
    forward(step_num)
    setheading(-90)
    pendown()

def dn(index):
    for nums in index:
        nd(int(nums))
        step_digit()


setheading(-90)
dn('141700')
