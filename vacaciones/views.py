from django.shortcuts import render,  redirect
from datetime import date, timedelta, datetime
from vacaciones.models import Solicitud_Vacaciones, Perfil, Dias_Festivos_Oficiales
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth.models import User

from static.py.enviaCorreo import enviar_correo_simple, enviar_correo_plantilla

from static.py.calculaDiasVacacionesLey import calcula_dias_vacaciones_ley
from static.py.calculaFechaVigencia import calcula_fecha_vigencia
from static.py.calculaFechaFinal import calcula_fecha_final

from django.template.loader import render_to_string

import os
import environ


# Create your views here.


@login_required()
def vacaciones(request):

    # cursos = Cursos.objects.all()
    # cursos = Cursos.objects.all()[:5]
    # cursos = Cursos.objects.all().order_by('nombre')
    # cursos = Cursos.objects.all().order_by('-nombre')
    # cursos = Cursos.objects.all().order_by('-creditos')
    # cursos = Cursos.objects.all().order_by('nombre', '-creditos')
    # cursos = Cursos.objects.all().filter(nombre='Español', creditos=10)
    # cursos = Cursos.objects.all().filter(creditos__gte=100)
    # cursos = Cursos.objects.all().filter(creditos__lte=100)
    # cursos = Cursos.objects.all().filter(nombre__contains="e")
    # cursos = Cursos.objects.all().filter(nombre__startswith="E")

    # Valores iniciales de dias
    dias_min_sol = 1
    dias_max_sol = 6
    dias_anticipacion = 15

    # Generamos fecha de acticipacion de solicitud de vacaciones
    fecha_anticipacion = str(date.today() + timedelta(days=dias_anticipacion))

    # Obtenemos fecha de ingreso del usuario
    fecha_ingreso_obj = request.user.perfil.fecha_ingreso
    fecha_ingreso = f"{fecha_ingreso_obj.year}-{fecha_ingreso_obj.month:02}-{fecha_ingreso_obj.day:02}"

    # Verificamos si la fecha de vencimiento ya paso para recalcularle sus dias de vacaciones
    fecha_vigencia_actual = request.user.perfil.vigencia_dias_vacaciones

    # Nos aseguramos que la fecha de vigencia actual no sea nula
    if fecha_vigencia_actual is None:
        fecha_vigencia_actual = request.user.perfil.fecha_ingreso

    # print("")
    # print("Fecha de vigencia actual", fecha_vigencia_actual)
    # print(type(fecha_vigencia_actual))
    # print("Fecha de hoy", datetime.now().date())
    # print("")

    # f1 = datetime.strptime("2024-01-10", '%Y-%m-%d').date()
    # f2 = datetime.strptime("2024-01-11", '%Y-%m-%d').date()

    # if (f1 < f2):
    if (fecha_vigencia_actual < datetime.now().date()):
        print("**************************+***")
        print(
            "Vencio la fecha de vigencia se recalculan dia de vacaiones y fecha de vigencia")
        print("**************************+***")

        dias_disponibles = calcula_dias_vacaciones_ley(fecha_ingreso)
        fecha_vigencia = calcula_fecha_vigencia(fecha_ingreso)

        print(
            f"Ahora tienes {dias_disponibles} dias de vacaciones")
        print(
            f"Con una vigencia de {fecha_vigencia}")

        # Actulizamos los datos en la BD
        Perfil.objects.filter(usuario=User.objects.get(username=request.user).pk).update(
            dias_vacaciones_disp=dias_disponibles, vigencia_dias_vacaciones=fecha_vigencia)

        print("[+] Actualizamos dias disponibles y fecha de vigencia")

    # Obtenemos fecha de vigencia de los dia de vaciones
    # fecha_vigencia_obj = request.user.perfil.vigencia_dias_vacaciones
    fecha_vigencia_obj = Perfil.objects.get(
        pk=User.objects.get(username=request.user).pk).vigencia_dias_vacaciones

    # Obtenemos los dias de vacaciones disponibles
    # dias_disponibles = request.user.perfil.dias_vacaciones_disp
    dias_disponibles = Perfil.objects.get(
        pk=User.objects.get(username=request.user).pk).dias_vacaciones_disp

    # Calculamos cuantos dias como maximo puede seleccionar en base a los que tiene disponibles y los que le corresponde por ley
    print(
        f"El usuario {request.user} tiene {dias_disponibles} dia(s) disponibles")

    if dias_disponibles >= dias_max_sol:
        dias_max_sol = dias_max_sol
    else:
        dias_max_sol = dias_disponibles

    # print(f"dias min: {dias_min_sol}")
    # print(f"dias max: {dias_max_sol}")

    # Consultas a DB
    # Todas las Solicitudes
    todas_solicitudes = Solicitud_Vacaciones.objects.all()

    # Solicitudes enviadas
    solicitudes_enviadas = Solicitud_Vacaciones.objects.filter(
        usuario=request.user)

    # Solicitudes pendientes
    solicitudes_enviadas_pendientes = Solicitud_Vacaciones.objects.filter(
        estado="Pendiente", usuario=request.user)

    # Calculamos cuantos dias disponibles tiene el ususario
    # f1 = fecha_vigencia_obj + timedelta(days=-365)
    # f2 = fecha_vigencia_obj

    # # Consulta de solicitudes aprobadas en el rango de fecha a 1 año atras de la fecha de vencimiento proxima
    # query_solicitudes_enviadas_aprobadas = Solicitud_Vacaciones.objects.all().values('dias').filter(
    #     estado="Aprobada", usuario=request.user, fecha__gte=f1, fecha__lte=f2)

    # Verificamos si el usuario tiene una solictud pendiente o si sus dias siponibles con 0
    if (len(solicitudes_enviadas_pendientes) > 0 or dias_disponibles == 0):
        print(
            f"[-] {request.user} tienes {len(solicitudes_enviadas_pendientes)} solictude(s) pendiente(s) y {dias_disponibles} dia(s) disponible(s)")
        disabled = "disabled"
    else:
        print("[+] No tienes solicitudes pendientes")
        disabled = ""

    # Solicitudes recibidas
    solicitudes_recibidas = Solicitud_Vacaciones.objects.filter(
        jefe__startswith=f"{request.user.first_name} {request.user.last_name}").order_by('-id')

    # Dias festivos oficiales
    lista_dias_festivos = Dias_Festivos_Oficiales.objects.all().order_by('id')

    # Lista de Dias o fechas festivas registradas
    lista_dias_festivos_str = []
    for i in range(len(lista_dias_festivos)):
        lista_dias_festivos_str.append(str(
            lista_dias_festivos.values('dia_festivo')[i]['dia_festivo']))

    # Lista de nombres de la fechas festivas registradas
    lista_nombres_festivos_str = []
    for i in range(len(lista_dias_festivos)):
        lista_nombres_festivos_str.append(str(
            lista_dias_festivos.values('nombre')[i]['nombre']))

    # Solicitudes Aprobadas

    context = {
        "fecha_anticipacion": fecha_anticipacion,
        "fecha_vigencia": str(fecha_vigencia_obj),
        "fecha_vigencia_obj": fecha_vigencia_obj,
        "todas_solicitudes": todas_solicitudes,
        "solicitudes_enviadas": solicitudes_enviadas,
        "solicitudes_recibidas": solicitudes_recibidas,
        "todas_solicitudes_count": len(todas_solicitudes),
        "solicitudes_enviadas_count": len(solicitudes_enviadas),
        "solicitudes_recibidas_count": len(solicitudes_recibidas),
        "usuario_rol": request.user.perfil.rol,
        "disabled": disabled,
        "lista_nombres_festivos_str": lista_nombres_festivos_str,
        "lista_dias_festivos_str": lista_dias_festivos_str,
        "dias_min_sol": dias_min_sol,
        "dias_max_sol": dias_max_sol,
        "dias_disponibles": dias_disponibles
    }

    return render(request, "vacaciones.html", context)


