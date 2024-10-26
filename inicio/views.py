from django.http import HttpResponse
from django.shortcuts import render
from inicio.models import Propiedad

def inicio (request):
    #return HttpResponse ("hola")
    return render (request, "index.html")


def crear_la_propiedad (request, metros_cuadrados, ubicacion, precio):

    propiedad = Propiedad (metros_cuadrados = metros_cuadrados, ubicacion = ubicacion, precio = precio)
    propiedad.save()
    return render (request, "crear_la_propiedad.html", {"propiedad": propiedad} )
    
