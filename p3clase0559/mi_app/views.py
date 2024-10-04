from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hola mundo soy Cas")

def Casandra(request):
    return HttpResponse("Soy Casandra Brito lol")

def minovia(request):
    return HttpResponse("Donde estas?")