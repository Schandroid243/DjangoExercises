from django.db import models

# Create your models here.

class Entreprise(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    secteurActivite = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    logo = models.ImageField(upload_to='logo/', height_field=None, width_field=None, max_length=100)

    def __str__(self) -> str:
        return self.nom



class Clients(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profile/', height_field=None, width_field=None, max_length=100)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.prenom + " " + self.nom + " " + self.postnom