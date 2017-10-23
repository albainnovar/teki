# coding: utf-8
"""
Alapfüggvények importálása
"""

from turtle import Turtle
from random import choice, random

szinek = "red green blue cyan yellow magenta black orange brown".split()


def haza(turtle):
    isdown = turtle.isdown()
    turtle.up()
    turtle.home()
    if isdown:
        turtle.down()


Turtle.haza = haza


def veletlen_szin():
    return choice(szinek)


def veletlen_szint_beallit(teki):
    teki.color(veletlen_szin())

Turtle.veletlen_szint_beallit = veletlen_szint_beallit
