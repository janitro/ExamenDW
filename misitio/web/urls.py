from django.urls import path,include 
from web import views




urlpatterns = [
    
    path('Login/', views.login, name='Login'),
    path('', views.home, name='home'),
    path('tecnico/', views.tecnico, name='tecnico'),
    path('asignado/', views.asignado, name='asignado'),
    path('cliente/', views.cliente, name='cliente'),
    path('orden_trabajo/', views.orden_trabajo, name='orden_trabajo'),
    path('prueba/', views.prueba, name='prueba'),
    


]



