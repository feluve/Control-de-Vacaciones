from django.shortcuts import render,  redirect
from datetime import date, timedelta, datetime
from vacaciones.models import Solicitud_Vacaciones, Perfil, Dias_Festivos_Oficiales
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth.models import User

from static.py.calculaFechaFinal import calcula_fecha_final
from static.py.calculaDiasVacacionesLey import calcula_dias_vacaciones_ley
from static.py.enviaCorreo import enviar_correo_simple

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

    dias_anticipacion = 15

    fecha_anticipacion = str(date.today() + timedelta(days=dias_anticipacion))

    fecha_ingreso = request.user.perfil.fecha_ingreso
    fecha_vigencia_dias_vacaciones = str(date.today().year) + "-" + \
        str(fecha_ingreso.month) + "-" + str(fecha_ingreso.day)

    fecha_vigencia_dias_vacaciones = datetime.strptime(
        fecha_vigencia_dias_vacaciones, '%Y-%m-%d').date()

    # Consultas a DB
    # Todas las Solicitudes
    todas_solicitudes = Solicitud_Vacaciones.objects.all()

    # Solicitudes enviadas
    solicitudes_enviadas = Solicitud_Vacaciones.objects.filter(
        usuario=request.user)

    # Solicitudes pendientes
    solicitudes_enviadas_pendientes = Solicitud_Vacaciones.objects.filter(
        estado="Pendiente", usuario=request.user)

    # Solicitudes recibidas
    solicitudes_recibidas = Solicitud_Vacaciones.objects.filter(
        jefe__startswith=f"{request.user.first_name} {request.user.last_name}").order_by('-id')

    # Dias festivos oficiales
    lista_dias_festivos = Dias_Festivos_Oficiales.objects.all().order_by('id')
    # print(lista_dias_festivos)

    # Verificamos si el usuario tiene una solictud pendiente
    if len(solicitudes_enviadas_pendientes) > 0:
        print(
            f"[-] Tienes {len(solicitudes_enviadas_pendientes)} solictudes pendientes")
        disabled = "disabled"
    else:
        print("[+] No tienes solicitudes pendientes")
        disabled = ""

    context = {
        "fecha_anticipacion": fecha_anticipacion,
        "fecha_vigencia_dias_vacaciones": fecha_vigencia_dias_vacaciones,
        "todas_solicitudes": todas_solicitudes,
        "solicitudes_enviadas": solicitudes_enviadas,
        "solicitudes_recibidas": solicitudes_recibidas,
        "todas_solicitudes_count": len(todas_solicitudes),
        "solicitudes_enviadas_count": len(solicitudes_enviadas),
        "solicitudes_recibidas_count": len(solicitudes_recibidas),
        "usuario_rol": request.user.perfil.rol,
        "disabled": disabled,
        "lista_dias_festivos": lista_dias_festivos,
        "n_lista_dias_festivos": len(lista_dias_festivos)
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
    if (False):
        msg = f"{request.user.first_name} {request.user.last_name}:\n Solicita {dias_solicitados} dia(s) de vacaciones, el {fecha_solicitud} al {fecha_final}. \n En espera de aceptación de {request.user.perfil.jefe}."
        enviar_correo_simple(f"Solicitud de vacaciones # {id_ultima_solicitud}", msg,
                             "vacaciones@cegmex.com.mx")

    return redirect('/')


def aprobarSolicitud(request, id):

    solicitud = Solicitud_Vacaciones.objects.get(id=id)
    solicitud.estado = "Aprobada"
    solicitud.save()

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


def calculo_vacaciones(fecha_solicitud, dias_solicitados):
    # Verificamos si hay domingos
    # def hay_domingo(fecha_solicitud, dias_solicitados):
    domingos = 0

    fecha_solicitud_obj = datetime.strptime(fecha_solicitud, '%Y-%m-%d').date()

    for dia in range(dias_solicitados):
        if (fecha_solicitud_obj + timedelta(days=dia)).weekday() == 6:
            print("Encontre domingo en la fecha:",
                  (fecha_solicitud_obj + timedelta(days=dia)))
            domingos += 1

    # return domingos


# Verificamos si hay dias festivos
# def hay_dias_festivos(fecha_solicitud, dias_solicitados):
    dias_festivos = 0

    agno = str(date.today().year)

    lista_dias_festivos = [
        agno+('-01-01'),
        agno+('-02-06'),
        agno+('-02-24'),
        agno+('-04-05'),
        agno+('-04-06'),
        agno+('-04-07')
    ]

    for dia_s in range(dias_solicitados):
        fecha_solicitud_obj = datetime.strptime(
            fecha_solicitud, '%Y-%m-%d').date() + timedelta(days=int(dia_s))

        for dia_f in range(len(lista_dias_festivos)):
            if str(fecha_solicitud_obj) == lista_dias_festivos[dia_f]:
                print("Encontre dia festivo en la fecha:",
                      lista_dias_festivos[dia_f])
                dias_festivos += 1

    # return dias_festivos


# Calculamos la fecha final de vacaciones
# def calcula_fecha_final(fecha_solicitud, dias_solicitados, domingos, dias_festivos):
    fecha_final_obj = datetime.strptime(fecha_solicitud, '%Y-%m-%d').date(
    ) + timedelta(days=int(dias_solicitados + domingos + dias_festivos - 1))

    print("*****************")
    print(
        f"Tu solicitu es por {dias_solicitados} dias en la fecha de {fecha_solicitud}")

    print("Domingos:", domingos)
    print("Dias festivos:", dias_festivos)
    print("Tu fecha final de vacaciones es:", str(fecha_final_obj))
    print("*****************")
