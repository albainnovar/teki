from teki import *

speed(4)


def tortvonal(darab, szog, hossz=120):
    for i in range(darab):
        color(veletlen_szin())
        forward(hossz)
        right(szog)


def csillag5():
    color("blue")
    tortvonal(5, 144, 130)
    # Ez az alábbival egyenértékű:
    # for i in range(5):
    #     forward(130)
    #     right(144)  # 180-36 = 144
