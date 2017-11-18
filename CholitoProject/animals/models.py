from django.db import models

from complaint.models import Complaint, AnimalType
from naturalUser.models import NaturalUser
from ong.models import ONG
from datetime import datetime
from django.utils import timezone

class AnimalImage(models.Model):
    image = models.ImageField(upload_to='animals/')
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)


class Animal(models.Model):
    GENDER_OPTIONS = (
        (1, "Macho"),
        (2, "Hembra"),
    )
    COLOR_OPTIONS = (
        (1, "marron"),
        (2, "amarillo"),
        (3, "blanco"),
        (4, "gris"),
        (5, "manchado"),
    )
    name = models.TextField(max_length=100)
    gender = models.SmallIntegerField(choices=GENDER_OPTIONS)
    description = models.TextField(max_length=1000)
    animal_type = models.ForeignKey(AnimalType)
    color = models.IntegerField(choices= COLOR_OPTIONS)
    estimated_age = models.PositiveSmallIntegerField()
    first_day = models.DateTimeField(auto_now_add=True)
    ong_responsable = models.ForeignKey(ONG, null=True)
    #days in adoption debe ser una funcion : fecha actual- dia ingres
    # TODO: for now
    def __str__(self):
        return self.name + " - " + self.animal_type.name


class Adopt(models.Model):
    user = models.ForeignKey(NaturalUser)
    animal = models.ForeignKey(Animal)
    sent = models.DateTimeField(auto_now_add=True)
