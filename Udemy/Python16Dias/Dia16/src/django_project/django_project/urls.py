"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Agregamos dentro de nuestro proyecto principal la ruta(endpoint) de nuestra app
# Los endpoints se pueden definir aqui, o en el archivo 'urls' de cada app
urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('test_app/', include('test_app.urls')),
    path('repaso/', include('repaso.urls')),
]
