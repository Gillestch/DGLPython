# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:32:52 2021

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


job_id = input("Entre un id de job : ")
request = ("SELECT skill.name FROM skill,job,job_skill"
          " WHERE job.id="+job_id+""
          " AND job_skill.job_fk=job.id"
          " AND job_skill.skill_fk=skill.id"
          )
#print(request)
curseur = connexion.cursor()
curseur.execute(request)

datas = curseur.fetchall()

print(datas)

#print("le nom  est :",titres[0][0])
print ("Les skills associés au job dont l'id est "+job_id+" :")
#print (datas[0][0]," | ",datas[0][1])
for data in datas : print(data[0]) 

connexion.close()
curseur.close()