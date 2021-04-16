# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:45:00 2021

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

student_id = input("Entre un id de student : ")
request = "SELECT unit.name FROM unit,unit_viewer WHERE unit_viewer.student_fk='"+student_id+"' AND unit_viewer.unit_fk=unit.id"
curseur = connexion.cursor()
curseur.execute(request)

units = curseur.fetchall()

#print("le nom  est :",titres[0][0])
print ("Unitées associées au student dont l'id est "+student_id+" :")
for unit in units : print(unit[0]) 

connexion.close()
curseur.close()