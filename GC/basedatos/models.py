from django.db import models

# Create your models here.

class Archivo(models.Model):
  nombre = models.CharField(max_length=20)
  archivo = models.FileField(upload_to = 'archivos/')