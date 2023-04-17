from datetime import date, timedelta, datetime
from vacaciones.models import Dias_Festivos_Oficiales

# funcion para calcular fecha final de vacaciones


def calcula_fecha_final(fecha_solicitud, dias_solicitados):
    print("Funcion: calcula_fecha_final")

    print("[py] Calculando fecha final...")

    domingos = 0

    fecha_solicitud_obj = datetime.strptime(fecha_solicitud, '%Y-%m-%d').date()

    for dia in range(dias_solicitados):
        if (fecha_solicitud_obj + timedelta(days=dia)).weekday() == 6:
            print("Encontre domingo en la fecha:",
                  (fecha_solicitud_obj + timedelta(days=dia)))
            domingos += 1

    # ------------------

    # lista_dias_festivos = [
    #     "2023-01-01",
    #     "2023-02-06",
    #     "2023-02-08",
    #     "2023-04-05",
    #     "2023-04-06",
    #     "2023-04-07",
    # ]

    dias_festivos = 0

    # Obtenemos lista de dias festivos registrados
    lista_dias_festivos_query = Dias_Festivos_Oficiales.objects.values(
        'dia_festivo')

    lista_dias_festivos = []
    for i in range(len(lista_dias_festivos_query)):
        lista_dias_festivos.append(
            str(lista_dias_festivos_query[i]['dia_festivo']))

    for dia_s in range(dias_solicitados + domingos):
        fecha_solicitud_obj = datetime.strptime(
            fecha_solicitud, '%Y-%m-%d').date() + timedelta(days=int(dia_s))

        for dia_f in range(len(lista_dias_festivos)):
            if str(fecha_solicitud_obj) == lista_dias_festivos[dia_f]:
                print("Encontre dia festivo en la fecha:",
                      lista_dias_festivos[dia_f])
                dias_festivos += 1

    # -----------------

    fecha_solicitud_obj = datetime.strptime(fecha_solicitud, '%Y-%m-%d').date(
    ) + timedelta(days=int(dias_solicitados + domingos + dias_festivos - 1))

    fecha_final = str(fecha_solicitud_obj)

    # -----------------

    print(
        f"Tu solicitu es por {dias_solicitados} dias en la fecha de {fecha_solicitud}")

    print("Domingos:", domingos)
    print("Dias festivos:", dias_festivos)
    print("Tu fecha final de vacaciones es:", fecha_final)

    return fecha_final, domingos, dias_festivos

# fecha_final = calcula_fecha_final("2023-02-26", 2)[0]
# print(f"Fecha final: {fecha_final}")
