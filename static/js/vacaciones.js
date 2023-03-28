
window.addEventListener("load", (event) => {
    console.log("Pagina cargada completamente.");

    document.getElementById("num_dias_sol").value = document.getElementById('-').getAttribute('data-dias_min_sol')

});

function resta_dias(){

    const dias_min = parseInt(document.getElementById("-").getAttribute("data-dias_min_sol"));
    // console.log(min_dias);

    if (parseInt(document.getElementById('num_dias_sol').value) > dias_min) {
        document.getElementById('num_dias_sol').value = parseInt(document.getElementById('num_dias_sol').value) -1;
        console.log("Restamos");
    }
}

function suma_dias(){

    const dias_max = parseInt(document.getElementById("+").getAttribute("data-dias_max_sol"));
    // console.log(max_dias);

    if (parseInt(document.getElementById('num_dias_sol').value) < dias_max) {
        document.getElementById('num_dias_sol').value = parseInt(document.getElementById('num_dias_sol').value) +1;
        console.log("Sumamos");
    }
}

function validaciones(dias_festivos_str, nombres_festivos_str, dias_max_sol, semana, dominio){

    console.log("Realizando validaciones...");

    // console.log(dias_festivos_str)
    // console.log(nombres_festivos_str)

    let { dia_festivo , nombre_dia_festivo} = verifica_fecha_festiva(dias_festivos_str, nombres_festivos_str);

    const dias_disp = parseInt(document.getElementById('dias_disp').innerText);
    const dias_sol = parseInt(document.getElementById('num_dias_sol').value);

    const fecha_sol_str = document.getElementById('fecha_sol').value;
    const fecha_sol_obj = new Date(fecha_sol_str);

    const fecha_actual_obj = new Date();

    const obj_date = document.getElementById("fecha_sol");
    const fecha_vigencia_str = obj_date.getAttribute('max');
    // const fecha_vigencia_obj = new Date (fecha_vigencia_str);
    const fecha_acticipacion_str = obj_date.getAttribute('min');
    // const fecha_acticipacion_obj = new Date (fecha_acticipacion_str);

    const solicitudes_pendientes = 0;

    
    // Validamos que no seleccionen mas dias
    if(dias_sol > parseInt(dias_max_sol)){
        
        swal({
            title: 'Información',
            text: 'No puede seleccionar más de' + dias_max_sol + ' dias.',
            icon: 'error',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que tenga una fecha seleccionada
    else if(fecha_sol_str.length == 0){
        // console.log("fecha nula")

        swal({
            title: 'Información',
            text: 'Debe seleccionar una fecha.',
            icon: 'warning',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que la fecha seleccionado sea mayor o igual a la fecha de acticipacion
    else if(diferencia_dias(fecha_acticipacion_str, fecha_sol_str) > 0){

        swal({
            title: 'Fecha inválida',
            text: 'La fecha seleccionada debe ser a partir de la fecha de anticipación: ' + format_fecha(fecha_acticipacion_str) + '.',
            icon: 'error',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que la fecha seleccionado no sea mayor  a la fecha vencimiento de sus dias de vacacioens
    else if(diferencia_dias(fecha_vigencia_str, fecha_sol_str) < 0){

        swal({
            title: 'Fecha inválida',
            text: 'La fecha seleccionada no debe ser mayor a la fecha de la vigencia de sus dias: ' + format_fecha(fecha_vigencia_str) + '.',
            icon: 'error',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que la fecha seleccionado no sea una fecha festiva oficial
    else if(dia_festivo){

        swal({
            title: 'Fecha festiva',
            text: 'La fecha seleccionada es una fecha festiva: '+ nombre_dia_festivo +'. Selecciona una fecha diferente.',
            icon: 'warning',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que tiene dias disponibles suficientes
    else if(dias_sol > dias_disp ){

        swal({
            title: 'Información',
            text: 'Estas solicitando ' + dias_sol +' dia(s) y solo cuentas con ' + dias_disp + ' dia(s) disponibles.',
            icon: 'warning',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que si es la semana Inglesa y fecha_sol_obj es sabado
    else if(semana == "Inglesa" && fecha_sol_obj.getDay() == 5){

        swal({
            title: 'Información',
            text: 'La fecha seleccionada es Sábado. Selecciona una feche entre Lunes y Viernes.',
            icon: 'warning',

            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que la fecha seleccionado no se domingo
    else if (fecha_sol_obj.getDay() == 6){

        swal({
            title: 'Información',
            // text: 'La fecha '+ document.getElementById('fecha_sol').value +' seleccionada es Domingo. Selecciona una fecha diferente.',
            text: 'La fecha seleccionada es Domingo. Selecciona una fecha diferente.',
            icon: 'warning',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Confimamos el envio de la solicitud
    else{

        const fecha_final = calcula_fecha_final(dias_festivos_str, nombres_festivos_str, semana);
        
        // si dias_sol es 1 
        if(dias_sol == 1){
            var fecha_final_str = fecha_sol_str
            var text = 'Esta seguro de enviar la solicitud por '+ dias_sol +' dia en la fecha ' + format_fecha(fecha_sol_str) + ' ?';
            
        // si dias_sol es mayor a 1
        } else {
            // calcula fecha final y la conviente en string en formato año-mes-dia
            var fecha_final_str = calcula_fecha_final(dias_festivos_str, nombres_festivos_str, semana);
            var text = 'Esta seguro de enviar la solicitud por '+ dias_sol +' dias en la fecha ' + format_fecha(fecha_sol_str) + ' al ' + format_fecha(fecha_final_str) + ' ?';
        }
        
        swal({
            title: 'Confirmación',
            text: text,
            icon: 'success',
    
            buttons: {
                No: "No",
                Si: "Si"
            },
        })

        .then((value) => {
            switch (value) {

                case "Si":

                    // Activamos campo de numero para que se pueda mandar por post
                    document.getElementById('num_dias_sol').disabled = false;

                    // Enviamos los datos por POST
                    // document.getElementById('form').submit();
                    // console.log('Se envio la solictud');

                    let comentario = document.getElementById('comentario_solicitud').value;

                    // si el comentario esta vacio
                    if(comentario.length == 0){
                        comentario = '-';
                    }

                    // creamos una url con el dominio, dias_sol, fecha_sol_str, fecha_final_srt y comentario
                    let url = dominio + '/registra_solicitud/' + dias_sol + '/' + fecha_sol_str + '/' + fecha_final_str + '/' + comentario;

                    // imprimimos la url junto a url
                    // console.log(url);

                    // enlazamos a la url
                    window.location.href = url;

                    break;

                case "No":
                    console.log('No se enevio la solitud');
                    break;
                    
                }
        })
            
    }
}
    
function verifica_fecha_festiva(dias_festivos_str, nombres_festivos_str){

    console.log("Verificando fecha festiva...");

    // console.log(dias_festivos_str)
    // console.log(nombres_festivos_str)

    const fecha_sol_obj = document.getElementById('fecha_sol').value.trim();
    
    let nombres_festivos_obj = nombres_festivos_str.replace("[", "").replace("]", "").replace(/[']+/g, "").split(",");
    let dias_festivos_obj = dias_festivos_str.replace("[", "").replace("]", "").replace(/[']+/g, "").split(",");

    let dia_festivo = false;
    let nombre_dia_festivo = "";
    let i = 0;

    for(i; i < dias_festivos_obj.length; i++){
        if(fecha_sol_obj === dias_festivos_obj[i].trim()){        
            dia_festivo = true;
            nombre_dia_festivo = nombres_festivos_obj[i]
            
            console.log("Encontre fecha festiva:");
            console.log(dias_festivos_obj[i] + " " + nombres_festivos_obj[i]);

            break;
        }
    }

    if(!dia_festivo){
        console.log("No se encontraron fechas festivas");
    }

    return {dia_festivo, nombre_dia_festivo};
}

function confirmacionAprobar(id){
    
  // const solicitud = document.querySelector("#go");
// const url = "aprobarSolicitud/" + solicitud.dataset.id.toString();

let comentario = "";

swal({
    title: 'Comentario opccional',
    icon: 'info',
    content: {
        element: "input",
        attributes: {
          placeholder: "Deja un comentario",
        },
      },
  })

  .then((value) => {

    if (value  == "") {
        value = "-";
    } 

    // console.log(value);

    const url = "aprobarSolicitud/" + id.toString() + "/" + value.toString();
    // console.log(url);

    swal({
        title: 'Confirmación',
        text: 'Esta seguro de Aprobar la solicitud?',
        icon: 'success',

        buttons: {
            No: "No",
            Si: "Si"
        },
    })

    .then((value) => {
        switch (value) {

            case "Si":
                window.location.href = url;
                // console.log('Se confirmo el Rechazo de la solictud ' + id);

                break;

            case "No":
                // console.log('No se confirmo el Rechazo de la solicitud ' + id);
                break;
        }
    })

});

}


function confirmacionRechazar(id){

// const solicitud = document.querySelector("#go");
// const url = "aprobarSolicitud/" + solicitud.dataset.id.toString();

let comentario = "";

swal({
    title: 'Comentario opccional',
    icon: 'info',
    content: {
        element: "input",
        attributes: {
          placeholder: "Deja un comentario",
        },
      },
  })

  .then((value) => {

    if (value  == "") {
        value = "-";
    } 

    // console.log(value);

    const url = "rechazarSolicitud/" + id.toString() + "/" + value.toString();
    // console.log(url);

    swal({
        title: 'Confirmación',
        text: 'Esta seguro de Rechazar la solicitud?',
        icon: 'success',

        buttons: {
            No: "No",
            Si: "Si"
        },
    })

    .then((value) => {
        switch (value) {

            case "Si":
                window.location.href = url;
                // console.log('Se confirmo el Rechazo de la solictud ' + id);

                break;

            case "No":
                // console.log('No se confirmo el Rechazo de la solicitud ' + id);
                break;
        }
    })

});

}


function muestra_calendario(){
    console.log("Muestra calendario")
    // abrimos el calendario
    document.getElementById("fecha_sol").click();
}


// Funcion para formatear fecha
function format_fecha(fecha_srt) {

    const s = fecha_srt.split('-');
    const meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"];

    const fecha_formateada = s[2] + "-" + meses[parseInt(s[1]) - 1] + "-" + s[0]
    // console.log(fecha_formateada)

    return fecha_formateada

}

// Funcion para calcular la diferencia de dias entre dos fechas
function diferencia_dias(fecha1_str, fecha2_str){

    const fecha1_obj = new Date(fecha1_str);
    const fecha2_obj = new Date(fecha2_str);
    // const date_obj = document.getElementById("fecha_sol");
    // const fecha_vigencia_obj = new Date (date_obj.getAttribute('max'));
    const diffTime = fecha1_obj - fecha2_obj;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 

    console.log("Diferencia dias: " + diffDays)
    return diffDays
}

// Funcion que muestra el comentario de la solicitud
function mostrar_comentario(comentario){

    // console.log("Mostrando comentario...")
    // console.log(comentario)

    // const comentario = document.getElementById('comentario').getAttribute('data-comentario')

    swal({
        title: 'Comentario',
        text: comentario,
        icon: 'info',

        buttons: {
            OK: "OK"
        },
    })

}

// crea una funcion que reciba la fecha de solicitud y calcula la fecha final
function calcula_fecha_final(lista_dias_festivos_str, lista_nombres_festivos_str, semana){

    console.log("Calculando fecha final...");

    fecha_sol_str = document.getElementById('fecha_sol').value;
    let fecha_sol_obj = new Date(fecha_sol_str);
    let fecha_final_obj = new Date();
    let fecha_estimada_obj = new Date();
    let dias = parseInt(document.getElementById('num_dias_sol').value);

    // crea un array que guarde los dias festivos en formato string eliminando los espacios y los caracteres '[', '] y comillas simples '
    let dias_festivos = lista_dias_festivos_str.replace(/ /g, "").replace(/'/g, "").replace("[", "").replace("]", "").split(",");

    // crea un array que guarde los nombres de los dias festivos en formato string eliminando los espacios y los caracteres '[', '] y comillas simples '
    let nombres_festivos = lista_nombres_festivos_str.replace(/ /g, "").replace(/'/g, "").replace("[", "").replace("]", "").split(",");

    // imprieme semana junto a semana
    console.log("semana: " + semana);

    // si dias es igual a 1 retorna la fecha final igual a la fecha de solicitud
    if (dias == 1) {
        fecha_final_obj = fecha_sol_obj;
        console.log("fecha final: " + fecha_final_obj.toISOString().slice(0,10));
        return fecha_final_obj.toISOString().slice(0,10);
    }

    let f_sabados = new Boolean(true) , f_domingos = new Boolean(true), f_festivos = new Boolean(true); 
    let sabados = 0 , domingos = 0, festivos = 0;
    let nombre_festivo = "";

    // calcula la fecha estimda sumando los dias solicitados  a la fecha de solicitud menos 1 dia
    fecha_estimada_obj = new Date(fecha_sol_obj.getTime() + ((dias - 1) * 24 * 60 * 60 * 1000));
    // imprime la fecha estimada junto a la fecha estimada en formato string ano mes dia separados por guiones
    console.log("Primer fecha estimada con los dias solicitados: " + fecha_estimada_obj.toISOString().slice(0,10));

    // imprimir salto de linea
    console.log("");


    // --------------------- Primera estimacion de fecha estimada --------------------- //
    // Buascamos sabados  

    // si es semana Inglesa
    if (semana == "Inglesa") {
        // crea un ciclo for que verifique cuantos sabados hay entre la fecha de solicitud mas los dias solicitados
        for (let i = 0; i < dias; i++) {
            // crea una variable que guarde la fecha de solicitud mas los dias
            let fecha = new Date(fecha_sol_obj.getTime() + (i * 24 * 60 * 60 * 1000));

            // verifica si la fecha es sabado
            if (fecha.getDay() == 5) {
                // si es sabado suma 1 a la variable sabados
                sabados += 1;
            }
        }
    }

    // Buscamos domingos
    // crea un ciclo for que verifique cuantos domingos hay entre la fecha de solicitud mas los dias solicitados
    for (let i = 0; i < dias + sabados; i++) {
        // crea una variable que guarde la fecha de solicitud mas los dias
        let fecha = new Date(fecha_sol_obj.getTime() + (i * 24 * 60 * 60 * 1000));

        // verifica si la fecha es domingo
        if (fecha.getDay() == 6) {
            // si es domingo suma 1 a la variable domingos
            domingos += 1;
        }
    }

    // Buscamos dias festivos
    // Verificamos si entre al fecha de solicitud y la fecha estimada mas los sabados y los domingos, hay dias festivos

    // crea una variable que guarde los dias festivos
    for (let i = 0; i < (dias + sabados +  domingos); i++) {
        // crea una variable que guarde la fecha de solicitud mas los dias
        let fecha = new Date(fecha_sol_obj.getTime() + (i * 24 * 60 * 60 * 1000));

        // crea una variable que guarde la fecha de solicitud mas los dias en formato string año-mes-dia
        let fecha_str = fecha.toISOString().slice(0,10);

        // crea un ciclo for que recorra el arreglo dias_festivos
        for (let j = 0; j < dias_festivos.length; j++) {
            // verifica si la fecha de solicitud mas los dias es igual a algun dia festivo
            if (fecha_str == dias_festivos[j]) {
                    // si es igual suma 1 a la variable dias_festivos
                    festivos += 1;

                    // guarda el nombre del dia festivo
                    nombre_festivo = nombres_festivos[j];

                    // imprime el nombre del dia festivo
                    console.log("Dia festivo: " + nombre_festivo);

                    // imprime la fecha del dia festivo
                    console.log("Fecha del dia festivo: " + dias_festivos[j]);
                }
            }
    }

    //actualizamos la fecha estiamada
    fecha_estimada_obj = new Date(fecha_sol_obj.getTime() + ((dias - 1 + sabados + domingos + festivos) * 24 * 60 * 60 * 1000));
    

    // reverificacion de sabados, domingos y festivos
    while (f_sabados || f_domingos || f_festivos) {

        let k = 1;

        // impimimos en consola el valor de k
        console.log("Ciclo while: " + k);

        // Nueva verificacion de sabados en la fecha estimdada
        // si semana es Inglesa
        if (semana == "Inglesa") {
            // recalcumamos si la fecha estimada es sabado
            if (fecha_estimada_obj.getDay() == 5) {
                // si es sabado suma 1 a la variable sabados
                sabados += 1;

                f_sabados = true;
                
                //actualizamos la fecha estmada
                fecha_estimada_obj = new Date(fecha_estimada_obj.getTime() + (1 * 24 * 60 * 60 * 1000));

            }else {
                f_sabados = false;

                // imprime en consola no hay sabados
                console.log("No hay sabados");
            }
        } else {
            f_sabados = false;
            // imprime en consola no hay sabados
            console.log("No hay sabados");
        }

        // imprime en consola el valor de f_sabados
        console.log("f_sabados: " + f_sabados);

        // Nueva verificacion de domingos en la fecha estimada 
        // recalcumamos si la fecha estimada es domingo
        if (fecha_estimada_obj.getDay() == 6) {
            // si es domingo suma 1 a la variable domingos
            domingos += 1;
            f_domingos = true;

            //actualizamos la fecha estimada
            fecha_estimada_obj = new Date(fecha_estimada_obj.getTime() + (1 * 24 * 60 * 60 * 1000));
            
        } else {
            f_domingos = false;
            // imprime en consola no hay domingos
            console.log("No hay domingos");
        }

        // imprime en consola el valor de f_domingos
        console.log("f_domingos: " + f_domingos);


        // crea una variable que guarde la fecha estimada en formato string año-mes-dia
        let fecha_estimada_str = fecha_estimada_obj.toISOString().slice(0,10);
        
        // crea un ciclo for que recorra el arreglo dias_festivos
        for (let j = 0; j < dias_festivos.length; j++) {
            // verifica si la fecha estimada es igual a algun dia festivo
            if (fecha_estimada_str == dias_festivos[j]) {
                // si es igual suma 1 a la variable dias_festivos
                festivos += 1;
                f_festivos = true;

                //actualizamos la feestimada
                fecha_estimada_obj = new Date(fecha_estimada_obj.getTime() + (1 * 24 * 60 * 60 * 1000));

                // guarda el nombre del dia festivo
                nombre_festivo = nombres_festivos[j];

                // imprime el nombre del dia festivo
                console.log("Dia festivo: " + nombre_festivo);

            } else {
                f_festivos = false;
                // imprime en consola no hay festivos
                console.log("No hay festivos");
            }
        }

        // imprime en consola el valor de f_festivos
        console.log("f_festivos: " + f_festivos);

        // incrementamos el valor de k
        k += 1;
        break;

    }

    // imprimimos salimos del ciclo while
    console.log("Salimos del ciclo while");

    // imprime la cadena dias junto con dias
    console.log("dias: " + dias);

    // imrpime sabados
    console.log("sabados: " + sabados);

    // imprime domingos
    console.log("domingos: " + domingos);

    // imprime festivos
    console.log("festivos: " + festivos);

    // imprime el nombre festivo junto con nombre_festivo
    console.log("nombre festivo: " + nombre_festivo);
    
    // imprime la fecha estimada junto a la fecha estimada
    console.log("fecha estimada primera estimacion: " + fecha_estimada_obj.toISOString().slice(0,10));

    // imprimimos un salto de linea
    console.log("");

    // -------------------------Fin de primera estimacion-------------------------

    // obtenemos la diferencia entre la fecha de solicitud y la fecha estimada convertida en dias
    let diferencia = Math.round((fecha_estimada_obj.getTime() - fecha_sol_obj.getTime()) / (1000 * 60 * 60 * 24));

    // imprimimos la diferencia de dias entre la fecha de solicitud y la fecha estimada
    console.log();
    console.log("diferencia de dias: " + diferencia);
    console.log();


    // --------------------- Segunda estimacion de fecha estimada --------------------- //

    // borrado de variables sabados, domingos, festivos y nombre_festivo
    sabados = 0;
    domingos = 0;
    festivos = 0;
    nombre_festivo = "";

    // Buascamos sabados  

    // si es semana Inglesa
    if (semana == "Inglesa") {
        // crea un ciclo for que verifique cuantos sabados hay entre la fecha de solicitud mas los dias solicitados
        for (let i = 0; i < diferencia; i++) {
            // crea una variable que guarde la fecha de solicitud mas los dias
            let fecha = new Date(fecha_sol_obj.getTime() + (i * 24 * 60 * 60 * 1000));

            // verifica si la fecha es sabado
            if (fecha.getDay() == 5) {
                // si es sabado suma 1 a la variable sabados
                sabados += 1;
            }
        }
    }

    // Buscamos domingos
    // crea un ciclo for que verifique cuantos domingos hay entre la fecha de solicitud mas los dias solicitados
    for (let i = 0; i < diferencia; i++) {
        // crea una variable que guarde la fecha de solicitud mas los dias
        let fecha = new Date(fecha_sol_obj.getTime() + (i * 24 * 60 * 60 * 1000));

        // verifica si la fecha es domingo
        if (fecha.getDay() == 6) {
            // si es domingo suma 1 a la variable domingos
            domingos += 1;
        }
    }

    // Buscamos dias festivos
    // Verificamos si entre al fecha de solicitud y la fecha estimada mas los sabados y los domingos, hay dias festivos

    // crea una variable que guarde los dias festivos
    for (let i = 0; i < (diferencia); i++) {
        // crea una variable que guarde la fecha de solicitud mas los dias
        let fecha = new Date(fecha_sol_obj.getTime() + (i * 24 * 60 * 60 * 1000));

        // crea una variable que guarde la fecha de solicitud mas los dias en formato string año-mes-dia
        let fecha_str = fecha.toISOString().slice(0,10);

        // crea un ciclo for que recorra el arreglo dias_festivos
        for (let j = 0; j < dias_festivos.length; j++) {
            // verifica si la fecha de solicitud mas los dias es igual a algun dia festivo
            if (fecha_str == dias_festivos[j]) {
                    // si es igual suma 1 a la variable dias_festivos
                    festivos += 1;

                    // guarda el nombre del dia festivo
                    nombre_festivo = nombres_festivos[j];

                    // imprime el nombre del dia festivo
                    console.log("Dia festivo: " + nombre_festivo);

                    // imprime la fecha del dia festivo
                    console.log("Fecha del dia festivo: " + dias_festivos[j]);
                }
            }
    }

    //actualizamos la fecha estiamada
    fecha_estimada_obj = new Date(fecha_sol_obj.getTime() + ((dias - 1 + sabados + domingos + festivos) * 24 * 60 * 60 * 1000));
    

    // reverificacion de sabados, domingos y festivos
    while (f_sabados || f_domingos || f_festivos) {

        let k = 1;

        // impimimos en consola el valor de k
        console.log("Ciclo while: " + k);

        // Nueva verificacion de sabados en la fecha estimdada
        // si semana es Inglesa
        if (semana == "Inglesa") {
            // recalcumamos si la fecha estimada es sabado
            if (fecha_estimada_obj.getDay() == 5) {
                // si es sabado suma 1 a la variable sabados
                sabados += 1;

                f_sabados = true;
                
                //actualizamos la fecha estmada
                fecha_estimada_obj = new Date(fecha_estimada_obj.getTime() + (1 * 24 * 60 * 60 * 1000));

            }else {
                f_sabados = false;

                // imprime en consola no hay sabados
                console.log("No hay sabados");
            }
        } else {
            f_sabados = false;
            // imprime en consola no hay sabados
            console.log("No hay sabados");
        }

        // imprime en consola el valor de f_sabados
        console.log("f_sabados: " + f_sabados);

        // Nueva verificacion de domingos en la fecha estimada 
        // recalcumamos si la fecha estimada es domingo
        if (fecha_estimada_obj.getDay() == 6) {
            // si es domingo suma 1 a la variable domingos
            domingos += 1;
            f_domingos = true;

            //actualizamos la fecha estimada
            fecha_estimada_obj = new Date(fecha_estimada_obj.getTime() + (1 * 24 * 60 * 60 * 1000));
            
        } else {
            f_domingos = false;
            // imprime en consola no hay domingos
            console.log("No hay domingos");
        }

        // imprime en consola el valor de f_domingos
        console.log("f_domingos: " + f_domingos);


        // crea una variable que guarde la fecha estimada en formato string año-mes-dia
        let fecha_estimada_str = fecha_estimada_obj.toISOString().slice(0,10);
        
        // crea un ciclo for que recorra el arreglo dias_festivos
        for (let j = 0; j < dias_festivos.length; j++) {
            // verifica si la fecha estimada es igual a algun dia festivo
            if (fecha_estimada_str == dias_festivos[j]) {
                // si es igual suma 1 a la variable dias_festivos
                festivos += 1;
                f_festivos = true;

                //actualizamos la feestimada
                fecha_estimada_obj = new Date(fecha_estimada_obj.getTime() + (1 * 24 * 60 * 60 * 1000));

                // guarda el nombre del dia festivo
                nombre_festivo = nombres_festivos[j];

                // imprime el nombre del dia festivo
                console.log("Dia festivo: " + nombre_festivo);

                // imprime la fecha del dia festivo
                console.log("Fecha del dia festivo: " + fecha_str);

            } else {
                f_festivos = false;
                // imprime en consola no hay festivos
                console.log("No hay festivos");
            }
        }

        // imprime en consola el valor de f_festivos
        console.log("f_festivos: " + f_festivos);

        // incrementamos el valor de k
        k += 1;
        break;

    }

    // imprimimos salimos del ciclo while
    console.log("Salimos del ciclo while");

    // imprime la cadena dias junto con dias
    console.log("dias: " + dias);

    // imrpime sabados
    console.log("sabados: " + sabados);

    // imprime domingos
    console.log("domingos: " + domingos);

    // imprime festivos
    console.log("festivos: " + festivos);

    // imprime el nombre festivo junto con nombre_festivo
    console.log("nombre festivo: " + nombre_festivo);
    
    // imprime la fecha estimada junto a la fecha estimada
    console.log("fecha estimada segunda estimacion: " + fecha_estimada_obj.toISOString().slice(0,10));

    // imprimimos un salto de linea
    console.log("");

    // -------------------------Fin de segunda estimacion-------------------------
   
    // imprime la cadena fecha solicitud junto con fecha_sol
    console.log("fecha solicitud: " + fecha_sol_str);

    fecha_final_obj = fecha_estimada_obj;

    // imprime la fecha final junto a la fecha final
    console.log("fecha final total: " + fecha_final_obj.toISOString().slice(0,10));

    // retorna la fecha final en formato string año-mes-dia
    return fecha_final_obj.toISOString().slice(0,10);

}