from django.contrib import admin
from .models import Cliente,OdenDeTrabajo,Tecnico,Asignar




admin.site.register(Tecnico)
admin.site.register(Cliente)
admin.site.register(Asignar)
admin.site.register(OdenDeTrabajo)



