# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:51:34 2021

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
request = ("SELECT skill.name,sum(earned) FROM skill,job_skill,acquiered_skill"
          " WHERE acquiered_skill.student_fk="+student_id+""
          " AND acquiered_skill.job_skill_fk=job_skill.id"
          " AND job_skill.skill_fk=skill.id"
          " GROUP BY skill.name"
          )
#print(request)
curseur = connexion.cursor()
curseur.execute(request)

datas = curseur.fetchall()

#print(datas)

#print("le nom  est :",titres[0][0])
print ("Le cumul des points gagnés par l'étudiant dont l'id est "+student_id+" :")
#print (datas[0][0]," | ",datas[0][1])
for data in datas : print(data[0],":",data[1]) 

connexion.close()
curseur.close()