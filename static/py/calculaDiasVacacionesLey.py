from datetime import date, datetime


def calcula_dias_vacaciones_ley(fecha_ingreso):
    print("Funcion: calcula_dias_vacaciones_ley")

    print("[py] Calculando dias de vacaciones...")

    fecha_ingreso_obj = datetime.strptime(fecha_ingreso, "%Y-%m-%d")

    # fecha_actual_obj = datetime.strptime("2023-02-16", "%Y-%m-%d")
    fecha_actual_obj = datetime.now()

    diferencia = fecha_actual_obj - fecha_ingreso_obj

    antiguedad_anos = int(diferencia.days / 365)
    antiguedad_dias = diferencia.days % 365

    print(
        f"Tu antiguedad es de {antiguedad_anos} año(s) y {antiguedad_dias} dias")

    if antiguedad_anos == 0:
        dias_vacaciones = 0
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif antiguedad_anos == 1:
        dias_vacaciones = 12
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif antiguedad_anos == 2:
        dias_vacaciones = 14
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif antiguedad_anos == 3:
        dias_vacaciones = 16
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif antiguedad_anos == 4:
        dias_vacaciones = 18
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif (antiguedad_anos == 5):
        dias_vacaciones = 20
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif (antiguedad_anos >= 6 and antiguedad_anos <= 10):
        dias_vacaciones = 22
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif (antiguedad_anos >= 11 and antiguedad_anos <= 15):
        dias_vacaciones = 24
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif (antiguedad_anos >= 16 and antiguedad_anos <= 20):
        dias_vacaciones = 26
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif (antiguedad_anos >= 21 and antiguedad_anos <= 25):
        dias_vacaciones = 28
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif (antiguedad_anos >= 26 and antiguedad_anos <= 30):
        dias_vacaciones = 30
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones
    elif (antiguedad_anos >= 31 and antiguedad_anos <= 35):
        dias_vacaciones = 32
        print(f"Tines {dias_vacaciones} dias de vacaciones por ley")
        print("[>py]")
        return dias_vacaciones


# input("Ingresa tu fecha de ingreso a la empresa: ")
# f = input("Ingresa tu fecha de ingreso a la empresa: ")

# calcula_dias_vacaciones_ley(f)
