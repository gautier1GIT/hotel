from django.db import models

# Create your models here.

class Ville(models.Model):
    nom=models.CharField(max_length=20)

class EndroitVille(models.Model):
    Ville=models.ForeignKey(Ville, on_delete=models.CASCADE)

class Hotel(models.Model):
    endroitVille=models.ForeignKey(EndroitVille, on_delete=models.CASCADE)
    nom=models.CharField(max_length=10)
    NbreEtoile=models.IntegerField()

class Spectacle(models.Model):
    nom=models.CharField(max_length=50)
    endroitVille = models.ForeignKey(EndroitVille, on_delete=models.CASCADE)


class ChambreCat(models.Model):
    prix=models.DecimalField(max_digits=1000, decimal_places=2)
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)

class Chambre(models.Model):
    chambreCat = models.ForeignKey(ChambreCat, on_delete=models.CASCADE)

class Salle(models.Model):
    Nom=models.CharField(max_length=20)

class DateSpectacle(models.Model):
    pass

class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateNaissance = models.DateField()


class ResevationSpectarcle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Spectacle = models.ForeignKey(Spectacle, on_delete=models.CASCADE)

class Depense(models.Model):
    pass

class DepenseClient(models.Model):
    montant = models.DecimalField(max_digits=1000, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    depense = models.ForeignKey(Depense, on_delete=models.CASCADE)


class PlaceCat(models.Model):
    prix=models.CharField(max_length=20)
    nbrPlace=models.IntegerField()
    spectacle = models.ForeignKey(Spectacle, on_delete=models.CASCADE)

class Place(models.Model):
    placeCat = models.ForeignKey(PlaceCat, on_delete=models.CASCADE)

class ReservationHotel(models.Model):
    client = models.ForeignKey(Client , on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    DateDebut=models.CharField(max_length=50)
    DateFin=models.CharField(max_length=20)

class DateDeroulementSpectacle(models.Model):
    spectacle = models.ForeignKey(Spectacle, on_delete=models.CASCADE)
    dateSpectacle = models.ForeignKey(DateSpectacle, on_delete=models.CASCADE)

class SalleDeroulementSpectacle(models.Model):
    spectacle = models.ForeignKey(Spectacle, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)