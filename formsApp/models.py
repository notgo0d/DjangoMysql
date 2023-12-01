from django.db import models

class UserData(models.Model):
    nombre = models.CharField(max_length=255)
    fono = models.CharField(max_length=255)
    email = models.EmailField()
    estado = models.CharField(max_length=10, choices=[('activo', 'ACTIVO'), ('inactivo', 'INACTIVO')], null=True)

    def __str__(self):
        return self.nombre

