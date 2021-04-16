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

group_id = input("Entre un group_id : ")
request = "SELECT job.name FROM job,registration WHERE group_id="+group_id+" AND registration.job_fk=job.id"
curseur = connexion.cursor()
curseur.execute(request)

titres = curseur.fetchall()

print("le job correspondant est :",titres[0][0])


connexion.close()
curseur.close()