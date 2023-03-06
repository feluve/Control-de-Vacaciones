import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.template.loader import render_to_string

import os
import environ


def enviar_correo_simple(subject, msg, to):
    try:
        print("[py<] Enviando correo...")
        # Eco al servidor de correo
        # print("Peticion eco al servidor de correo...")
        mailServer = smtplib.SMTP(os.environ.get(
            "EMAIL_HOST"), os.environ.get("EMAIL_PORT"))
        # print(mailServer.ehlo())
        mailServer.starttls()
        # print(mailServer.ehlo())
        mailServer.login(os.environ.get('EMAIL_USERNAME'),
                         os.environ.get('EMAIL_PASSWORD'))
        # print("Servidor acepta eco...")

        mensaje = MIMEText(msg)
        mensaje['From'] = os.environ.get('EMAIL_USER')
        mensaje['To'] = ', '.join(to)
        mensaje['Subject'] = subject

        mailServer.sendmail(os.environ.get('EMAIL_USER'),
                            to, mensaje.as_string())

        print(f"[+] Correo {subject} enviado a {to} correctamente.")

    except Exception as e:
        print(e)


def enviar_correo_plantilla(correo_contenido, subject, to, cc):
    try:
        print("[py<] Enviando correo...")

        # print("Peticion eco al servidor de correo...")
        mailServer = smtplib.SMTP(os.environ.get(
            "EMAIL_HOST"), os.environ.get("EMAIL_PORT"))
        # print(mailServer.ehlo())
        mailServer.starttls()
        # print(mailServer.ehlo())
        mailServer.login(os.environ.get("EMAIL_USERNAME"),
                         os.environ.get("EMAIL_PASSWORD"))
        # print("Servidor acepta eco...")

        # bcc = ['admin@cegmex.com.mx']
        # bcc = [os.environ.get("EMAIL_BCC").split(',')]
        bcc = [os.environ.get("EMAIL_BCC")]

        # print("")
        # print("bcc: ", bcc)
        # print("")

        mensaje = MIMEMultipart()
        mensaje['From'] = os.environ.get("EMAIL_USERNAME")
        mensaje['To'] = ', '.join(to)
        mensaje['Cc'] = ', '.join(cc)
        mensaje['Bcc'] = ', '.join(bcc)
        mensaje['Subject'] = subject

        # contenido = render_to_string('send_email.html')
        mensaje.attach(MIMEText(correo_contenido, 'html'))

        mailServer.sendmail(os.environ.get("EMAIL_USERNAME"),
                            to + cc + bcc, mensaje.as_string())

        print("[>py][+] Notificación por correo enviado correctamente")

    except Exception as e:
        print("[>py][+]Ocurrio un excepccion")
        print(e)
