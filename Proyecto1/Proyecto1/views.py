from django.http import HttpResponse
import datetime
from django.template import Template,Context, loader
from django.template.loader import get_template
from django.shortcuts import render
class Persona(object):

    def __init__(self, nombre, apellido):
        
        self.nombre=nombre

        self.apellido=apellido


def sistema(request): #primera vista
    fecha_actual=datetime.datetime.now()

    return render(request, "Sistema.html", {"dame_fecha":fecha_actual})

def sistema1(request): #primera vista
    fecha_actual=datetime.datetime.now()

    return render(request, "Sistema1.html", {"dame_fecha":fecha_actual})    

def saludo(request): #primera vista

    persona1=Persona("Matias","Urrutia")
    
    ahora=datetime.datetime.now()

    return render(request, "miplantilla.html", {"nombre_persona":persona1.nombre, "apellido_persona":persona1.apellido, "momento_actual":ahora})

def dame_fecha(request): #primera vista

    fecha_actual=datetime.datetime.now()
    documento2 = "<html><body><h1>fecha y hora actuales %s </h1></body></html>" % fecha_actual
    return HttpResponse(documento2)