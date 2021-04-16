# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:49:16 2021

@author: Gilles

Job 16
Faites un programme qui demande à l’utilisateur d’entrer un id de ‘skill’ et
qui affiche l’id du ‘student’ ayant le plus de ‘earned’ sur ce skill. 
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


skill_id = input("Entre un id de 'skill' : ")
request = ("SELECT student_fk,sum(earned) FROM acquiered_skill,job_skill"
          " WHERE job_skill.id=job_skill_fk"
          " AND skill_fk="+skill_id+""
          " GROUP BY student_fk"
          )
#print(request)
curseur = connexion.cursor()
curseur.execute(request)

datas = curseur.fetchall()

#print(datas)

maxEarned = 0
bestStudent = 0
for id_student,sumEarned in datas:
    #print(int(sumEarned))
    if int(sumEarned)>=maxEarned : 
        bestStudent = id_student
        maxEarned = int(sumEarned)
    #print(id_student,sumEarned)
print("l'id du student ayant le plus de earned est :",bestStudent)

#print("le job est :",titres[0][0])
#print ("Le cumul des points gagnés par l'étudiant dont l'id est "+student_id+" :")
#print (datas[0][0]," | ",datas[0][1])
#for data in datas : print(data[0],":",data[1]) 

connexion.close()
curseur.close()