from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from vacaciones.models import Perfil

from static.py.enviaCorreo import enviar_correo_simple, enviar_correo_plantilla

from django.template.loader import render_to_string

import os
import environ

# Create your views here.

# decorador para verificar si usuario tiene el rol de admin o RH
# @ user_passes_test(lambda u: u.perfil.rol == 'admin' or u.perfil.rol == 'RH')


@login_required()
def nuevo_usuario(request):

    # obtenemos del modelo User todos los campos username
    lista_usuarios = User.objects.values_list('username', flat=True)

    # convertimos lista_usuarios a lista del tipo string
    lista_usuarios = list(lista_usuarios)

    # convertimos lista_usuarios a una cadena de texto
    lista_usuarios = str(lista_usuarios)

    context = {
        'lista_usuarios': lista_usuarios
    }

    return render(request, "nuevo_usuario.html", context)


@ login_required()
def guardar_nuevo_usuario(request):

    usuario = request.POST.get("usuario")
    nombre = request.POST.get("nombre")
    apellidos = request.POST.get("apellidos")
    contrasena = request.POST.get("contrasena")
    correo = request.POST.get("correo")
    telefono = request.POST.get("telefono")
    fecha_ingreso = request.POST.get("fecha_ingreso")
    fecha_nacimiento = request.POST.get("fecha_nacimiento")
    jefe = request.POST.get("jefe")
    area = request.POST.get("area")
    dias_vacaciones_disp = 0  # request.POST.get("dias_vacaciones_disp")
    # establecemos que la vigencia de los dias de vacaciones es la fecha de ingreso para que el proximo inicio de sesion calcule los dias de vacaciones y la vigencia
    vigencia_dias_vacaciones = request.POST.get("fecha_ingreso")
    rol = request.POST.get("rol")
    semana = request.POST.get("semana")

    # crear un nuevo usuario del modelo User
    nuevo_usuario = User.objects.create_user(
        username=usuario, first_name=nombre, last_name=apellidos, password=contrasena, email=correo)

    # imprimir en consola usuario guardado con exito
    print("[+] Usuario guardado con exito")

    # # actualizamos el perfil del usuario
    Perfil.objects.filter(usuario=User.objects.get(username=usuario).pk).update(telefono=telefono, fecha_ingreso=fecha_ingreso,
                                                                                fecha_nacimiento=fecha_nacimiento, area=area, dias_vacaciones_disp=dias_vacaciones_disp, vigencia_dias_vacaciones=vigencia_dias_vacaciones, rol=rol, jefe=jefe, semana=semana)

    # # imprimir en consola perfil guardado con exito
    print("[+] Perfil guardado con exito")

    # retonamos al DOMINO mas el path de la vista

    return redirect('/')


# -----------------------Recupracion de contraseña-----------------------

def olvide_contrasena(request):

    # consulta a la base de datos para obtener todos nombres de usuario
    usuarios = list(User.objects.all().values_list('username', flat=True))

    context = {
        'usuarios': usuarios,
        'dominio': os.environ.get('DOMINIO')
    }

    return render(request, 'olvide_contrasena.html', context)


def link_recuperacion(request, usuario):

    # genera un token aleatorio
    token = generar_token()

    # imprime en consola el token
    print("")
    print(f"Token: {token}")
    print("")

    # realiza un update en el modelo perfil para actualizar el campo token
    Perfil.objects.filter(usuario=User.objects.get(
        username=usuario).pk).update(token=token)

    # imrpime en consola
    print("[+] Token actualizado con exito")

    # Obtenermo el nombre completo del usuario
    nombre = f'{User.objects.get(username=usuario).first_name} {User.objects.get(username=usuario).last_name}'

    # Generamos el link de recuperacion
    link = f'{os.environ.get("DOMINIO")}/contrasena_nueva/{usuario}/{token}'

    # imprimir en consola link
    print("")
    print(f"Link: {link}")
    print("")

    context_correo = {
        'nombre': nombre,
        'link': link
    }

    # obtener el nombre de correo del usuario
    correo_usuario = User.objects.get(username=usuario).email

    to = []
    if correo_usuario != None:
        to = [correo_usuario]
    else:
        to = [correo_usuario]

    cc = [os.environ.get('EMAIL_CC')]
    subject = f"Recuperación de contraseña"

    correo_contenido = render_to_string(
        'correo_recuperacion.html', context_correo, request=request)
    enviar_correo_plantilla(correo_contenido, subject, to)

    return redirect('/')