def registra_solicitud(request):

    fecha_solicitud = request.POST["fecha_sol"]
    dias_solicitados = int(request.POST["dias_sol"])

    fecha_final = calcula_fecha_final(fecha_solicitud, dias_solicitados)[0]
    domingos = calcula_fecha_final(fecha_solicitud, dias_solicitados)[1]
    dias_festivos = calcula_fecha_final(fecha_solicitud, dias_solicitados)[2]

    solicitud = Solicitud_Vacaciones.objects.create(
        usuario=request.user.username,
        nombre=f"{request.user.first_name} {request.user.last_name}",
        dias=dias_solicitados,
        fecha_inicio=fecha_solicitud,
        fecha_fin=fecha_final,
        jefe=request.user.perfil.jefe,
        domingos=domingos,
        dias_festivos=dias_festivos,
        estado='Pendiente'
    )

    solicitud.save()
    print(f"[+] Solicitud Registrada para el usuario {request.user.username}")

    id_ultima_solicitud = Solicitud_Vacaciones.objects.latest('id').id
    print(f"Ultimo id: {id_ultima_solicitud}")

    # Notificamos por correo
    if (True):
        # msg = f"{request.user.first_name} {request.user.last_name}:\n Solicita {dias_solicitados} dia(s) de vacaciones, el {fecha_solicitud} al {fecha_final}. \n En espera de aceptación de {request.user.perfil.jefe}."
        # enviar_correo_simple(f"Solicitud de vacaciones # {id_ultima_solicitud}", msg,
        #                      "vacaciones@cegmex.com.mx")

        fecha_solicitud_obj = datetime.strptime(
            fecha_solicitud, '%Y-%M-%d').date()
        fecha_solicitud_srt = f"{fecha_solicitud_obj.day}-{mes_formato(fecha_solicitud_obj.month)}-{fecha_solicitud_obj.year}"

        fecha_final_obj = datetime.strptime(fecha_final, '%Y-%M-%d').date()
        fecha_final_srt = f"{fecha_final_obj.day}-{mes_formato(fecha_final_obj.month)}-{fecha_final_obj.year}"

        context_correo = {
            'usuario': request.user.username,
            'nombre': f"{request.user.first_name} {request.user.last_name}",
            'dias': dias_solicitados,
            # 'fecha_inicio': fecha_solicitud,
            # 'fecha_fin': fecha_final,
            'fecha_inicio': fecha_solicitud_srt,
            'fecha_fin': fecha_final_srt,
            'jefe': request.user.perfil.jefe,
            'domingos': domingos,
            'dias_festivos': dias_festivos,
            'estado': 'Pendiente'
        }

        to = "feluve22@gmail.com"

        correo_contenido = render_to_string(
            'correo2.html', context_correo, request=request)
        enviar_correo_plantilla(correo_contenido, str(
            id_ultima_solicitud), to)

    return redirect('/')


