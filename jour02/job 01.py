# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:31:15 2021

@author: Gilles
"""

class Personne(object) : # le object est optionnel et sert à optimiser le multiheritage (ca sert pas ici)
    def __init__(self,fnom,fprenom) :
        self.name = fnom
        self.prenom = fprenom
    def se_presenter(self) :
        
        print("je m'appelle",self.prenom,self.name)
    
    ## getter method to get the properties using an object
    def get_nom(self):
        return self.nom

    ## setter method to change the value 'a' using an object
    def set_prenom(self, a):
        self.prenom = a

class Etudiant(Personne) :
    pass

p1 = Personne("Jojo","lapin")
p2 = Etudiant("Easter","Egg")
p1.se_presenter()
p2.se_presenter() 

