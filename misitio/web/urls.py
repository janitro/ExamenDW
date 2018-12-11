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
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path(' lista_asignar/', views.lista_asignar, name='lista_asignar'),

   
   
    


]
# urlpatterns = patterns('pushes.views',
# url(r'^', 'push_notifications_view', name='push_notifications_view'),
# )



