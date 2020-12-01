"""PaginaProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from PaginaProyecto.views import *
from pic.views import *
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static

handler404 = error404
handler500 = error500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio'),
    path('somos/', somos, name='somos'),
    path('contacto/', contacto, name='contacto'),
    path('registro/', usuarioNuevo, name='registro'),
    path('ingresar/', ingresar, name='ingresar'),
    path('privado/', privado),
    path('salir/', salir, name='salir'),
    path('prod0/', prod0, name='prod0'),
    path('prod1/', prod1, name='prod1'),
    path('prod2/', prod2, name='prod2'),
    path('prod3/', prod3, name='prod3'),
    path('prod4/', prod4, name='prod4'),
    path('buscar/', buscar, name='buscar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

