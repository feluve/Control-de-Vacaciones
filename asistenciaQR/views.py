from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AsistenciaQR
from vacaciones.models import Perfil

import os

# Create your views here.
@login_required
def dispositivo(request):
    print("Vista: dispositivo")
    
    dominio = os.environ.get('DOMINIO')
    dispositivo = request.user.perfil.dispositivo
    
    print('dispositivo: ', dispositivo)
    
    context = {
        'dominio': dominio,
        'dispositivo': dispositivo,
    }
    
    return render(request, 'dispositivo.html', context)

@login_required
def registroDispositivo(request):
    print("Vista: registroDispositivo")
    
    # actualizamo en el Modelo Perfil el estado del dispositivo
    Perfil.objects.filter(usuario=request.user).update(dispositivo="Registrado")
    
    print("[+] Dispositivo registrado con exito")
    
    
    aviso = 'Dispositivo registrado con exito'
    # remplazar de la variable aviso los espacios por guiones bajos
    aviso = aviso.replace(' ', '_')

    return redirect(f'/aviso/{aviso}')

@login_required
def asistenciaQR(request):
    print("Vista: asistenciaQR")
    
    dominio = os.environ.get('DOMINIO')
    
    context = {
        'dominio': dominio,
    }
    
    return render(request, 'asistenciaQR.html', context)


# registro de asistencia por QR
@login_required
def registroAsistenciaQR(request, fecha_hora):
    print("Vista: registroAsistenciaQR")
    
    print('fecha_hora: ', fecha_hora)
    
    # guardamos en el Modelo AsistenciaQR los datos de la asistencia
    AsistenciaQR(usuario=request.user).save()
    
    context = {
    }
    
    aviso = 'Asistencia registrada con exito'
    # remplazar de la variable aviso los espacios por guiones bajos
    aviso = aviso.replace(' ', '_')

    return redirect(f'/aviso/{aviso}')

