from django.db import models

class Familia(models.Model):
    
    # atributos:
    nombre = models.CharField(max_length = 40)
    edad = models.IntegerField()
