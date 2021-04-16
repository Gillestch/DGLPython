# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:16:33 2021

@author: Gilles
"""

c = input("Entrer une Chaine : ")
fichier = open('E:\AI\jours\jour3\output.txt', 'w')
fichier.write(c)
fichier = open('E:\AI\jours\jour3\output.txt', 'r')
for ligne in fichier print (ligne)