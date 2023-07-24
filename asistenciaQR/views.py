from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AsistenciaQR, Dispositivo
from vacaciones.models import Perfil

import os
from datetime import datetime

# Create your views here.
@login_required
def dispositivo(request):
    print("Vista: dispositivo")
    
    # validamos que el usuario tenga dispositivo
    dispositivo = Dispositivo.objects.filter(usuario=request.user)
    
    if dispositivo.count() == 0:
        print("[-] El usuario no tiene dispositivo")
        
        context = {
            "dispositivo": "No"
        }
        
        return render(request, 'dispositivo.html', context)
    else:
        
        # si tiene dispositivo el usuario
        # verificamos que el dispositivo este registrado
        if request.user.dispositivo.estado == 'Registrado':
            print("[+] El usuario tiene dispositivo registrado")
            
            context = {
            
            }
            
            return render(request, 'asistenciaQR.html', context)
        else:
            print("[-] El usuario tiene dispositivo pero no esta registrado")
            
            context = {
                "dispositivo": "No"
            }
            
            return render(request, 'dispositivo.html', context)
    

@login_required
def registroDispositivo(request, pantalla, plataforma, nucleos):
    print("Vista: registroDispositivo")
    
    # verificanos si el usuario tiene dispositivo registrado
    dispositivo = Dispositivo.objects.filter(usuario=request.user)

    # si el usuario no tiene dispositivo registrado
    if dispositivo.count() == 0:
        # le creamos un dispositivo en la tabla Dispositivo
        Dispositivo.objects.create(usuario=request.user, estado='Registrado', pantalla=pantalla, plataforma=plataforma, nucleos=nucleos)
        
        print("[+] Dispositivo registrado con exito")
    
        aviso = 'Dispositivo registrado con exito'
        # remplazar de la variable aviso los espacios por guiones bajos
        aviso = aviso.replace(' ', '_')

        return redirect(f'/aviso/{aviso}')
    else:
        print("[+] El usuario ya tiene un dispositivo registrado solo se actualiza el estado")
        
        # actualizamos el estado del dispositivo
        Dispositivo.objects.filter(usuario=request.user).update(estado='Registrado')
        
        aviso = 'Dispositivo registrado con exito'
        # remplazar de la variable aviso los espacios por guiones bajos
        aviso = aviso.replace(' ', '_')

        return redirect(f'/aviso/{aviso}')
        

@login_required
def asistenciaQR(request):
    print("Vista: asistenciaQR")
    
    context = {
        
    }
    
    return render(request, 'asistenciaQR.html', context)


# registro de asistencia por QR
@login_required
def registroAsistenciaQR(request, fecha_hora):
    print("Vista: registroAsistenciaQR")
    
    # convertimos la fecha_hora en un objeto datetime
    fecha_hora = datetime.strptime(fecha_hora, '%Y-%m-%d-%H-%M-%S')
    print('fecha_hora: ', fecha_hora)
    
    # obtenemos la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # si la fecha de fecha_hora es igual a la fecha_hora_actual
    if fecha_hora.date() == fecha_hora_actual.date():
        print("[+] La fecha coincide")
        
        # obtenemos los segundos totales de la fecha_hora
        segundos_fecha_hora = fecha_hora.time().hour * 3600 + fecha_hora.time().minute * 60 + fecha_hora.time().second
        # obtenemos los segundos totales de la fecha_hora_actual
        segundos_fecha_hora_actual = fecha_hora_actual.time().hour * 3600 + fecha_hora_actual.time().minute * 60 + fecha_hora_actual.time().second
        
        print("diferencia de segundos: ", segundos_fecha_hora_actual - segundos_fecha_hora)
        
        # Rango mas o menos de 30 segundos
        rango = 30
        # si la diferencia de segundos es menor igual a rango segundos
        if ((segundos_fecha_hora_actual - segundos_fecha_hora) <= rango) and ((segundos_fecha_hora_actual - segundos_fecha_hora) >= -rango):
            
            print("[+] La hora esta en el rango de: ", rango, " segundos")
            
            # registramos la asistencia en el Modelo AsistenciaQR
            AsistenciaQR(usuario=request.user).save()
            print("[+] Asistencia registrada con exito")
            
            # preparamos el aviso
            aviso = f"Asistencia registrada con exito para la fecha y hora: {fecha_hora}"
            # remplazar de la variable aviso los espacios por guiones bajos
            aviso = aviso.replace(' ', '_')

            return redirect(f'/aviso/{aviso}')
        
        else:
            print("[-] La hora no esta en el rango de: ", rango, " segundos")
            
            # preparamos el aviso
            aviso = 'No se pudo registrar la asistencia'
            # remplazar de la variable aviso los espacios por guiones bajos
            aviso = aviso.replace(' ', '_')

            return redirect(f'/aviso/{aviso}')

    else:
        
        print("[-] La fecha no coincide con la fecha actual de : ", fecha_hora_actual.date())
        
        # preparamos el aviso
        aviso = 'No se pudo registrar la asistencia'
        # remplazar de la variable aviso los espacios por guiones bajos
        aviso = aviso.replace(' ', '_')

        return redirect(f'/aviso/{aviso}')

