"""Sge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views import View
from webapp.views import index,Consulta, irbase,ConsultaUser
from webapp import views
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', views.consola_administrativa, name='mantenimiento'),
    path('index.html',index,name='inicio'),
    path('index.html',index),
    path('solicitud.html',views.Consulta, name="consulta"),
    path('base.html',irbase,name="base"),
    path('',views.ConsultaUser,name="login"),
    path('login.html',views.ConsultaUser,name="login"),
    path('crearUsuario.html',views.ConsultaCreacionUsuario,name="crearusuario"),
    path('logout/', views.logout_view, name='logout'),
    

      
]


urlpatterns += staticfiles_urlpatterns()
