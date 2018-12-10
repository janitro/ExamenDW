from django.urls import path,include 
from web import views




urlpatterns = [
    
    path('Login/', views.login, name='Login'),
    
    


]



