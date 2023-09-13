from typing import Any
from django.db import models

SEXE = (
    ("Homme", "Homme"),
    ("Femme", "Femme"),
)

TYPES = (
    ("CNSS", "CNSS"),
    ("SVIP", "SVIP"),
)

SIT_CONJ = (
    ("Marié", "Marié"),
    ("Célibataire", "Célibataire"),
    ("Divorcé", "Divorcé"),
    ("Veufe", "Veufe"),
)

PAIEMENT = (
    ("Chèque", "Chèque"),
    ("Virement", "Virement"),
    ("Espèce", "Espèce"),
)

DESIGNATION_CONTRAT = (
    ("SVIP", "SIVP"),
    ("Contractuel", "Contractuel"),
    ("Occasionnel", "Occasionnel"),
    ("Permanent", "Permanent"),
    ("Titulaire", "Titulaire"),
)

DESIGNATION_LOCAL = (
    ("Siège", "Siège"),
    ("Marsa corniche", "Marsa corniche"),
    ("MMarsa saada", "Marsa saada"),
    ("Tunis city", "Tunis city"),
    ("Azur city", "Azur city"),
    ("Mall of Sousse", "Mall of Sousse"),
    ("Mall de Tunis", "Mall de Tunis"),
)

class CNSS(models.Model):
    Date_Affectation = models.DateField(null=True, blank=True)
    Numero = models.CharField(max_length=40, unique= True)
    Type = models.CharField(max_length=4, choices= TYPES)
    def __str__(self):
        return "cnss {0}".format(self.Numero)

class Situation(models.Model):
    Sexe = models.CharField(max_length=10, choices= SEXE) 
    sit_conjug = models.CharField(max_length=40, choices= SIT_CONJ) 
    nb_Enfants = models.SmallIntegerField(null=True, blank=True)
    chef_famille = models.BooleanField()
    def __str__(self):
        return "{0}/{1}/{2}".format(self.Sexe, self.sit_conjug, self.nb_Enfants)
    
class Banque(models.Model):
    Designation = models.CharField(max_length=50)
    Adresse = models.CharField(max_length=60, null=True, blank=True)
    RIB = models.BigIntegerField(null= True, unique=True)
    Paiement = models.CharField(max_length= 10, choices= PAIEMENT, null= True)
    def __str__(self):
        return "Banque: ({0}) ({1})".format( self.Designation, self.RIB)

class Local(models.Model):
    Designation = models.CharField(max_length=25, choices= DESIGNATION_LOCAL)
    def __str__(self):
        return "Local: {0}".format(self.Designation)

class Etat_Contrat(models.Model):
    Designation = models.CharField(max_length=20, choices= DESIGNATION_CONTRAT)
    def __str__(self):
        return "Contrat: {0}".format(self.Designation)

class Poste(models.Model):
    Designation = models.CharField(max_length=30)
    Description = models.TextField(max_length=500)
    def __str__(self):
        return "Poste: {0}".format(self.Designation)
    
class Affectation(models.Model):
    Id_Local = models.ForeignKey(Local, on_delete= models.CASCADE, null=True, blank=True)
    Id_Poste = models.ForeignKey(Poste, on_delete= models.CASCADE, null=True, blank=True)
    Id_Etat_Contrat = models.ForeignKey(Etat_Contrat, on_delete= models.CASCADE, null=True, blank=True)
    def __str__(self):
        return "{0} {1} {2}".format(self.Id_Local.Designation, self.Id_Poste.Designation, self.Id_Etat_Contrat.Designation)

class Congés(models.Model):
    Absence  = models.SmallIntegerField(null=False, blank=True, default= 0)
    Congés_Annuels = models.SmallIntegerField(null=False, blank=True, default= 26)
    Congés_Maladie = models.SmallIntegerField(null=False, blank=True, default= 7)
    Congés_Sans_Solde = models.SmallIntegerField(null=False, blank=True, default= 0)
    
class Employé(models.Model):
    Prénom = models.CharField(max_length=30, null=False, blank=True)
    Nom = models.CharField(max_length=30, null=False, blank=True)
    Matricule = models.BigIntegerField(null=False)
    Télephone = models.BigIntegerField(null=False)
    Date_Naissance = models.DateField(null=True, blank=True)
    Lieu_Naissance = models.CharField(max_length=40, null=True, blank=True)
    Adresse = models.CharField(max_length=60, null=True, blank=True)
    Echelon = models.SmallIntegerField(null=True, blank=True)
    Categorie = models.SmallIntegerField(null=True, blank=True)
    Salaire_de_Base = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=True)
    CIN = models.CharField(max_length=8, null=False, blank=True, unique=True)
    Id_Banque = models.OneToOneField(Banque, on_delete= models.CASCADE, null=True, blank=True)
    Id_Situation = models.ForeignKey(Situation, on_delete= models.CASCADE, null=True, blank=True)
    Id_CNSS = models.OneToOneField(CNSS, on_delete= models.CASCADE, null=True, blank=True)
    Id_Affectation = models.ForeignKey(Affectation, on_delete= models.CASCADE, null=True, blank=True)
    Id_Congés = models.OneToOneField(Congés, on_delete= models.CASCADE, null=True, blank=True)
    def __str__(self):
        return "Employé: {0} {1}".format( self.Prénom, self.Nom)