def contrasena_nueva(request, usuario, token):

    # token recibido por parametro
    print(f"Token recibido: {token}")

    # obtener de el modelo Perfil el token del usuario que se recibe por parametro
    token_usuario = Perfil.objects.get(
        usuario=User.objects.get(username=usuario).pk).token

    # token del usuario
    # print(f"Token del usuario: {token_usuario}")

    # si el token del usuario es igual al token que se recibe por parametro
    if token_usuario == token:
        # token valido
        print("[+] Token valido")

        context = {
            'usuario': usuario,
            'token': token
        }

        return render(request, 'contrasena_nueva.html', context)
    else:
        # token invalido
        print("[-] Token invalido o expirado")

        # redireccionar a la pagina link_expirado
        return redirect('/link_expirado')

        # return redirect('/')


def link_expirado(request):

    return render(request, 'link_expirado.html')


def cambiar_contrasena(request, usuario, token, contrasena):

    # imprimimos en consola el token que se recibe por parametro
    print(f"Token recibido: {token}")

    # imprime en consola la contraseña que se recibe por parametro
    print(f"Contraseña encriptada: {contrasena}")

    # desencriptamos la contraseña
    contrasena = desencriptar(contrasena)

    # imprime en consola la contraseña desencriptada
    # print(f"Contraseña desencriptada: {contrasena}")

    # consultamos del modelo Perfil el token del usuario que se recibe por parametro
    token_usuario = Perfil.objects.get(
        usuario=User.objects.get(username=usuario).pk).token

    # imprimimos en consola el token del usuario
    print(f"Token del usuario: {token_usuario}")

    # si el token del usuario es igual al token que se recibe por parametro
    if token_usuario == token:
        # token valido
        print("[+] Token valido")

        # cambiar la contraseña del usuario
        user = User.objects.get(username=usuario)
        user.set_password(contrasena)
        user.save()

        # imprime en consola el usuario y la contraseña
        print(f"Usuario: {usuario} - Contraseña: {contrasena}")
        print("[+] Contraseña cambiada con exito")

        # genra un nuevo token por seguridad
        token_nuevo = generar_token()

        # actializamos el modelo Perfil con el nuevo token
        Perfil.objects.filter(usuario=User.objects.get(
            username=usuario).pk).update(token=token_nuevo)

        # enviamos un correo al usuario indicando que la contraseña fue cambiada con exito
        # creando el contexto del correo

        context_correo = {
            'nombre': f'{user.first_name} {user.last_name}'
        }

        # obtener el nombre de correo del usuario
        correo_usuario = User.objects.get(username=usuario).email

        to = []
        if correo_usuario != None:
            to = [correo_usuario]
        else:
            to = [correo_usuario]

        cc = [os.environ.get('EMAIL_CC')]
        subject = f"Contraseña cambiada"

        correo_contenido = render_to_string(
            'correo_contrasena_cambiada.html', context_correo, request=request)
        enviar_correo_plantilla(correo_contenido, subject, to)

        return redirect('/')

    else:
        # token invalido
        print("[-] Token invalido o ya expiro")
        print("[+] Contraseña no cambiada")

        # retorna a la pagina de 404
        return redirect('/')

# -----------------------Funciones adcionales-----------------------

# funcion que genera una cadena aleatoria de 32 caracteres hexadecimales


def generar_token():
    # import secrets
    import secrets
    return secrets.token_hex(32)

# funcion que desencripta una cadena de texto restandole 3 a cada caracter


def desencriptar(cadena):
    cadena_desencriptada = ""
    for caracter in cadena:
        caracter = ord(caracter) - 3
        caracter = chr(caracter)
        cadena_desencriptada += caracter
    return cadena_desencriptada
