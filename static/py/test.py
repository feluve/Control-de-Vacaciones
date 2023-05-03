def fecha_lunes():
    print("Funcion: fecha_lunes")

    import datetime

    today = datetime.date.today()  # fecha actual
    last_monday = today - \
        datetime.timedelta(days=today.weekday())  # lunes pasado

    # obtener el año, mes y día del lunes pasado
    year = last_monday.year
    month = last_monday.month
    day = last_monday.day

    # crear un objeto datetime con year, month y day
    fecha = datetime.datetime(year, month, day)

    return fecha


print(fecha_lunes())
