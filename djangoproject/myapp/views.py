from django.shortcuts import render, redirect  # Se usa para renderizar nuestras paginas
from django.http import HttpResponse, JsonResponse # Solo manda una respuesta HTTP o Json
from .models import Project, Task # Importamos los modelos
from django.shortcuts import get_object_or_404 # Funcion que permite obtener un objeto, y si no es, regresa un error
# 404 - Asi evitamos que el servidor se caiga
from .forms import CreateNewTask, CreateNewProject
def home(request):
    return render(request, 'hello.html')

def about(request):
    context = {
        'username' : 'hugop',
        'email' : 'perez.hugo.3010@gmail.com',
        'password': '645effgtscbhyjasad'
    }
    return render(request, 'about.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }

    return render(request, 'projects.html', context)

def tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks
    }
    return render(request, 'tasks.html', context)

def form_tasks(request):

    if request.method == 'GET':
        return render(request, 'formulary.html', {
            'form' : CreateNewTask
        })
    else:
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title,
                            description=description,
                            project_id=2)
        return redirect('/tasks')

def new_project(request):
    if request.method == 'GET':
        return render(request, 'new_project.html', {
            'form': CreateNewProject
        })
    else:
        name = request.POST['name']
        Project.objects.create(name=name)
        return redirect("/projects")
