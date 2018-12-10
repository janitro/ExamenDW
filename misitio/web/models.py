from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tecnico(models.Model):
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    direccion = models.CharField('Direccion', max_length=100, null= True)
    telefono = models.CharField('Telefono', max_length=100, null= True)
    region = models.CharField('Region',max_length=50,null=True)
    ciudad = models.CharField('Ciudad',max_length=50,null=True)
    

    def __str__(self):
     return self.user.email


@receiver(post_save, sender=User)
def update_user_tecnico(sender, instance, created, **kwargs):
    if created:
        Tecnico.objects.create(user=instance)
    instance.tecnico.save()



class Cliente(models.Model):

    nombre = models.CharField('Nombre Cliente', max_length=100, null= True)
    direccion = models.CharField('Dirección', max_length=100, null= True)
    ciudad = models.CharField('Ciudad', max_length=100, null= True)
    comuna = models.CharField('Comuna', max_length=100, null= True)
    telefono = models.CharField('Telefono', max_length=100, null= True)
    correo = models.EmailField('Correo de Contacto',  max_length=250, null= True)


    def __str__(self):
     return self.nombre


class Asignar(models.Model):
    dia_asc = models.DateTimeField()
    Nom_tecnico =models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    Nom_cliente =models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
     return self.dia_asc


    




class OdenDeTrabajo(models.Model):

    numero = models.AutoField('Num OTE',primary_key=True)
    fecha = models.DateField('Fecha de Hoy', null=True)
    hora_inicio = models.TimeField('Hora de Inicio', null=True)
    hora_termino = models.TimeField('Hora de Termino',null= True)
    id_acensor = models.CharField('Identificador Ascensor',max_length=100, null= True)
    mod_ascensor = models.CharField('Modelo Ascensor', max_length=100, null= True)
    fallas = models.CharField('Fallas Detectadas',max_length=600, null= True)
    reparacion = models.CharField('Reparacion Efectuadas', max_length=600, null= True)
    pieza_cambio = models.CharField('Piezas Cambiadas',max_length=100,null=True)
    Nom_tecnico =models.CharField('Nombre Tecnico',max_length=100,null=True)
    Nom_cliente =models.CharField('Nombre Cliente',max_length=100,null=True)
    asignado = models.ForeignKey(Asignar, models.CASCADE)


    def __str__(self):
     return self.asignado.nombre








  



