from django.urls import path,include 
from web import views




urlpatterns = [
    
    path('Login/', views.login, name='Login'),
    path('', views.home, name='home'),
    path('tecnico/', views.tecnico, name='tecnico'),
    path('asignado/', views.asignado, name='asignado'),
    
    


]



