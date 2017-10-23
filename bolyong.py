from teki import *
import random


lali = Teki()
lali.speed(0)


def lepes_kis_kanyarral(hossz=20, teki=lali):
    teki.forward(hossz)
    szog = random.random() * 90 - 45  # -45 és +45 fok között véletlen szög
    teki.right(szog)


def meroleges_lepes(hossz=20, teki=lali):
    teki.forward(hossz)
    irany = random.choice([teki.right, teki.left])
    irany(90)


def bolyong_adott_lepest(lepes=20, teki=lali):
    szin = random.choice(szinek)
    teki.color(szin)
    for i in range(lepes):
        meroleges_lepes(15, teki)
    tavolsag = distance(0, 0)
    haza(teki)
    return tavolsag


def sokbolyongas_elmozdulas(bolyongasszam=20, lepesszam=15, teki=lali):
    elmozdulasok = []
    for i in range(bolyongasszam):
        elmozdulas = bolyong_adott_lepest(lepesszam, teki)
        elmozdulasok.append(elmozdulas)
    return elmozdulasok


def bolyong_adott_tavolsagig(tavolsag, teki=lali):
    szin = random.choice(szinek)
    teki.color(szin)
    lepesszam = 0
    while distance(0, 0) < tavolsag:
        lepesszam = lepesszam + 1
        lepes2(15)
    haza(teki)
    return lepesszam


def sokbolyongas_lepesszam(bolyongasszam=20, tavolsag=150, teki=lali):
    lepesszamok = []
    for i in range(bolyongasszam):
        lepesszam = bolyong_adott_tavolsagig(tavolsag, teki)
        lepesszamok.append(lepesszam)
