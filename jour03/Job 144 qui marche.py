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

l = int(input('Entre la largeur du tabDamier : '))
print()

tabDamier = []
for i in range(int(l)) :
    tabDamier.append([])
    for j in range(int(l)) :
        tabDamier[i].append("O")
#tabDamierBis = tabDamier

def tostrDamier(tabDamier) :
    strDamier = ''
    for i in range(len(tabDamier)) :
        for j in range(len(tabDamier)) :
            strDamier = strDamier + tabDamier[i][j]+' '
        if i<len(tabDamier) : strDamier = strDamier + "\n"
    return strDamier

print (toStr(tabDamier))

tabDirections = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]

def placeDame(tabDamierBis,nbDamesPlacees,tabPosDePriseDerniereDamePlacee) :
    
    if nbDamesPlacees == l :
        print (toStr(tabDamier))
        return


    peuPlacerDame = False
    for i in range(l) :
        for y in range(l) :
            car = tabDamierBis[i][y]
            if car == "O" :
                peuPlacerDame = True
                #print(i)
                
                tabDamier[i][y] = "X"
                
                tabPosDePriseDerniereDamePlaceeBis = [[i,y]]
                
                
                for direction in tabDirections :
                    ii = i
                    yy = y
                    j = 1
                    while ii >= 0 and ii<l and yy>=0 and yy<l :
                        if tabDamier[ii][yy] == "O" :
                            tabDamier[ii][yy] = '-'
                            tabPosDePriseDerniereDamePlaceeBis.append([ii,yy])
                        print(ii,yy,'"'+tabDamier[ii][yy]+'"',direction,"j="+str(j),"nbd =",nbDamesPlacees+1) #,"♥\n")
                        print(tabPosDePriseDerniereDamePlaceeBis)
                        print(toStr(tabDamier))

                        ii = ii + j*direction[0]
                        yy = yy + j*direction[1]
                        print(ii,yy,"\n") 
                        j=j+1
                       

                #print(nbDamesPlacees+1)
                #print(tabDamier)
                tabDamierBis = tabDamier
                placeDame(tabDamierBis, nbDamesPlacees+1,tabPosDePriseDerniereDamePlaceeBis)
            
    if not peuPlacerDame : 
        if tabPosDePriseDerniereDamePlacee != [] :
            for tabCoord in tabPosDePriseDerniereDamePlacee :
                i,y = list(tabCoord)
                tabDamier[i][y] = "O"
        return

placeDame(tabDamier,0,[])

