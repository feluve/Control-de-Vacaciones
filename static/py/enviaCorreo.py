import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.template.loader import render_to_string


def enviar_correo_simple(subject, msg, para):
    try:
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


def send_email_simple_Plantilla():
    try:
        # print("Peticion eco al servidor de correo...")
        # mailServer = smtplib.SMTP('smtp.hostinger.com', 465)
        # print(mailServer.ehlo())
        # mailServer.starttls()
        # print(mailServer.ehlo())
        # mailServer.login('info@cegmex.com.mx', 'Info123?')
        # print("Servidor acepta eco...")

        print("Peticion eco al servidor de correo...")
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login('feluve22@gmail.com', 'qzhpyygiaqmhatrw')
        print("Servidor acepta eco...")

        mensaje = MIMEMultipart()
        mensaje['From'] = "feluve22@gmail.com"
        mensaje['To'] = "feluve@gmail.com"
        mensaje['Subject'] = "Tienes un correo"

        contenido = render_to_string('send_email.html')
        mensaje.attach(MIMEText(contenido, 'html'))

        mailServer.sendmail("feluve22@gmail.com",
                            "feluve22@gmail.com", mensaje.as_string())

        print("Correo enviado correctamente")

    except Exception as e:
        print(e)


# enviar_correo_simple("Solicitud de vacaciones",
#                      "Esta es una solicitud de vacaciones.", "vacaciones@cegmex.com.mx")
