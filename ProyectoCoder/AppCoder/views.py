from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada=31075)
    curso.save()
    documento = f"Curso: {curso.nombre} ..... Camada: {curso.camada}"
    return HttpResponse(documento)


# Create your views here.
