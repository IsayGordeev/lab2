from math import sqrt
from turtle import *

# global variable
step_num = 50
side_num = 40
speed(100)
num = [0] * 10
num = [[[0, 0]] for i in range(10)]

inp = open('font')


def read_font(a):
    s = inp.readline().rstrip()
    for item in s.split():
        leng, ang = item.split(',')
        if leng == 'side_num':
            leng = side_num
        num[a].append((float(leng), float(ang)))


for i in range(10):
    read_font(i)


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
