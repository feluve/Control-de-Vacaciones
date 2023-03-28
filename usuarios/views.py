from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from vacaciones.models import Perfil

from django.core.files.storage import FileSystemStorage

from static.py.enviaCorreo import enviar_correo_simple, enviar_correo_plantilla

from django.template.loader import render_to_string

import os
import environ

import openpyxl

from datetime import datetime

import urllib

# Create your views here.

# @ user_passes_test(lambda u: u.perfil.rol == 'admin' or u.perfil.rol == 'RH')


def master(request):

    return render(request, 'master.html')


@login_required()
# decorador para verificar si usuario tiene el rol de admin o RH
@user_passes_test(lambda u: u.perfil.rol == 'admin' or u.perfil.rol == 'RH')
def carga_usuarios(request):

    print("")
    print("Carga de usuarios")
    print("")

    # print(request.FILES)
    # print(request.POST)

    if "GET" == request.method:
        return render(request, 'carga_usuarios.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        # you may put validations here to check extension or file size
        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Hoja1"]
        # print(worksheet)

        excel_data = list()
        usuarios_excel = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))

            if row_data[0] == "None":
                print("usuario vacio")
            else:
                excel_data.append(row_data)

        for i in range(0, len(excel_data) - 2):
            usuarios_excel.append(excel_data[i + 2])

        # si el tamaño de usuarios_excel es mayor a 0, guardamos los usuarios en la base de datos
        if len(usuarios_excel) > 0:
            # imprimir en consola los usuarios del excel
            print(usuarios_excel)

            print("Guardando usuarios en la base de datos")
            guardar_usuarios_excel(usuarios_excel)
        else:
            print("No hay usuarios para guardar en la base de datos")

        context = {
            "excel_data": excel_data
        }

        return render(request, 'carga_usuarios.html', context)


# crear una funcion que alamcena los usuarios del excel en la base de datos
def guardar_usuarios_excel(usuarios_excel):

    n_usuarios = 0

    for u in usuarios_excel:

        usuario = u[0].replace(" ", "")
        nombre = u[1]
        apellidos = u[2]
        contrasena = u[3].replace(" ", "")
        correo = u[4].replace(" ", "")
        telefono = u[5].replace(" ", "")
        # convertimos la fecha de ingreso a formato datetime con el formato año-mes-dia
        fecha_ingreso = datetime.strptime(
            u[6].replace(" ", ""), '%Y-%m-%d').date()
        # convertimos la fecha de nacimiento a formato datetime con el formato año-mes-dia
        fecha_nacimiento = datetime.strptime(
            u[7].replace(" ", ""), '%Y-%m-%d').date()
        jefe = u[8]
        area = u[9].replace(" ", "")
        rol = u[10].replace(" ", "")
        semana = u[11].replace(" ", "")

        dias_vacaciones_disp = 0  # request.POST.get("dias_vacaciones_disp")
        # establecemos que la vigencia de los dias de vacaciones es la fecha de ingreso para que el proximo inicio de sesion calcule los dias de vacaciones y la vigencia
        vigencia_dias_vacaciones = fecha_ingreso

        # imagen del usuario
        imagen = u[12].replace(" ", "")

        # imprimir en consola los datos del usuario
        # print("usuario: ", usuario)
        # print("nombre: ", nombre)
        # print("apellidos: ", apellidos)
        # print("contrasena: ", contrasena)
        # print("correo: ", correo)
        # print("telefono: ", telefono)
        # print("fecha_ingreso: ", fecha_ingreso)
        # print("fecha_nacimiento: ", fecha_nacimiento)
        # print("jefe: ", jefe)
        # print("area: ", area)

        # crear un nuevo usuario del modelo User
        nuevo_usuario = User.objects.create_user(
            username=usuario, first_name=nombre, last_name=apellidos, password=contrasena, email=correo)
        # imprimir en consola usuario guardado con exito
        print("[+] Usuario guardado con exito")

        # actualizamos el perfil del usuario
        Perfil.objects.filter(usuario=User.objects.get(username=usuario).pk).update(telefono=telefono, fecha_ingreso=fecha_ingreso,
                                                                                    fecha_nacimiento=fecha_nacimiento, area=area, dias_vacaciones_disp=dias_vacaciones_disp, vigencia_dias_vacaciones=vigencia_dias_vacaciones, rol=rol, jefe=jefe, semana=semana, imagen=imagen)
        # imprimir en consola perfil guardado con exito
        print("[+] Perfil guardado con exito")

        # incrementamos el contador de usuarios
        n_usuarios += 1

    # imprimir en consola el numero de usuarios guardados
    print("Numero de usuarios guardados correctamente: ", n_usuarios)

    return True


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
    rol = request.POST.get("rol")
    semana = request.POST.get("semana")

    dias_vacaciones_disp = 0  # request.POST.get("dias_vacaciones_disp")
    # establecemos que la vigencia de los dias de vacaciones es la fecha de ingreso para que el proximo inicio de sesion calcule los dias de vacaciones y la vigencia
    vigencia_dias_vacaciones = request.POST.get("fecha_ingreso")

    # imagen del usuario
    imagen = request.FILES['imagen']
    fs = FileSystemStorage()
    filename = fs.save(imagen.name, imagen)
    uploaded_file_url = fs.url(filename)

    # crear un nuevo usuario del modelo User
    nuevo_usuario = User.objects.create_user(
        username=usuario, first_name=nombre, last_name=apellidos, password=contrasena, email=correo)
    # imprimir en consola usuario guardado con exito
    print("[+] Usuario guardado con exito")

    # actualizamos el perfil del usuario
    Perfil.objects.filter(usuario=User.objects.get(username=usuario).pk).update(telefono=telefono, fecha_ingreso=fecha_ingreso,
                                                                                fecha_nacimiento=fecha_nacimiento, area=area, dias_vacaciones_disp=dias_vacaciones_disp, vigencia_dias_vacaciones=vigencia_dias_vacaciones, rol=rol, jefe=jefe, semana=semana, imagen=imagen.name)
    # imprimir en consola perfil guardado con exito
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
        'link': link,
        'dominio': os.environ.get('DOMINIO')
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

    aviso = 'Se genero un link de recuperación de contraseña, por favor revisa tu correo'
    # remplazar de la variable aviso los espacios por guiones bajos
    aviso = aviso.replace(' ', '_')

    return redirect(f'/aviso/{aviso}')


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
            'token': token,
            'dominio': os.environ.get('DOMINIO')
        }

        return render(request, 'contrasena_nueva.html', context)
    else:
        # token invalido
        print("[-] Token invalido o expirado")

        aviso = 'El link de recuperación de contraseña a expirado, favor de generar uno nuevo.'
        # remplazar de la variable aviso los espacios por guiones bajos
        aviso = aviso.replace(' ', '_')

        return redirect(f'/aviso/{aviso}')


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

        context = {
            'aviso': 'Contraseña cambiada con exito'
        }
        return render(request, 'aviso.html', context)

    else:
        # token invalido
        print("[-] Token invalido o ya expiro")
        print("[+] Contraseña no cambiada")

        # retorna a la pagina de 404
        context = {
            'aviso': 'Ocurrio un error al cambiar la contraseña'
        }
        return render(request, 'aviso.html', context)


# @login_required()
def aviso(request, aviso):
    context = {
        'aviso': aviso
    }
    return render(request, 'aviso.html', context)

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
