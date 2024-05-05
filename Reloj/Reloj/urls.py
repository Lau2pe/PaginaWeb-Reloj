from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mostrar_home),
    path('inicio/', views.mostrar_home),
    path('reloj/', views.mostrar_reloj),
    path('temporizador/', views.mostrar_temporizador),
    path('alarma/', views.mostrar_alarma),
    
]
