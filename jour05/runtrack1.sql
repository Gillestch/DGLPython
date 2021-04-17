# -*- coding: utf-8 -*-
/*"""
Created on Fri Apr 16 09:44:19 2021

@author: Gilles
"""
*/

CREATE DATABASE IF NOT EXISTS runtrack1;# 1 ligne affectée.

USE runtrack1;# MySQL a retourné un résultat vide (aucune ligne).

SET FOREIGN_KEY_CHECKS=0;# MySQL a retourné un résultat vide (aucune ligne).
 -- to disable them



DROP TABLE IF EXISTS `livre`;# MySQL a retourné un résultat vide (aucune ligne).

CREATE TABLE IF NOT EXISTS livre(
    id INT PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(100),
    auteur_id INT,
    FOREIGN KEY (auteur_id) REFERENCES auteur(id)
	);# MySQL a retourné un résultat vide (aucune ligne).



# DELETE FROM livre;# MySQL a retourné un résultat vide (aucune ligne).


INSERT INTO LIVRE(titre,auteur_id) VALUES 
        ('La grande carotte',1),
        ('La petite carotte',1),
        ('La carotte enchantée',1),
        ('Cheri je t\'aime',2),
        ('Mon amour de ma vie',2),
        ('Choisir sa couleur de tifs',3),
        ('Eclater en sanglots parcequ\'on a raté sa couleur',3),
        ('J\'ai trouvé un truc',4),
        ('Ici c\'est trop top',4),
        ('Donne moi du pain',5),
        ('Ne me mange pas',5),
        ('Hou la la c\'est loin',5);# 12 lignes affectées.


DROP TABLE IF EXISTS `auteur`;# MySQL a retourné un résultat vide (aucune ligne).

CREATE TABLE IF NOT EXISTS auteur(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nom VARCHAR(30),
    prenom VARCHAR(30)
    );# MySQL a retourné un résultat vide (aucune ligne).





# DELETE FROM auteur;# MySQL a retourné un résultat vide (aucune ligne).


# INSERT INTO auteur (nom,prenom) VALUES("Jojo","Lapin");

INSERT INTO auteur(nom,prenom) VALUES
                ('Jojo','Lapin'),
                ('Bibi','Fricotin'),
                ('Zora','La Rousse'),
                ('Grand','Coeur Gueri'),
                ('Petit','Poucet')
            ;# 5 lignes affectées.

            
SET FOREIGN_KEY_CHECKS=1;# MySQL a retourné un résultat vide (aucune ligne).
 -- to re-enable them# MySQL a retourné un résultat vide (aucune ligne).
