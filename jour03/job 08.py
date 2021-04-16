# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:51:31 2021

@author: Gilles
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
import unicodedata # pour enlever les accents

#ceci est un tuto sur https://moonbooks.org/Articles/Supprimer-les-accents-dun-string-en-python/
#s = 'Découvrez tous les logiciels à télécharger ö Ö'
#print(s)
#s1 = unicode(s,'utf-8') # unicode n'existe pas !!! : génère une erreur
#s2 = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').upper()   
#print(s2)

import re

""" version lente
f =  open('E:\AI\jours\jour3\data.txt', 'r')

ch=''
for l in f :
    ch = ch + str(unicodedata.normalize('NFD', l).encode('ascii', 'ignore').upper()) + "\n" # enlève les accent de chaque lignes et mets tout en majuscules
#print(ch)
"""

# version rapide trouvée sur https://python.sdv.univ-paris-diderot.fr/07_fichiers/#712-methode-read
with open('E:\AI\jours\jour3\data.txt', "r") as filin:
    ch = str(unicodedata.normalize('NFD', filin.read()).encode('ascii', 'ignore').upper())

tabMots = re.findall("([A-Z-]+)",ch)
tabNbMotsDeLongueurEnIndice = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for mot in tabMots :
    
    tabNbMotsDeLongueurEnIndice[len(mot)] = tabNbMotsDeLongueurEnIndice[len(mot)] + 1
print (tabNbMotsDeLongueurEnIndice)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.bar(range(len(tabNbMotsDeLongueurEnIndice)), tabNbMotsDeLongueurEnIndice)  # Plot some data on the axes.

