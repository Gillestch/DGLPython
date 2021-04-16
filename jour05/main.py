# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:16:11 2021

@author: Gilles
"""

import mysql.connector

connexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "runtrack1"
    )

"""
request =   ""
curseur = connexion.cursor()
curseur.execute(request)
"""

auteur = input("Entres un nom d'auteur : ")

request = "SELECT livre.titre FROM livre,auteur WHERE UPPER(auteur.nom)=UPPER('"+auteur+"') AND livre.auteur_id=auteur.id"
curseur = connexion.cursor()
curseur.execute(request)

titres = curseur.fetchall()

for titre in titres :
    print(titre)

connexion.close()
curseur.close()

