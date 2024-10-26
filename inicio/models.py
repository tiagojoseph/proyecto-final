from django.db import models

class Propiedad(models.Model):
    metros_cuadrados = models.IntegerField()
    ubicacion = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)