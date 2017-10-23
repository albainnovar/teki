import turtle
toll=turtle.Turtle()
import random

szin=random.choice(["brown","red","purple","green","blue","black"])

def minta(oldalhossz):
    toll.left(90)
    toll.forward(oldalhossz*3)
    toll.right(90)
    toll.forward(oldalhossz*2)
    toll.right(90)
    toll.forward(oldalhossz)
    toll.right(90)
    toll.forward(oldalhossz)
    toll.left(90)
    toll.forward(oldalhossz*2)
    toll.left(90)
    toll.forward(oldalhossz*2)

def ogorog(oldalhossz,darab):
    for i in range(darab):
        szin=random.choice(["brown","red","purple","green","blue","black"])
        toll.color(szin)
        minta(oldalhossz)

ogorog(15,5)
