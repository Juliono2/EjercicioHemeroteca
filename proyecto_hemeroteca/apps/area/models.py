from django.db import models

# Create your models here.
class Area(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre