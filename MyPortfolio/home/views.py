from django.shortcuts import render
from .models import SkillTag, Project

from django.utils.timezone import now

# Para asegurarte de que el navegador siempre cargue la versión más reciente,
# agrega un parámetro de versión en la URL del CSS en la plantilla:
def my_view(request):
    return render(request, "index.html", {"timestamp": now().timestamp()})

def home_render(request):
    context = {
        'skills' : SkillTag.objects.all(),
        'projects': Project.objects.all()
    }
    return render(request, 'home.html', context)

def about_render(request):
    return render(request, 'about.html')


def portfolio_render(request):
    return render(request, 'portfolio.html')


def contact_render(request):
    return render(request, 'contact.html')