from django.db import models
import os
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class Salles(models.Model):
#     nom_salle = models.CharField(max_length=50,blank=True,null=True)
#     etg = models.CharField(max_length=50,blank=True,null=True)

#     def __str__(self):
#         return self.nom_salle
    
# class Entites(models.Model):
#     nom_entite = models.CharField(max_length=150,blank=True,null=True)
#     acronyme = models.CharField(max_length=50,blank=True,null=True)
#     superieur = models.ForeignKey('self', on_delete = models.CASCADE,blank=True,null=True)
#     chef = models.ForeignKey('Utilisateurs', on_delete=models.SET_NULL, blank=True,null=True)

#     def __str__(self):
#         return self.nom_entite

# def chargement_photo(instance, nom_fichier):
#     username = instance.user.username
#     dossier = f'photos/{username}'
#     return os.path.join(dossier,nom_fichier)

# class Utilisateurs(AbstractUser):
#     nom = models.CharField(max_length=50)
#     prenom = models.CharField(max_length=50)
#     photo = models.ImageField(upload_to =chargement_photo,blank=True,null=True,default='photos/default.png')
#     grade = models.CharField(max_length=50,blank=True,null=True)
#     telephone = models.CharField(max_length=30)
#     salle = models.ForeignKey(Salles, on_delete=models.SET_NULL, blank=True,null = True)
#     entite = models.ForeignKey(Entites, on_delete=models.SET_NULL, blank=True,null=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     choixSexe = (
#         ('M','M'),#male
#         ('F','F'),#femele
#     )
#     sexe = models.CharField(max_length=1,null=True,choices=choixSexe)

#     def __str__(self):
#         return self.username