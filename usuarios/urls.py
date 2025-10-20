# usuarios/urls.py (este é o arquivo novo que você está criando)

from django.urls import path
from . import views

urlpatterns = [
    # Este path define a URL /usuarios/perfil/
    path('perfil/', views.ver_perfil, name='ver_perfil'),
]