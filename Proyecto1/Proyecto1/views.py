from django.http import HttpResponse
import datetime

def saludo(request): #primera vista

    documento = "<html><body><h1>HOLA MUNDO!!!</h1></body></html>"
    return HttpResponse(documento)

def dameFecha(request): #primera vista

    fecha_actual=datetime.datetime.now()
    documento2 = "<html><body><h1>fecha y hora actuales %s </h1></body></html>" % fecha_actual
    return HttpResponse(documento2)


def calcularEdad(request,edad, anho): 
    #edadActual=20
    periodo=anho-2022
    edadFutura=edad+periodo
    documento="<html><body><h2>en el año %s tendras %s años" %(anho, edadFutura)

    return HttpResponse(documento)
