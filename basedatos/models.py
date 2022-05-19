from django.db import models

# Create your models here.

class Archivo(models.Model):
  area = models.CharField(max_length=20, null=False)
  nombre = models.CharField(max_length=20, null=False)
  archivo = models.FileField(upload_to = 'archivos/', null=False)
