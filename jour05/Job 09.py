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

job = input("Entre un job : ")
request = "SELECT unit.name FROM job,unit WHERE job.name='"+job+"' AND unit.id=job.unit_fk"
curseur = connexion.cursor()
curseur.execute(request)

titres = curseur.fetchall()

#print(titres)

for titre in titres :
    print(job,titre[0])

connexion.close()
curseur.close()