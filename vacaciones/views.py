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
import uuid


@login_required()
def vacaciones(request):
    print("Vista: vacaciones")

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

    # obtiene el numero minimo de dias de vacaciones por solicitud de la variable de entorno en entero
    dias_min_sol = int(os.environ.get('DIAS_MIN_SOLICITUD'))

    # obtiene el numero maximo de dias de vacaciones por solicitud de la variable de entorno en entero
    dias_max_sol = int(os.environ.get('DIAS_MAX_SOLICITUD'))

    # obtiene el numero de dias de anticipacion para solicitar vacaciones de la variable de entorno en entero
    dias_anticipacion = int(os.environ.get('DIAS_ANTICIPACION'))

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
            "Vencio la fecha de vigencia se recalculan dia de vacaciones y fecha de vigencia")
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
    if (len(solicitudes_enviadas_pendientes) > 0 or dias_disponibles <= 0):
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
        "disabled": disabled,
        "lista_nombres_festivos_str": lista_nombres_festivos_str,
        "lista_dias_festivos_str": lista_dias_festivos_str,
        "dias_min_sol": dias_min_sol,
        "dias_max_sol": dias_max_sol,
        "dias_disponibles": dias_disponibles,
        "dominio": os.environ.get("DOMINIO")
    }

    return render(request, "vacaciones.html", context)


@login_required()
def registra_solicitud(request, dias_solicitados, fecha_solicitud, fecha_final, comentario_solicitud):
    print("Vista: registra_solicitud")

    # fecha_solicitud = request.POST["fecha_sol"]
    # dias_solicitados = int(request.POST["dias_sol"])
    # comentario_solicitud = request.POST["comentario_solicitud"]

    # fecha_final = calcula_fecha_final(fecha_solicitud, dias_solicitados)[0]
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
        estado='Pendiente',
        comentario_solicitud=comentario_solicitud
    )

    solicitud.save()
    print(f"[+] Solicitud Registrada para el usuario {request.user.username}")

    id_ultima_solicitud = Solicitud_Vacaciones.objects.latest('id').id
    # print(f"Ultimo id: {id_ultima_solicitud}")

    # Consulta cual es el nombre jefe del usuario
    # jefe_usuario = request.user.perfil.jefe
    # print(f"Nombre del jefe: {jefe_usuario.split(' ')[0]}")
    # correo_jefe = User.objects.get(
    #     first_name=request.user.perfil.jefe.split(' ')[0]).email
    # print(f"Correo del jefe: {correo_jefe}")

    # Notificamos por correo del registro de la solicitud
    if (os.environ.get('NOTIFICACIONES')):

        context_correo = {
            'usuario': request.user.username,
            'nombre': f"{request.user.first_name} {request.user.last_name}",
            'dias': dias_solicitados,
            'fecha_inicio': fecha_str_format(fecha_solicitud),
            'fecha_fin': fecha_str_format(fecha_final),
            'jefe': request.user.perfil.jefe,
            'domingos': domingos,
            'dias_festivos': dias_festivos,
            'estado': 'Pendiente',
            'comentario_solicitud': comentario_solicitud
        }

        correo_jefe = User.objects.get(
            first_name=request.user.perfil.jefe.split(' ')[0]).email

        to = []
        if correo_jefe != None:
            to = [request.user.email, correo_jefe]
        else:
            to = [request.user.email]

        subject = f"Registro de solicitud # {id_ultima_solicitud}"

        correo_contenido = render_to_string(
            'correo_resgitro_solicitud.html', context_correo, request=request)
        enviar_correo_plantilla(correo_contenido, subject, to, cc_flag=True)

    aviso = 'Solicitud registrada con exito.'
    # remplazar de la variable aviso los espacios por guiones bajos
    aviso = aviso.replace(' ', '_')

    return redirect(f'/aviso/{aviso}')


