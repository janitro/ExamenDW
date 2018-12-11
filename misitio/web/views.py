from django.shortcuts import render
import requests
from web.forms import AgregarTecnicoForm,AsignarForm
from web.models import Asignar








def login(request):
    
    return render(request,"login.html") 


def home(request):
    
    return render(request,"base/home.html") 


def tecnico(request):

   
    if request.method == 'POST':
        form = AgregarTecnicoForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
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

              



