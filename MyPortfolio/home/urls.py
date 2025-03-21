from django.urls import path
from .views import home_render, about_render, portfolio_render, contact_render

urlpatterns = [
    path('', home_render, name='home'),
    path('about/', about_render, name='about'),
    path('portfolio/', portfolio_render, name='portfolio'),
    path('contact/', contact_render, name='contact'),
]