# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:55:03 2021

@author: Gilles
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:22:05 2021

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
class Auteur(Personne) :
    pass
    def __init__(self, fnom, fprenom) :
        self.name = fnom
        self.prenom = fprenom

        self.oeuvre=[]
    
    def listerOeuvre(self) :
        print(self.oeuvre)
    
    def ecrireUnLivre(self,titre) :
        self.oeuvre.append(titre)

class Livre(object) :
    def __init__(self,titre,auteur) :
        self.titre = titre
        self.auteur = Auteur
    def print(self) :
        print ("Le titre du livre est : ",str(self.titre))

 
class Bibliotheque(object) :
    def __init__(self,fnom,fcata) :
        self.nom = fnom
        self.catalogue = fcata
     
    def acheterLivre(fAuteur,fnom,fnb) :
       if (fnom in fAuteur.oeuvre) : 
         1   
        
    def poulet():
        1

p1 = Personne("Jojo","Lapin")
p2 = Etudiant("Easter","Egg")
p1.se_presenter()
p2.se_presenter() 
a1=Auteur("Houhou","Joseph")
a1.ecrireUnLivre("La grande chose")
a1.listerOeuvre()
print ("je suis un",a1.__class__ )

