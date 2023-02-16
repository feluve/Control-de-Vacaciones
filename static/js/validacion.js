
function resta_dias(){

    if (parseInt(document.getElementById('dias_sol').value) > 1) {
        document.getElementById('dias_sol').value = parseInt(document.getElementById('dias_sol').value) -1;
        console.log("Restamos");
    }
}

function suma_dias(){
    
    if (parseInt(document.getElementById('dias_sol').value) < 6) {
        document.getElementById('dias_sol').value = parseInt(document.getElementById('dias_sol').value) +1;
        console.log("Sumamos");
    }
}

function verifica_domingo(fecha){
    const fecha1 = new Date(fecha);

    console.log("Dia de la semana: " + fecha1.getDay())

    if(fecha1.getDay() === 6){
        console.log("Es domingo")  
        return true
    }
    else{
        console.log("No es domingo")
        return false
    }

}

function validacion(){

    console.log("Verificando fecha ....");

    const dias_disp = parseInt(document.getElementById('dias_disp').innerText);
    const dias_sol = parseInt(document.getElementById('dias_sol').value);
    const fecha_sol = new Date(document.getElementById('fecha_sol').value);
    const fecha_sol_str = document.getElementById('fecha_sol').value;

    const solicitudes_pendientes = 0;

    const fecha_actual = new Date();
    const diffTime = (fecha_sol - fecha_actual);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 

    console.log("Diferencia de dias: " + diffDays);


    console.log("fes: " + verifica_fecha_festiva("2023-03-20"))

    // Validamos que no seleccionen mas dias
    if(dias_sol > 6){
        
        swal({
            title: 'Información',
            text: 'No puede seleccionar más 6 dias.',
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
    // Validamos que la fecha seleccionado no sea menos a la fecha actual
    else if(diffDays < 15){

        swal({
            title: 'Fecha inválida',
            text: 'La fecha seleccionada debe ser mayor a la fecha actual y 15 dias de acticipacion.',
            icon: 'error',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que la fecha seleccionado no sea una fecha festiva oficial
    else if(verifica_fecha_festiva()){

        swal({
            title: 'Fecha inválida',
            text: 'La fecha seleccionada es una fecha festiva. Selecciona una diferente.',
            icon: 'warning',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que no tenga solicitudes pendinetes
    else if (solicitudes_pendientes > 0){

        swal({
            title: 'Información',
            text: 'No puede hacer más solicitudes ya que tiene una pendiente por autorizar.',
            icon: 'warning',
    
            buttons: {
                OK: "OK"
            },
        })

    }
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
    else if (verifica_domingo(fecha_sol)){

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
            text: 'Esta seguro de enviar la solicitud por '+ dias_sol +' dia(s) en la fecha ' + fecha_sol_str + ' ?',
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
                    document.getElementById('dias_sol').disabled = false;

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

function verifica_fecha_festiva(){

    // const fecha = "2023-02-06";
    const n = parseInt(document.getElementById("n").innerText);
    const fecha = document.getElementById('fecha_sol').value.trim();
    let i;
    let j = false;

    console.log("Verificacion de fecha festiva")
    // console.log("Fecha de entrada: " + fecha)
    // console.log("Tamaño de la fecha de entrada: "+ fecha.length)

    for(i = 1; i <= n; i++){
        f = document.getElementById(i.toString()).innerText.trim()
        if (f === fecha){
            console.log("Encontramos fecha festiva: " + f);
            j = true;
        } 
    }

    // console.log(j)

    return j
    
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
                console.log('Se confirmo el Rechazo de la solictud ' + id);

                break;

            case "No":
                console.log('No se confirmo el Rechazo de la solicitud ' + id);
                break;

        }
    })
}

function prueba(a){

    console.log(typeof(a))
    console.log(a)
    
    const b = a.replace('[','').replace(']','').split(',');
    
    console.log(typeof(b))
    console.log(b)

}

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
