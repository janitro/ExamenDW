from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from web.models import Tecnico,Cliente,Asignar,OdenDeTrabajo
from datetime import datetime,date, time,timezone




class AgregarTecnicoForm(UserCreationForm):
    email = forms.CharField(max_length=50, 
    widget=forms.EmailInput(attrs={'class': 'form-control',
    'placeholder':'ejemplo@ejemplo.cl'}))
    first_name = forms.CharField(max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'Bruno Cordova'}))
    direccion = forms.CharField(max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'Avenida Miraflores'}))
    telefono = direccion = forms.CharField(max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'+56 9907012'}))
    region = forms.CharField(max_length=50, 
    widget=forms.Select(attrs={'class': 'form-control',
    'id':'regiones','for': 'regiones'}))
    ciudad = forms.CharField(max_length=50, 
    widget=forms.Select(attrs={'class': 'form-control',
    'id':'comunas','for': 'comunas'}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'direccion', 'telefono',  'region', 
        'ciudad',  )



class ClienteForm(forms.ModelForm):

    ciudad = forms.CharField(max_length=50, 
    widget=forms.Select(attrs={'class': 'form-control',
    'id':'regiones','for': 'regiones'}))
    comuna = forms.CharField(max_length=50, 
    widget=forms.Select(attrs={'class': 'form-control',
    'id':'comunas','for': 'comunas'}))

    class Meta:
        model = Cliente
        fields = ('nombre', 'correo', 'telefono', 'direccion', 'ciudad', 'comuna',  )






class AsignarForm(forms.ModelForm):

    dia_asc =forms.DateTimeField(initial=datetime.now,disabled='disabled')
    class Meta:
        model = Asignar
        fields = ('dia_asc', 'Nom_tecnico', 'Nom_cliente', )



class OrdenForm(forms.ModelForm):

    class Meta:
        model = OdenDeTrabajo
        fields = ('numero', 'fecha', 'hora_inicio', 'hora_termino', 'id_acensor', 
        'mod_ascensor', 'fallas', 'reparacion', 'pieza_cambio', 'Nom_tecnico', 
        'Nom_cliente', 'asignado',  )


    





