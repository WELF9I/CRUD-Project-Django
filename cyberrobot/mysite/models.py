
from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cin=models.IntegerField()
    tel=models.IntegerField()
    email = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.prenom} {self.nom} {self.cin} {self.tel} {self.email}"

class Article(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    quantite=models.IntegerField()
    
    def __str__(self):
        return f"{self.nom} {self.description} (Quantité: {self.quantite})"
