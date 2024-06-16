from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User 
from datetime import datetime;
# 1
class Personnel(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="personnel_user")
    nom_prenom=models.CharField(max_length=100,blank=True, null=True)
    
    date_naissance =models.DateField(default=datetime.now,null=True)
    genre =models.CharField(max_length=100,null=True)
    qualification=models.CharField(max_length=100)
    telephone =models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100, null = True)
    date_enre=models.DateField(default=datetime.now,null=True)


    def __str__(self):
        return self.nom_prenom if self.nom_prenom else "Nom non spécifié"


#2
class Projet(models.Model):
    nom_projet=models.CharField(max_length=100,null=True)
    chef_projet=models.ForeignKey(Personnel,on_delete=models.CASCADE,null=True)
    lieu=models.CharField(max_length=100,null=True)
    date_debut=models.DateField(null=True)
    date_fin=models.DateField()
    description_projet=models.CharField(max_length=100,null=True)
# 3
class Rapport(models.Model):
    personnel=models.ForeignKey(Personnel,on_delete=models.CASCADE,null=True)
    projet=models.ForeignKey(Projet,on_delete=models.CASCADE,null=True)
    titre_rapport=models.CharField(max_length=150,null=True)
    description=models.TextField(max_length=500,null=True)
    date=models.DateField()
# 4
class Materiel(models.Model):
    nom_materiel=models.CharField(max_length=100,null=True)
    type_materiel=models.CharField(max_length=100,null=True)
    quantite_materiel=models.CharField(max_length=100,null=True)
    qualite=models.CharField(max_length=100,null=True)   
    projet=models.ForeignKey(Projet,on_delete=models.CASCADE,null=True)    
         



# 5
class Perdieme(models.Model) :
    personnel=models.ForeignKey(Personnel,on_delete=models.CASCADE,null=True)
    
    type_perdieme= models.CharField(max_length=100,null=True)
    montant=models.IntegerField()
    date_transaction=models.DateField()
 