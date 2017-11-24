# coding: utf-8                   # Python 2.x-hez kell
from __future__ import division  # Python 2.x-hez kell

from turtle import Turtle

from negyzetracs_alap import negyzetracs

lali = Turtle("turtle")
negyzetracs(33, 4, 2, lali)

from modul_es_osztaly.myturtle_alap import MyTurtle
from modul_es_osztaly.veletlenszin import veletlenszin
ili = MyTurtle("turtle")
ili.color(veletlenszin())
ili.negyzet(70)

from time import sleep
sleep(5)


