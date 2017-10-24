from teki import *

lali = Turtle()

def sokszog(oldalszam, oldalhossz, teki=lali):
    for i in range(oldalszam):
        teki.forward(oldalhossz)
        teki.right(360/oldalszam)


def negyzet(oldalhossz, teki=lali):
    sokszog(4, oldalhossz, teki=teki)
