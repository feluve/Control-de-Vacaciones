from datetime import date, timedelta, datetime
import math


def calcula_fecha_vigencia(fecha_ingreso):
    print("Funcion: calcula_fecha_vigencia")

    print("[py<] Calculando fecha de vigencia...")

    fecha_ingreso_obj = datetime.strptime(fecha_ingreso, '%Y-%m-%d').date()
    fecha_actual_obj = datetime.now().date()
    # fecha_actual_obj = datetime.strptime("2025-1-10", '%Y-%m-%d').date()
    diferencia = fecha_actual_obj - fecha_ingreso_obj

    anos = math.ceil(diferencia.days / 365)

    fecha_vencimiento = f"{anos + fecha_ingreso_obj.year}-{fecha_ingreso_obj.month:02}-{fecha_ingreso_obj.day:#02}"

    print(f"Fecha de ingreso: {fecha_ingreso_obj}")
    print(f"Fecha actual: {fecha_actual_obj}")
    print(f"Fecha de vigencia: {fecha_vencimiento}")

    print("[>py]")

    return datetime.strptime(fecha_vencimiento, '%Y-%m-%d').date()


# calcula_fecha_vigencia("2022-01-10")
