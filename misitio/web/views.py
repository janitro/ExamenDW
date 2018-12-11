from django.shortcuts import render,redirect
import requests
from web.forms import AgregarTecnicoForm,AsignarForm,ClienteForm,OrdenForm
from web.models import Asignar,Cliente,Tecnico,OdenDeTrabajo
from django.contrib import messages
# from django.shortcuts import render_to_response, RequestContext
# from push_notifications.models import APNSDevice, GCMDevice









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


def listar_clientes(request):
    posts = OdenDeTrabajo.objects.all()

    return render(request, 'base/listar_orden.html', {'posts': posts})


def lista_asignar(request):
    posts = Asignar.objects.all()

    return render(request, 'base/listar_asignar.html', {'posts': posts})


# def push_notifications_view(request):


#     if request.method == "POST":
#      if 'code' in request.POST:
#       code = request.POST['code']

#     if code == 'android':
#      print 'code == android'
#      devices = GCMDevice.objects.all()
#      devices.send_message({"message": "Hola Android!"})
#      message = "mensaje enviado a los ANDROID"

#     elif code == 'ios':
#       print 'code == ios'
#       devices = APNSDevice.objects.all()
#       devices.send_message("Hola iOS!")
#       message = "mensaje Enviado a los IOS"

#     elif code == 'simple':
#       print 'code == simple'
#       device = APNSDevice.objects.get(registration_id='mi apns token')
#       device.send_message(None, extra={"foo": "bar"})
#       message = "simple message sent"

#     return render_to_response('notificacion_push.html', locals(), context_instance=RequestContext(request))


              



