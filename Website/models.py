from typing import Any
from django.db import models

SEXE = (
    ("H", "Homme"),
    ("F", "Femme"),
)

TYPES = (
    ("CNSS", "CNSS"),
    ("SVIP", "SVIP"),
)

SIT_CONJ = (
    ("M", "Marié"),
    ("C", "Célibataire"),
    ("D", "Divorcé"),
    ("V", "Veufe"),
)

PAIEMENT = (
    ("C", "Chèque"),
    ("V", "Virement"),
    ("E", "Espèce"),
)

DESIGNATION_CONTRAT = (
    ("S", "SIVP"),
    ("C", "Contractuel"),
    ("O", "Occasionnel"),
    ("P", "Permanent"),
    ("T", "Titulaire"),
)

DESIGNATION_LOCAL = (
    ("S", "Siège"),
    ("M1", "Marsa corniche"),
    ("M2", "Marsa saada"),
    ("TS", "Tunis city"),
    ("AS", "Azur city"),
    ("MS", "Mall of Sousse"),
    ("MT", "Mall de Tunis"),
)

class CNSS(models.Model):
    Date_Affectation = models.DateField(null=True, blank=True)
    Numero = models.CharField(max_length=40)
    Type = models.CharField(max_length=4, choices= TYPES)

class Situation(models.Model):
    Sexe = models.CharField(max_length=10, choices= SEXE) 
    sit_conjug = models.CharField(max_length=40, choices= SIT_CONJ) 
    nb_Enfants = models.SmallIntegerField(null=True, blank=True)
    chef_famille = models.BooleanField() 
    
class Banque(models.Model):
    Designation = models.CharField(max_length=50)
    RIB = models.BigIntegerField(null= True)
    Paiement = models.CharField(max_length= 10, choices= PAIEMENT, null= True)

class Local(models.Model):
    Designation = models.CharField(max_length=25, choices= DESIGNATION_LOCAL)

class Etat_Contrat(models.Model):
    Designation = models.CharField(max_length=20, choices= DESIGNATION_CONTRAT)

class Poste(models.Model):
    Designation = models.CharField(max_length=30)
    Description = models.TextField(max_length=500)

class Affectation(models.Model):
    Id_Local = models.ForeignKey(Local, on_delete= models.CASCADE, null=True, blank=True)
    Id_Poste = models.ForeignKey(Poste, on_delete= models.CASCADE, null=True, blank=True)
    Id_Etat_Contrat = models.ForeignKey(Etat_Contrat, on_delete= models.CASCADE, null=True, blank=True)

class Employé(models.Model):
    Prénom = models.CharField(max_length=30, null=False, blank=True)
    Nom = models.CharField(max_length=30, null=False, blank=True)
    Date_Naissance = models.DateField(null=True, blank=True)
    Lieu_Naissance = models.CharField(max_length=40, null=True, blank=True)
    Adresse = models.CharField(max_length=60, null=True, blank=True)
    Echelon = models.SmallIntegerField(null=True, blank=True)
    Categorie = models.SmallIntegerField(null=True, blank=True)
    Salaire_de_Base = models.DecimalField(max_digits=8, decimal_places=3, null=False, blank=True)
    CIN = models.CharField(max_length=8, null=False, blank=True)
    Id_Banque = models.ForeignKey(Banque, on_delete= models.CASCADE, null=True, blank=True)
    Id_Situation = models.ForeignKey(Situation, on_delete= models.CASCADE, null=True, blank=True)
    Id_CNSS = models.ForeignKey(CNSS, on_delete= models.CASCADE, null=True, blank=True)
    Id_Affectation = models.ForeignKey(Affectation, on_delete= models.CASCADE, null=True, blank=True)
    