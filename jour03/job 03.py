# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:31:28 2021

@author: Gilles
"""

import re
nb = input("Nombre de lettres : ")
f =  open('E:\AI\jours\jour3\data.txt', 'r')
ch=''
for l in f :
    ch = ch + l + "\n"
#print(ch)
#print (len(re.findall("([A-z]+)",ch)))
tabMots = re.findall("([A-z]+)",ch)
nbMots = 0
for mot in tabMots :
    #print(mot + str(len(mot)))
    if (str(len(mot)) == nb) : nbMots = nbMots+1
print("Le nombre de mots de "+str(nb)+" lettre(s) est : " + str(nbMots))