from django.db import models
from apps.area.models import Area

# Create your models here.
class Libro(models.Model):
    tipo = models.CharField(max_length=50, null=False, blank=False)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    editorial = models.CharField(max_length=100, null=False, blank=False)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.titulo