@login_required()
def aprobarSolicitud(request, id, comentario):
    print("Vista: aprobarSolicitud")

    # Obtenemos solicitud a aprobar
    solicitud = Solicitud_Vacaciones.objects.get(id=id)

    dias_aprobados = solicitud.dias
    usuario = solicitud.usuario

    dias_actuales = Perfil.objects.get(
        usuario=User.objects.get(username=usuario).pk).dias_vacaciones_disp

    dias_actuales = dias_actuales - dias_aprobados

    # Actualizamos dias disponibles
    Perfil.objects.filter(usuario=User.objects.get(username=usuario).pk).update(
        dias_vacaciones_disp=dias_actuales)

    solicitud.estado = "Aprobada"
    solicitud.comentario_jefe = comentario
    solicitud.save()

    # Notificamos por correo de la aprobacion de la solicitud
    if (os.environ.get('NOTIFICACIONES')):

        context_correo = {
            'nombre': solicitud.nombre,
            'dias': solicitud.dias,
            'fecha_inicio': fecha_obj_str_format(solicitud.fecha_inicio),
            'fecha_fin': fecha_obj_str_format(solicitud.fecha_fin),
            'jefe': solicitud.jefe,
            'comentario_jefe': solicitud.comentario_jefe,
            'estado': solicitud.estado
        }

        # obtenemos del modelo User el correo de la persona que realizo la solicitud
        correo_usuario = User.objects.get(username=solicitud.usuario).email

        to = []
        if correo_usuario != None:
            to = [request.user.email, correo_usuario]
        else:
            to = [request.user.email]

        subject = f"Solicitud # {solicitud.id} {solicitud.estado}"

        correo_contenido = render_to_string(
            'correo_estado_solicitud.html', context_correo, request=request)
        enviar_correo_plantilla(correo_contenido, subject, to, cc_flag=True)

    aviso = 'Solicitud aprobada con exito.'
    # remplazar de la variable aviso los espacios por guiones bajos
    aviso = aviso.replace(' ', '_')

    return redirect(f'/aviso/{aviso}')


@login_required()
def rechazarSolicitud(request, id, comentario):
    print("Vista: rechazarSolicitud")

    solicitud = Solicitud_Vacaciones.objects.get(id=id)
    solicitud.estado = "Rechazada"
    solicitud.comentario_jefe = comentario
    solicitud.save()

    # Notificamos por correo de la aprobacion de la solicitud
    if (os.environ.get('NOTIFICACIONES')):

        context_correo = {
            'nombre': solicitud.nombre,
            'dias': solicitud.dias,
            'fecha_inicio': fecha_obj_str_format(solicitud.fecha_inicio),
            'fecha_fin': fecha_obj_str_format(solicitud.fecha_fin),
            'jefe': solicitud.jefe,
            'comentario_jefe': solicitud.comentario_jefe,
            'estado': solicitud.estado
        }

        # obtenemos del modelo User el correo de la persona que realizo la solicitud
        correo_usuario = User.objects.get(username=solicitud.usuario).email

        # imprimir correo
        print(f"Correo del usuario: {correo_usuario}")

        to = []

        if correo_usuario != None:
            to = [request.user.email, correo_usuario]
        else:
            to = [request.user.email]

        cc = [os.environ.get('EMAIL_CC')]
        subject = f"Solicitud # {solicitud.id} {solicitud.estado}"

        correo_contenido = render_to_string(
            'correo_estado_solicitud.html', context_correo, request=request)
        enviar_correo_plantilla(correo_contenido, subject, to, cc_flag=True)

    aviso = 'Solicitud rechazada con exito.'
    # remplazar de la variable aviso los espacios por guiones bajos
    aviso = aviso.replace(' ', '_')

    return redirect(f'/aviso/{aviso}')


def salir(request):
    print("Vista: salir")

    logout(request)

    return redirect('/')

# -------------------------------------------------------------------------------------
# Funciones adicionales

# funcion que recibe el numero del mes y lo convierte en nombre del mes


def mes_formato(mes):
    print("Funcion: mes_formato")

    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    return meses[mes]

# funcion que reciba un fecha en cadena y la conveirte en formato dias mes año


def fecha_str_format(fecha):
    print("Funcion: fecha_str_format")

    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
    fecha_srt = f"{fecha_obj.day}-{mes_formato(fecha_obj.month)[:3]}-{fecha_obj.year}"
    return fecha_srt

# funcion que recibe una fecha en objeto date y la convierte en cadena en el formato dias nombre mes año


def fecha_obj_str_format(fecha_obj):
    print("Funcion: fecha_obj_str_format")

    fecha_srt = f"{fecha_obj.day}-{mes_formato(fecha_obj.month)[:3]}-{fecha_obj.year}"
    return fecha_srt
