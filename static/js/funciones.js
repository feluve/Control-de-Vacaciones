

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

function verifica_domingo(fecha){

    const fecha1 = new Date(fecha);
    // console.log("Dia de la semana: " + fecha1.getDay());

    if(fecha1.getDay() === 6){
        console.log("Es domingo")  
        return true
    }
    else{
        console.log("No es domingo")
        return false
    }

}

function validaciones(dias_festivos_str, nombres_festivos_str, dias_max_sol){

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
            text: 'No puede seleccionar más de 6 dias.',
            icon: 'error',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validadmos que tenga una fecha seleccionada
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
    // Validamos que la fecha seleccionado no sea mayor  a la fecha vencimientod de sus dias de vacacioens
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
    // // Validamos que no tenga solicitudes pendinetes
    // else if (solicitudes_pendientes > 0){

    //     swal({
    //         title: 'Información',
    //         text: 'No puede hacer más solicitudes ya que tiene una pendiente por autorizar.',
    //         icon: 'warning',
    
    //         buttons: {
    //             OK: "OK"
    //         },
    //     })

    // }
    //Validamos que tiene dias disponibles suficientes
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
    //Validamos que la fecha seleccionado no se adomingo
    else if (verifica_domingo(fecha_sol_obj)){

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
    //Confimamos el envio de la solicitud
    else{

        // const fecha_format = fecha_sol.getDay + "-" + fecha_sol.getMonth + "-" + fecha_sol.getFullYear

        swal({
            title: 'Confirmación',
            text: 'Esta seguro de enviar la solicitud por '+ dias_sol +' dia(s) en la fecha ' + format_fecha(fecha_sol_str) + ' ?',
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
                    document.getElementById('form').submit();
                    console.log('Se envio la solictud');


                    // swal({
                    //     title: 'Confirmación',
                    //     text: 'Solicitud envida correctamente.',
                    //     icon: 'success',
                    //     buttons: 'OK'
                    // })

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
    
    const url = "aprobarSolicitud/" + id.toString();
    console.log(url);
    
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
            console.log('Se confirmo la Aprobación de la solictud ' + id);

            break;

        case "No":
            console.log('No se confirmo la Aprobación de la solicitud ' + id);
            break;

    }
})


}

function confirmacionRechazar(id){

// const solicitud = document.querySelector("#go");
// const url = "aprobarSolicitud/" + solicitud.dataset.id.toString();

const url = "rechazarSolicitud/" + id.toString();
console.log(url);

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
}


function muestra_calendario(){
    // console.log("Muestra calendario")
    document.getElementById('fecha_sol').click();
}


function format_fecha(fecha_srt) {

    const s = fecha_srt.split('-');
    const meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"];

    const fecha_formateada = s[2] + "-" + meses[parseInt(s[1]) - 1] + "-" + s[0]
    // console.log(fecha_formateada)

    return fecha_formateada

}

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



// function verifica_fecha_festiva(){
    
//         // const fecha = "2023-02-06";
//         const n = parseInt(document.getElementById("n").innerText);
//         const fecha = document.getElementById('fecha_sol').value.trim();
//         let i;
//         let j = false;
    
//         console.log("Verificacion de fecha festiva")
//         // console.log("Fecha de entrada: " + fecha)
//         // console.log("Tamaño de la fecha de entrada: "+ fecha.length)
    
//         for(i = 1; i <= n; i++){
//     f = document.getElementById(i.toString()).innerText.trim()
//     if (f === fecha){
//             console.log("Encontramos fecha festiva: " + f);
//             j = true;
//         } 
//     }

//     // console.log(j)

//     return j

// }



// function post(){

//     console.log(document.getElementById('token').innerText)

//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "/registra_solicitud/", true);
//     xhr.setRequestHeader('Content-Type', 'application/json');
//     xhr.send(JSON.stringify({
//         fecha_sol: '2023-01-01',
//         dias_sol: 6
//     }));


//     xhr.onload = function() {
//     console.log("Hola")
//     console.log(this.responseText);
//     var data = JSON.parse(this.responseText);
//     console.log(data);
//     }

// }
