from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def render_test(request):
    return HttpResponse('Testeando los endpoints')