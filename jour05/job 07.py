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
    database = "laplateforme"
    )

"""
request =   ""
curseur = connexion.cursor()
curseur.execute(request)
"""


request = "SELECT name FROM unit"
curseur = connexion.cursor()
curseur.execute(request)

titres = curseur.fetchall()

for titre in titres :
    print(titre[0])

connexion.close()
curseur.close()

