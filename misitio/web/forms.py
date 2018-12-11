from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from web.models import Tecnico,Cliente,Asignar




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

class AsignarForm(forms.ModelForm):
    class Meta:
        model = Asignar
        fields = ('dia_asc', 'Nom_tecnico', 'Nom_cliente', )

    





