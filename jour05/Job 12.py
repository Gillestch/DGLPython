# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:54:56 2021

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
request = ("SELECT unit.name,job.name FROM unit,job,registration"
          " WHERE registration.group_id="+group_id+""
          " AND job.unit_fk=unit.id"
          " AND registration.job_fk=job.id"
          )
#print(request)
curseur = connexion.cursor()
curseur.execute(request)

datas = curseur.fetchall()

#print(datas)

#print("le nom  est :",titres[0][0])
print ("Le job et la unit associés au group_id "+group_id+" :")
print (datas[0][0]," | ",datas[0][1])
#for unit in units : print(unit[0]) 

connexion.close()
curseur.close()