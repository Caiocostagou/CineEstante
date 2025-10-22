from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filmes.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('filmes/', include('filmes.urls')),
]

# Adicionar suporte a media files em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)