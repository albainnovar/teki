from __future__ import division
from turtle import Turtle
import random


def koch(teki, length=800, limit=9):
    if length < limit:
        teki.forward(length)
        return
    newlength = length/3
    teki.width(limit/3)
    koch(teki, newlength)
    teki.right(60)
    koch(teki, newlength)
    teki.left(120)
    koch(teki, newlength)
    teki.right(60)
    koch(teki, newlength)

def full_koch(teki, length=650):    
    for i in range(3):
        koch(teki, length)
        lali.left(120)

def square_koch(teki, length=800, limit=9):
    if length < limit:
        teki.forward(length)
        return
    teki.width(limit/4)
    newlength = length/3
    other_length = newlength/(1.2 + random.random())
    square_koch(teki, newlength)
    teki.right(90)
    square_koch(teki, other_length)
    teki.left(90)
    square_koch(teki, newlength)
    teki.left(90)
    square_koch(teki, other_length)
    teki.right(90)
    square_koch(teki, newlength)


def full_square_koch(teki, length=400):    
    for i in range(4):
        square_koch(teki, length)
        lali.left(90)

length = 300
lali = Turtle()
lali.hideturtle()
lali.speed(0)
lali.color("darkgreen")
lali.fillcolor("green")

lali.penup()
lali.backward(length/2)
lali.left(90)
lali.backward(length/4)
lali.right(90)
lali.pendown()

lali.fill(True)
full_square_koch(lali, length=length)
lali.fill(False)