def mes_formato(mes):
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
             "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    return meses[int(mes)-1]


def aprobarSolicitud(request, id):

    # Objenemos solicitud a aprobar
    solicitud = Solicitud_Vacaciones.objects.get(id=id)

    dias_aprobados = solicitud.dias
    usuario = solicitud.usuario

    dias_actuales = Perfil.objects.get(
        usuario=User.objects.get(username=usuario).pk).dias_vacaciones_disp

    dias_actuales = dias_actuales - dias_aprobados

    Perfil.objects.filter(usuario=User.objects.get(username=usuario).pk).update(
        dias_vacaciones_disp=dias_actuales)

    # ----------------------------------
    print("")
    print(solicitud.usuario)
    print("")
    # ----------------------------------

    solicitud.estado = "Aprobada"
    solicitud.save()

    # context_correo = {
    #     'usuario': request.user.username,
    #     'nombre': f"{request.user.first_name} {request.user.last_name}",
    #     'dias': dias_solicitados,
    #     # 'fecha_inicio': fecha_solicitud,
    #     # 'fecha_fin': fecha_final,
    #     'fecha_inicio': fecha_solicitud_srt,
    #     'fecha_fin': fecha_final_srt,
    #     'jefe': request.user.perfil.jefe,
    #     'domingos': domingos,
    #     'dias_festivos': dias_festivos,
    #     'estado': 'Pendiente'
    # }

    # correo_contenido = render_to_string(
    #     'correo2.html', context_correo, request=request)
    # enviar_correo_plantilla(correo_contenido, str(
    #     id_ultima_solicitud), "feluve22@gmail.com, feluve@live.com.mx")

    return redirect('/')


def rechazarSolicitud(request, id):

    solicitud = Solicitud_Vacaciones.objects.get(id=id)
    solicitud.estado = "Rechazada"
    solicitud.save()

    return redirect('/')


def salir(request):

    logout(request)

    return redirect('/')

# -----------------------------------------------------------------
