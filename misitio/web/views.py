from django.shortcuts import render,redirect
import requests
from web.forms import AgregarTecnicoForm,AsignarForm,ClienteForm,OrdenForm
from web.models import Asignar
from django.contrib import messages









def login(request):
    
    return render(request,"login.html") 


def home(request):
    
    return render(request,"base/home.html") 

def prueba(request):

    return render(request,"base/prueba.html")    


def tecnico(request):

   
    if request.method == 'POST':
        form = AgregarTecnicoForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.tecnico.email = form.cleaned_data.get('email')
            user.tecnico.first_name = form.cleaned_data.get('first_name')
            user.tecnico.direccion  = form.cleaned_data.get('direccion')
            user.tecnico.telefono  = form.cleaned_data.get('telefono')
            user.tecnico.region  = form.cleaned_data.get('region')
            user.tecnico.region  = form.cleaned_data.get('ciudad')
            user.save()
            messages.success(request, 'Tecnico  Agregado')
           
            return redirect('tecnico')
    else:
        form = AgregarTecnicoForm()
    return render(request, 'base/AgregarTecnico.html', {'form': form})


def cliente(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, 'Tecnico  Agregado')
           
            return redirect('cliente')
    else:
        form = ClienteForm()
    return render(request, 'base/AgregarCliente.html', {'form': form})




def asignado(request):
    if request.method == 'POST':
        form = AsignarForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('asignado')
    else:
        form = AsignarForm()
    return render(request, 'base/asignar.html', {'form': form})


def asignado_detail(request, pk):
    form = get_object_or_404(Asignar, pk=pk)
    return render(request, 'base/asignar_detail.html', {'form': form})



def orden_trabajo(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = OrdenForm()
    return render(request, 'base/Orden.html', {'form': form})

              



