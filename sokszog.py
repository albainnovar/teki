from teki import *


def sokszog(oldalszam, oldalhossz):
    for i in range(oldalszam):
        forward(oldalhossz)
        right(360/oldalszam)


def negyzet(oldalhossz):
    sokszog(4, oldalhossz)
