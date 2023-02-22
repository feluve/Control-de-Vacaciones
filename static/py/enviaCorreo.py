import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.template.loader import render_to_string


def enviar_correo_simple(subject, msg, para):
    try:
        print("[py<] Enviando correo...")
        # Eco al servidor de correo
        # print("Peticion eco al servidor de correo...")
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        # print(mailServer.ehlo())
        mailServer.starttls()
        # print(mailServer.ehlo())
        mailServer.login('feluve22@gmail.com', 'afgdzyikzymhszjo')
        # print("Servidor acepta eco...")

        mensaje = MIMEText(msg)
        mensaje['From'] = "feluve22@gmail.com"
        mensaje['To'] = para
        mensaje['Subject'] = subject

        mailServer.sendmail(para,
                            para, mensaje.as_string())

        print(f"[+] Correo {subject} enviado a {para} correctamente.")

    except Exception as e:
        print(e)


def enviar_correo_plantilla(correo_contenido, id_solicitud, to):
    try:
        print("[py<] Enviando correo...")

        # print("Peticion eco al servidor de correo...")
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        # print(mailServer.ehlo())
        mailServer.starttls()
        # print(mailServer.ehlo())
        mailServer.login('feluve22@gmail.com', 'qzhpyygiaqmhatrw')
        # print("Servidor acepta eco...")

        mensaje = MIMEMultipart()
        mensaje['From'] = "feluve22@gmail.com"
        mensaje['To'] = to
        # mensaje['Cc'] = ""
        mensaje['Subject'] = "Solicitud de vacaciones # " + id_solicitud

        # contenido = render_to_string('send_email.html')
        mensaje.attach(MIMEText(correo_contenido, 'html'))

        mailServer.sendmail("feluve22@gmail.com",
                            to, mensaje.as_string())

        print("[>py][+] Notificación por correo enviado correctamente")

    except Exception as e:
        print("[>py][+]Ocurrio un excepccion")
        print(e)
