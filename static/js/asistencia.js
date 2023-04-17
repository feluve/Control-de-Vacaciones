window.addEventListener("load", (event) => {
    console.log("Pagina asistencia cargada completamente.");


    // colocamos la fecha del lunes de la semana pasada en el input de fecha
    document.getElementById("fecha").value = fecha_lunes_semana_pasado();

});

// funcion que obtiene la fecha del todos los lunes de la semana pasada
function fecha_lunes_semana_pasado() {
    var today = new Date();
    var lastMonday = new Date(today.getFullYear(), today.getMonth(), today.getDate() - today.getDay() - 6);

    // convertir lastMonday a formato string y asegurar que tenga el año con 4 digitos el mes a 2 digitos y el dia a 2 digitos
    var fecha = lastMonday.getFullYear() + "-" + ("0" + (lastMonday.getMonth() + 1)).slice(-2) + "-" + ("0" + lastMonday.getDate()).slice(-2);

    // console.log(fecha);

    return fecha;
}   