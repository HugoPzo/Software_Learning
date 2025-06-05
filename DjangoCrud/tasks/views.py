from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == "GET":
        context = {
            'form': UserCreationForm,
        }
        return render(request, 'Login/signup.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Register User
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse("User created succesfully!")
            except:
                return HttpResponse('Username already exists')

        return HttpResponse("Password do not match!")




