"""
URL configuration for escola project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# Esse arquivo adiciona rotas para todo o projeto, rotas globais

from django.contrib import admin
from django.urls import path, include
# Importa as direçoes locais do APP
from cursos.urls import router 

urlpatterns = [
    path('api/v1/', include('cursos.urls')),
    path('api/v2/', include(router.urls)), # chama as URLS registrada usando o viewset e routers
    path('admin/', admin.site.urls),
    #Essa rota faz faze o login no DJANGO rest_framework e não mais só no django
    path('auth/', include('rest_framework.urls')) 
]