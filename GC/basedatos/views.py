from turtle import Terminator
from django.contrib import messages
from django.shortcuts import render
from basedatos.models import Archivo 
from basedatos import models
from .models import Archivo

# Create your views here.

def index(request):
  searchTerm = request.GET.get('NombreBusqueda')
  if searchTerm:
    mensajes = Archivo.objects.filter(nombre__icontains = searchTerm)
  else:
    mensajes = 'Buscar'
     
  if request.method == 'POST':
    area = request.POST['Area']
    nombre = request.POST['Nombre']
    archivo = request.FILES['Archivo']
    agregar = models.Archivo(area=area, nombre=nombre, archivo= archivo)
    agregar.save()
    return render(request,'salto.html')
    
  return render(request,'index.html',{'searchTerm':searchTerm,'mensajes':mensajes}) 


def Salto(request):
  return render(request, 'salto.html')


