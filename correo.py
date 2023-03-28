import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_correo_simple(subject, msg, to):
    try:
        print("[py<] Enviando correo...")
        # Eco al servidor de correo
        # print("Peticion eco al servidor de correo...")
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login('feluve22@gmail.com', 'qzhpyygiaqmhatrw')
        print("Servidor acepta eco...")

        mensaje = MIMEText(msg)
        mensaje['From'] = 'feluve22@gmail.com'
        mensaje['To'] = ', '.join(to)
        mensaje['Subject'] = subject

        mailServer.sendmail('feluve22@gmail.com',
                            to, mensaje.as_string())

        print(f"[+] Correo {subject} enviado a {to} correctamente.")

    except Exception as e:
        print(e)


subject = "Alertas server"
mensaje = "Servidor reiniciando..."
to = ['feluve22@gmail.com']

enviar_correo_simple(subject, mensaje, to)
