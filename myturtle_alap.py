# coding: utf-8                   # Python 2-höz kell
from __future__ import division   # Python 2-höz kell
from turtle import Turtle

class MyTurtle(Turtle):

    def negyzet(self, oldalhossz):
        for i in range(4):
            self.forward(oldalhossz)
            self.right(90)


def sokszog(self, oldalszam, oldalhossz):
    for i in range(oldalszam):
        self.forward(oldalhossz)
        self.right(360 / oldalszam)


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


if __name__ == "__main__":
    lali = MyTurtle("turtle")
    lali.speed(0)
    lali.hideturtle()

    lali.negyzet(42)
    # lali.sokszog(8, 77)
    # lali.negyzetsor(44, 5)

    lali.write("Kész")    # Python2-ben ehhez karakterkódolást tudnia kell (első sor)

    from time import sleep
    sleep(5)

