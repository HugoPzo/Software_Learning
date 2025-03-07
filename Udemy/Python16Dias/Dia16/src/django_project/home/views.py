
# from django.http import HttpResponse

# render se usa para renderizar plantillas HTML, aunque en este código no se está usando.
# HttpResponse permite devolver directamente una respuesta HTTP con contenido de texto.

# Tipo de pagina, que representa una lista de objetos - modelos
from django.views.generic.list import ListView
# Vista de Detalle
from django.views.generic.detail import DetailView
# Clase con herramientas para crear nuevas listas - nuevos modelos
from django.views.generic.edit import CreateView
# Redireccionamiento
from django.urls import reverse_lazy
from .models import Tarea
# Clase de edicion de tareas
from django.views.generic.edit import UpdateView
# Clase para eliminar Tarea
from django.views.generic.edit import DeleteView
# clase para login
from django.contrib.auth.views import LoginView
# clase para middleware de logueo - bloqueo de paginas sin loguera - Se coloca en cualquier Clase que se quiera bloquear
from django.contrib.auth.mixins import LoginRequiredMixin # Mixins tiene muchas ayudas para la restriccion por rol

# Clases para registar nuevos usuarios - generica
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



# Metodos para desloguear
from django.contrib.auth import logout
from django.shortcuts import redirect


# Se crea una clase hija
# Clase de vista de logueo
class Logueo(LoginView):
    template_name = 'home/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    # Si se logea se abre la pagina de tareas
    def get_success_url(self):
        return reverse_lazy('home')


# clase para registrar nuevos usuarios
class Registrar(FormView):
    template_name = 'home/registro.html'
    # Tipo de Formulario
    form_class = UserCreationForm
    # Redireccionar una vez registrado
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    # Cuando se usa FormView o una vista basada en formularios como CreateView, UpdateView, DeleteView,
    # Django maneja los formularios con el método form_valid(). Este método se ejecuta cuando el formulario
    #  es válido y generalmente guarda el formulario antes de redirigir a otra página.
    # Devolver lo que hay en la instancia
    def form_valid(self, form): # Es un método que se ejecuta cuando el formulario es válido.
        # Guardamos el usuario, la informacion del formulario
        usuario = form.save()
        # Si el usuario existe
        if usuario is not None:
            # Se loguea
            login(self.request, usuario)

        # Retornamos la informacion del formulario - Si no fue posible registrarse nos regresa al mismo formulario
        return super().form_valid(form) # Llama al método form_valid() de la clase padre (super()),
        # que guarda el formulario y redirige al usuario a la URL de éxito (success_url).

    # Bloquear el endpoint de registro si ya se esta logueado
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        # Si no esta autenticado, si nos permite ingresar
        return super(Registrar, self).get(*args, **kwargs)


# Funcion especial para deslogear
def custom_logout(request):
    logout(request)  # Borra la sesión
    return redirect('login')  # Redirige manualmente a login


# Listas - Se configura para mostrar solo los datos de el usuario en especifico
class ListaPendientes(LoginRequiredMixin, ListView):
    # La clase necesita un modelo y un query set(consulta de datos filtrada)

    # Modelo de base de datos - 'model' must be the name
    model = Tarea
    template_name = 'home/lista_tareas.html'
    context_object_name = 'tareas'

    # MOSTRAR LOS DATOS UNICOS DE CADA USUARIO
    # Proporcionamos los datos solamente del usuario en especifico
    def get_context_data(self, **kwargs):
        # Obtenemos todos los datos por usuario(contexto de cada usuario)
        context = super().get_context_data(**kwargs)

        # Se filtra por el usuario que esta haciendo la peticion - solo devuelve esas tareas
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        # Solo se muestran las tareas no completas
        context['count'] = context['tareas'].filter(completo=False)
        # print(context) # {'paginator': None, 'page_obj': None, 'is_paginated': False, \
        # 'object_list': <QuerySet [<Tarea: Acabar Curso>, <Tarea: Acabar Dia 16>,
        # <Tarea: Practicar DJango>]>, 'tareas': <QuerySet [<Tarea: Acabar Curso>,
        # <Tarea: Acabar Dia 16>, <Tarea: Practicar DJango>]>,
        # 'view': <home.views.ListaPendientes object at 0x00000125B3F64BD0>}
        # Se pasa el contexto['ciudad'] = 'madrid' - Se manda esta informacion
        # context['ciudad'] = 'madrid'


        # Filtrar por busqueda          '# nombre del input text - contemplamos que puede estar vacia(Se visualizan
        # todas las tareas
        valor_busqueda = self.request.GET.get('area-buscar') or ''
        if valor_busqueda:                      # Busca tareas que tengan similitud con el texto
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_busqueda)

        # Mantener el valor de la busqueda
        context['valor_busqueda'] = valor_busqueda

        return context



# Listas a detalle
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    # Nombre de template
    template_name = 'home/tarea.html'

    # Solo mostramos los datos que le pertenecen al usuario - protegemos los endpoints
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


# Crear nuevas listas de modelo
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    # Campos que queremos llenar
    # Primera forma de hacerlo
    # fields = ['titulo', 'descripcion', 'etc']
    # Pedir todos los campos - Mandar todos los datos
    fields = ['titulo', 'descricion', 'completo']
    # Redireccionamiento
    success_url = reverse_lazy('home')

    # Asignar cada tarea a su usuario creador, no a uno en conjunto
    def form_valid(self, form):
        # Asigna automaticamente la tarea creada al usuario que la creo
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)


# Editar tareas
class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descricion', 'completo']
    success_url = reverse_lazy('home')


    # Solo mostramos los datos que le pertenecen al usuario - protegemos los endpoints
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


# Eliminar Tarea
class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('home')
    template_name = 'home/eliminando_tarea.html'

    # Solo mostramos los datos que le pertenecen al usuario - protegemos los endpoints
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)




# Create your views here.

# def mi_vista(pedido):
#     return HttpResponse("Bienvenido a tu primer pagina web con django")
#

# def mi_vista(pedido): Se define una función llamada mi_vista, que es una vista en Django.

# Django pasa automáticamente un objeto HttpRequest (en este caso llamado pedido) a la vista.
# pedido contiene detalles de la solicitud del usuario, como la URL, método (GET, POST, etc.), y encabezados.

# return HttpResponse("Bienvenido a tu primer pagina web con django"):
# Devuelve una respuesta HTTP con el mensaje "Bienvenido a tu primer pagina web con django".
# Este mensaje aparecerá como texto plano en el navegador cuando un usuario visite la URL asociada con esta vista.
