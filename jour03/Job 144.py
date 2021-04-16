# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:14:06 2021

@author: Gilles
"""

"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
import unicodedata # pour enlever les accents
"""

l = int(input('Entre la largeur du damier : '))
print()
damier = ''
tabDamier = []
for i in range(int(l)) :
    tabDamier = []
    for j in range(int(l)) :
        damier = damier + "O "
        tabDamier.append("O")
    damier = damier + "\n"
    
print (damier)

longueurDamier = len(damier)

tabDirections = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]

def placeDame(damier,nbDamesPlacees,tabPosDePriseDerniereDamePlacee) :
    
    if nbDamesPlacees == int(l) :
        print(damier)
        return


    peuPlacerDame = False
    placeCar = 0
    for i in damier :
        if i == "O" :
            peuPlacerDame = True
            #print(i)
            damierBis = damier[:placeCar] + "X" + damier[placeCar+1:]
            
            tabPosDePriseDerniereDamePlaceeBis = [placeCar]
            j = 1
            position = placeCar
            for direction in tabDirections :
                while position >= 0 and position < longueurDamier:
                    print(position)
                    print(direction[0],direction[1],j)
                    print(placeCar,damierBis[position])
                    print(damierBis)
                    if damierBis[position] == "O" :
                        damierBis = damierBis[:position] + "-" + damierBis[position+1:]
                        print(damierBis)
                        tabPosDePriseDerniereDamePlacee.append(position)
                    position = position + j*direction[0]*2 + j*direction[1]*(2*l)
                    
                    j=j+1
            #print(nbDamesPlacees+1)
            #print(damierBis)
            placeDame(damierBis, nbDamesPlacees+1,tabPosDePriseDerniereDamePlaceeBis)
        placeCar = placeCar + 1
    if not peuPlacerDame : 
        if tabPosDePriseDerniereDamePlacee != [] :
            for i in tabPosDePriseDerniereDamePlacee :
                damier = damier[:i] + "O" + damier[i+1 :]
        return

placeDame(damier,0,[])

