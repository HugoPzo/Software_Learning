"""
URL configuration for djangoproject project.

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
from django.urls import path

from django.urls import include # Con este metodo añadimos los bloques
# de urls que son de diferentes apps

# AQUI AGREGAMOS RUTAS(ENDPOINTS) PARA EJECUTAR VIEWS DE LAS APPS

# Las rutas colocadas aqui, preceden a las rutas dentro del archivo urls de cada app

# P.E - Son Prefijos

# home/ -> Nos llevara al endpoint base de esa app, establecido por ('')
# home/about -> Nos llevara al endpoint que ese definido por esa ruta ('about/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')) # path(ruta(endpoint), bloque app.urls)
]
