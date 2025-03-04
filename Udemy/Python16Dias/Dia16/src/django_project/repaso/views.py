from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mi_vista_repaso(request):
    return HttpResponse('Tratando de recordar lo aprendido de Django')