from django.urls import path,include
from . import views

urlpatterns = [

   path('perfil/', views.perfil, name='perfil'),

  ]