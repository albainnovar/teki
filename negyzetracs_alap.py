# coding: utf-8
from __future__ import division   # Python 2.x-hez kell
from turtle import Turtle
from veletlenszin import veletlenszin


def sokszog(oldalszam, oldalhossz, teki):
    for i in range(oldalszam):
        teki.forward(oldalhossz)
        teki.right(360/oldalszam)


def negyzetsor(oldalhossz, darab, teki):
    for i in range(darab):
        sokszog(4, oldalhossz, teki)
        teki.forward(oldalhossz)


def negyzetracs(oldalhossz, oszlop, sor, teki):
    for s in range(sor):
        teki.color(veletlenszin())
        negyzetsor(oldalhossz, oszlop, teki)
        teki.backward(oldalhossz*oszlop)
        teki.right(90)
        teki.forward(oldalhossz+1)
        teki.left(90)


from random import choice, random

szinek = "red green blue cyan yellow magenta black orange brown".split()

def veletlenszin():
    return choice(szinek)


if __name__ == "__main__":
    lali = Turtle("turtle")
    lali.speed(0)
    lali.hideturtle()

    negyzetracs(12, oszlop=8, sor=4, teki=lali)

    from time import sleep
    lali.showturtle()
    lali.write("Kész")
    sleep(5)
