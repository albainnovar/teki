from turtle import Turtle
from time import sleep
from random import random, randint
pista = Turtle()

pista.penup()
pista.backward(50)
pista.left(90)
pista.forward(30)
pista.right(90)

pista.pendown()
for i in range(4):
    pista.forward(100)
    pista.right(90)

pista.left(45)
pista.forward(70)
pista.right(90)
pista.forward(70)
pista.penup()

pista.home()

pista.pendown()
pista.speed(0)
pista.write("KOCSMA", False, align="center", font=("Arial", 8, "normal"))
sleep(1.5)

pista.color("red")

for i in range(1000):
    pista.right(randint(1, 100))
    pista.forward(randint(1, 20))
    pista.speed(randint(5, 9))




