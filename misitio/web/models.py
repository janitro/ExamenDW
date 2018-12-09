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
