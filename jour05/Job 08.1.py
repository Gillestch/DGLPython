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


request = "SELECT promotion.name,count(*) FROM promotion,student WHERE student.promotion_fk=promotion.id GROUP BY promotion.name"
curseur = connexion.cursor()
curseur.execute(request)

titres = curseur.fetchall()

#print(titres)

for titre in titres :
    print("promotion :",titre[0]," | nombre d'étudiants :",titre[1])

connexion.close()
curseur.close()