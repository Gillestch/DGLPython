# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:40:03 2021

@author: Gilles


print(10 + 3)
def add(a,b):
    print (a+b)
add(10,3)
add(456,0.25)
add("a",'b')
add("d","1")

def hello():
    pseudo = input("Tape ton pseudo : ")
    print("Hello "+ pseudo+" !")
hello()

listeNb=[]
for i in range(5):
    nb = input("Cher utilisateur, entres un nombre : ")
    listeNb.append(nb)
print (sorted(listeNb))


for i in range(1,101):
    if (i%15 == 0) :
        print("FizzBuzz")
    elif (i%3 == 0) :
        print("Fizz")
    elif (i%5 == 0) :
        print("Buzz")
    else :
        print(i)
        



def traceRect(x,y):
    lignes = ""
    for i in range(x):
        lignes = lignes + "|"
        for j in range(y):
            if ((j==0 or j==y-1)):
                lignes = lignes + "-"
            else :
                lignes = lignes + " "
        lignes = lignes + "|\n"
    print(lignes)
traceRect(30,4)



def traceTri(h):
    print("Triangle tracé de hauteur %1 avec des \\ et des / puis des _",h)
traceTri(5)



ln=[3,37,100]
def arrondir(i):
    if (i%5>=2): return i+5-i%5
    else : return i
def arrondi(ln):
    for i in range(len(ln)) :
        ln[i]=arrondir(ln[i])
    return ln
print(arrondi(ln))



import re
def PermutPlusProch(mot):
    return re.findall(r"(?=([a-z]))+",mot)
mot=input("Entres un mot dont les lettres sont dans le range a->z : ")
print(PermutPlusProch(mot))

"""

import pygame
#import torch
from pygame.locals import *
pygame.init()
color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red
DISPLAYSURF = pygame.display.set_mode((300,300))
pygame.draw.circle(DISPLAYSURF, color1, (200,50), 30)
