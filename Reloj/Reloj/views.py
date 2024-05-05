from django.shortcuts import render
import requests

def mostrar_home(request):
    return render(request, 'home.html')

def mostrar_alarma(request):
    return render(request, 'alarma.html')

def mostrar_reloj(request):
    return render(request, 'reloj.html')

def mostrar_temporizador(request):
    return render(request, 'temporizador.html')
